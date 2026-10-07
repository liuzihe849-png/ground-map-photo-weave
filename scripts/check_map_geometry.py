#!/usr/bin/env python3
"""Check ground-panel proportions; no image editing or aesthetic certification."""
import argparse
import json
import math
from pathlib import Path


def check(plan):
    corners = plan['corners']  # TL, TR, BR, BL in final photo pixels
    width, height = plan['map_crop_size']  # actual crop before projection
    if width <= 0 or height <= 0 or len(corners) != 4:
        raise ValueError('Positive crop size and four ordered corners required')
    edges = [(corners[(i + 1) % 4][0] - corners[i][0],
              corners[(i + 1) % 4][1] - corners[i][1]) for i in range(4)]
    lengths = [math.hypot(*e) for e in edges]
    if min(lengths) <= 0:
        raise ValueError('Degenerate panel edge')
    cross = [edges[i][0] * edges[(i + 1) % 4][1] -
             edges[i][1] * edges[(i + 1) % 4][0] for i in range(4)]
    errors = []
    if not (all(v > 0 for v in cross) or all(v < 0 for v in cross)):
        errors.append('Corners are self-crossing or non-convex')
    horizontal = (lengths[0] + lengths[2]) / 2 / width
    vertical = (lengths[1] + lengths[3]) / 2 / height
    anisotropy = max(horizontal / vertical, vertical / horizontal)
    opposite_ratio = max(lengths[0] / lengths[2], lengths[2] / lengths[0],
                         lengths[1] / lengths[3], lengths[3] / lengths[1])
    angle_errors = []
    for i in range(4):
        a, b = edges[i], edges[(i + 1) % 4]
        cosine = (a[0] * b[0] + a[1] * b[1]) / lengths[i] / lengths[(i + 1) % 4]
        angle_errors.append(abs(90 - math.degrees(math.acos(max(-1, min(1, cosine))))))
    mode = plan.get('projection', 'uniform-rotate')
    if mode == 'uniform-rotate':
        if anisotropy > 1.03:
            errors.append('Independent axis scaling detected; preserve map crop aspect')
        if opposite_ratio > 1.03 or max(angle_errors) > 3:
            errors.append('Shear/trapezoid detected in the near-top-down rectangle')
    elif mode == 'mild-perspective':
        if not plan.get('camera_reason', '').strip():
            errors.append('Perspective requires an observed source-camera reason')
        if anisotropy > 1.12 or opposite_ratio > 1.12 or max(angle_errors) > 10:
            errors.append('Perspective exceeds this reference style; reframe before warping')
    else:
        errors.append('Unknown projection mode')
    return {'geometry_pass': not errors, 'errors': errors,
            'axis_scale_ratio': round(anisotropy, 4),
            'opposite_edge_ratio': round(opposite_ratio, 4),
            'max_right_angle_error_degrees': round(max(angle_errors), 3),
            'scope': 'Geometry only. Shoe matte, shadows, map provenance and readable labels require separate actual-image inspection.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.plan.read_text(encoding='utf-8')))
    except (ValueError, KeyError, TypeError, IndexError) as exc:
        result = {'geometry_pass': False, 'errors': [str(exc)]}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        args.output.write_text(rendered + '\n', encoding='utf-8')
    raise SystemExit(0 if result['geometry_pass'] else 1)


if __name__ == '__main__':
    main()

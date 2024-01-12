// Original file: frontend_rpc/grpcdefs.proto

import type { NTCStatElement as _NTCStatElement, NTCStatElement__Output as _NTCStatElement__Output } from './NTCStatElement';

export interface NTCStat {
  'name'?: (string);
  'id'?: (string);
  'elements'?: (_NTCStatElement)[];
}

export interface NTCStat__Output {
  'name': (string);
  'id': (string);
  'elements': (_NTCStatElement__Output)[];
}

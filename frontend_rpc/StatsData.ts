// Original file: frontend_rpc/grpcdefs.proto

import type { NTCStat as _NTCStat, NTCStat__Output as _NTCStat__Output } from './NTCStat';

export interface StatsData {
  'ntc'?: (_NTCStat)[];
}

export interface StatsData__Output {
  'ntc': (_NTCStat__Output)[];
}

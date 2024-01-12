// Original file: frontend_rpc/grpcdefs.proto

import type { Speed as _Speed, Speed__Output as _Speed__Output } from './Speed';

export interface State {
  'name'?: (string);
  'isLocked'?: (boolean);
  'canDriveAuto'?: (boolean);
  'canDriveManual'?: (boolean);
  'isFatal'?: (boolean);
  'isWarn'?: (boolean);
  'speed'?: (_Speed);
}

export interface State__Output {
  'name': (string);
  'isLocked': (boolean);
  'canDriveAuto': (boolean);
  'canDriveManual': (boolean);
  'isFatal': (boolean);
  'isWarn': (boolean);
  'speed': (_Speed__Output);
}

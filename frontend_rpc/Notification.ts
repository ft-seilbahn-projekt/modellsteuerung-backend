// Original file: frontend_rpc/grpcdefs.proto

import type { Level as _Level, Level__Output as _Level__Output } from './Level';

export interface Notification {
  'id'?: (number);
  'level'?: (_Level);
  'title'?: (string);
  'description'?: (string);
  'location'?: (string);
  'startTime'?: (number | string);
  'errorrnr'?: (string);
  'possibleSources'?: (string)[];
}

export interface Notification__Output {
  'id': (number);
  'level': (_Level__Output);
  'title': (string);
  'description': (string);
  'location': (string);
  'startTime': (number);
  'errorrnr': (string);
  'possibleSources': (string)[];
}

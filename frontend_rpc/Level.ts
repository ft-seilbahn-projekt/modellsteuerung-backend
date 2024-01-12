// Original file: frontend_rpc/grpcdefs.proto

export const Level = {
  INFO: 'INFO',
  WARNING: 'WARNING',
  FATAL: 'FATAL',
} as const;

export type Level =
  | 'INFO'
  | 0
  | 'WARNING'
  | 1
  | 'FATAL'
  | 2

export type Level__Output = typeof Level[keyof typeof Level]

// Original file: frontend_rpc/grpcdefs.proto

export const Speed = {
  STOP: 'STOP',
  SLOW: 'SLOW',
  MEDIUM: 'MEDIUM',
  FAST: 'FAST',
} as const;

export type Speed =
  | 'STOP'
  | 0
  | 'SLOW'
  | 1
  | 'MEDIUM'
  | 2
  | 'FAST'
  | 3

export type Speed__Output = typeof Speed[keyof typeof Speed]

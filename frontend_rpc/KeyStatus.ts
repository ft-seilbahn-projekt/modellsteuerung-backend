// Original file: frontend_rpc/grpcdefs.proto


export interface KeyStatus {
  'isPulled'?: (boolean);
  'isVerified'?: (boolean);
  'username'?: (string);
}

export interface KeyStatus__Output {
  'isPulled': (boolean);
  'isVerified': (boolean);
  'username': (string);
}

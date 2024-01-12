// Original file: frontend_rpc/grpcdefs.proto


export interface Info {
  'project'?: (string);
  'version'?: (string);
  'description'?: (string);
  'author'?: (string);
  'contact'?: (string);
  'license'?: (string);
  'time'?: (number | string);
  'commit'?: (string);
}

export interface Info__Output {
  'project': (string);
  'version': (string);
  'description': (string);
  'author': (string);
  'contact': (string);
  'license': (string);
  'time': (number);
  'commit': (string);
}

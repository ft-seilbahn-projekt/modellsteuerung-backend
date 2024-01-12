import type * as grpc from '@grpc/grpc-js';
import type { MessageTypeDefinition } from '@grpc/proto-loader';

import type { BackendClient as _BackendClient, BackendDefinition as _BackendDefinition } from './Backend';

type SubtypeConstructor<Constructor extends new (...args: any) => any, Subtype> = {
  new(...args: ConstructorParameters<Constructor>): Subtype;
};

export interface ProtoGrpcType {
  Backend: SubtypeConstructor<typeof grpc.Client, _BackendClient> & { service: _BackendDefinition }
  Info: MessageTypeDefinition
  Void: MessageTypeDefinition
}


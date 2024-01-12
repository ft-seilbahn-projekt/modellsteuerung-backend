import type * as grpc from '@grpc/grpc-js';
import type { EnumTypeDefinition, MessageTypeDefinition } from '@grpc/proto-loader';

import type { BackendClient as _BackendClient, BackendDefinition as _BackendDefinition } from './Backend';

type SubtypeConstructor<Constructor extends new (...args: any) => any, Subtype> = {
  new(...args: ConstructorParameters<Constructor>): Subtype;
};

export interface ProtoGrpcType {
  Backend: SubtypeConstructor<typeof grpc.Client, _BackendClient> & { service: _BackendDefinition }
  Info: MessageTypeDefinition
  KeyPair: MessageTypeDefinition
  KeyStatus: MessageTypeDefinition
  Level: EnumTypeDefinition
  NTCStat: MessageTypeDefinition
  NTCStatElement: MessageTypeDefinition
  Notification: MessageTypeDefinition
  NotificationIdentifier: MessageTypeDefinition
  NotificationList: MessageTypeDefinition
  Speed: EnumTypeDefinition
  State: MessageTypeDefinition
  StatsData: MessageTypeDefinition
  Status: MessageTypeDefinition
  Void: MessageTypeDefinition
}


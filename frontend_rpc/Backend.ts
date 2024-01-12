// Original file: frontend_rpc/grpcdefs.proto

import type * as grpc from '@grpc/grpc-js'
import type { MethodDefinition } from '@grpc/proto-loader'
import type { Info as _Info, Info__Output as _Info__Output } from './Info';
import type { KeyPair as _KeyPair, KeyPair__Output as _KeyPair__Output } from './KeyPair';
import type { KeyStatus as _KeyStatus, KeyStatus__Output as _KeyStatus__Output } from './KeyStatus';
import type { NotificationIdentifier as _NotificationIdentifier, NotificationIdentifier__Output as _NotificationIdentifier__Output } from './NotificationIdentifier';
import type { NotificationList as _NotificationList, NotificationList__Output as _NotificationList__Output } from './NotificationList';
import type { State as _State, State__Output as _State__Output } from './State';
import type { StatsData as _StatsData, StatsData__Output as _StatsData__Output } from './StatsData';
import type { Status as _Status, Status__Output as _Status__Output } from './Status';
import type { Void as _Void, Void__Output as _Void__Output } from './Void';

export interface BackendClient extends grpc.Client {
  info(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_Info__Output>): grpc.ClientUnaryCall;
  info(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_Info__Output>): grpc.ClientUnaryCall;
  info(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_Info__Output>): grpc.ClientUnaryCall;
  info(argument: _Void, callback: grpc.requestCallback<_Info__Output>): grpc.ClientUnaryCall;
  info(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_Info__Output>): grpc.ClientUnaryCall;
  info(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_Info__Output>): grpc.ClientUnaryCall;
  info(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_Info__Output>): grpc.ClientUnaryCall;
  info(argument: _Void, callback: grpc.requestCallback<_Info__Output>): grpc.ClientUnaryCall;
  
  key_status(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_KeyStatus__Output>): grpc.ClientUnaryCall;
  key_status(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_KeyStatus__Output>): grpc.ClientUnaryCall;
  key_status(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_KeyStatus__Output>): grpc.ClientUnaryCall;
  key_status(argument: _Void, callback: grpc.requestCallback<_KeyStatus__Output>): grpc.ClientUnaryCall;
  keyStatus(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_KeyStatus__Output>): grpc.ClientUnaryCall;
  keyStatus(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_KeyStatus__Output>): grpc.ClientUnaryCall;
  keyStatus(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_KeyStatus__Output>): grpc.ClientUnaryCall;
  keyStatus(argument: _Void, callback: grpc.requestCallback<_KeyStatus__Output>): grpc.ClientUnaryCall;
  
  key_unlock(argument: _KeyPair, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_Status__Output>): grpc.ClientUnaryCall;
  key_unlock(argument: _KeyPair, metadata: grpc.Metadata, callback: grpc.requestCallback<_Status__Output>): grpc.ClientUnaryCall;
  key_unlock(argument: _KeyPair, options: grpc.CallOptions, callback: grpc.requestCallback<_Status__Output>): grpc.ClientUnaryCall;
  key_unlock(argument: _KeyPair, callback: grpc.requestCallback<_Status__Output>): grpc.ClientUnaryCall;
  keyUnlock(argument: _KeyPair, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_Status__Output>): grpc.ClientUnaryCall;
  keyUnlock(argument: _KeyPair, metadata: grpc.Metadata, callback: grpc.requestCallback<_Status__Output>): grpc.ClientUnaryCall;
  keyUnlock(argument: _KeyPair, options: grpc.CallOptions, callback: grpc.requestCallback<_Status__Output>): grpc.ClientUnaryCall;
  keyUnlock(argument: _KeyPair, callback: grpc.requestCallback<_Status__Output>): grpc.ClientUnaryCall;
  
  notifications(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_NotificationList__Output>): grpc.ClientUnaryCall;
  notifications(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_NotificationList__Output>): grpc.ClientUnaryCall;
  notifications(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_NotificationList__Output>): grpc.ClientUnaryCall;
  notifications(argument: _Void, callback: grpc.requestCallback<_NotificationList__Output>): grpc.ClientUnaryCall;
  notifications(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_NotificationList__Output>): grpc.ClientUnaryCall;
  notifications(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_NotificationList__Output>): grpc.ClientUnaryCall;
  notifications(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_NotificationList__Output>): grpc.ClientUnaryCall;
  notifications(argument: _Void, callback: grpc.requestCallback<_NotificationList__Output>): grpc.ClientUnaryCall;
  
  remove_notification(argument: _NotificationIdentifier, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_Void__Output>): grpc.ClientUnaryCall;
  remove_notification(argument: _NotificationIdentifier, metadata: grpc.Metadata, callback: grpc.requestCallback<_Void__Output>): grpc.ClientUnaryCall;
  remove_notification(argument: _NotificationIdentifier, options: grpc.CallOptions, callback: grpc.requestCallback<_Void__Output>): grpc.ClientUnaryCall;
  remove_notification(argument: _NotificationIdentifier, callback: grpc.requestCallback<_Void__Output>): grpc.ClientUnaryCall;
  removeNotification(argument: _NotificationIdentifier, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_Void__Output>): grpc.ClientUnaryCall;
  removeNotification(argument: _NotificationIdentifier, metadata: grpc.Metadata, callback: grpc.requestCallback<_Void__Output>): grpc.ClientUnaryCall;
  removeNotification(argument: _NotificationIdentifier, options: grpc.CallOptions, callback: grpc.requestCallback<_Void__Output>): grpc.ClientUnaryCall;
  removeNotification(argument: _NotificationIdentifier, callback: grpc.requestCallback<_Void__Output>): grpc.ClientUnaryCall;
  
  state(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_State__Output>): grpc.ClientUnaryCall;
  state(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_State__Output>): grpc.ClientUnaryCall;
  state(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_State__Output>): grpc.ClientUnaryCall;
  state(argument: _Void, callback: grpc.requestCallback<_State__Output>): grpc.ClientUnaryCall;
  state(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_State__Output>): grpc.ClientUnaryCall;
  state(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_State__Output>): grpc.ClientUnaryCall;
  state(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_State__Output>): grpc.ClientUnaryCall;
  state(argument: _Void, callback: grpc.requestCallback<_State__Output>): grpc.ClientUnaryCall;
  
  stats_data(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_StatsData__Output>): grpc.ClientUnaryCall;
  stats_data(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_StatsData__Output>): grpc.ClientUnaryCall;
  stats_data(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_StatsData__Output>): grpc.ClientUnaryCall;
  stats_data(argument: _Void, callback: grpc.requestCallback<_StatsData__Output>): grpc.ClientUnaryCall;
  statsData(argument: _Void, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_StatsData__Output>): grpc.ClientUnaryCall;
  statsData(argument: _Void, metadata: grpc.Metadata, callback: grpc.requestCallback<_StatsData__Output>): grpc.ClientUnaryCall;
  statsData(argument: _Void, options: grpc.CallOptions, callback: grpc.requestCallback<_StatsData__Output>): grpc.ClientUnaryCall;
  statsData(argument: _Void, callback: grpc.requestCallback<_StatsData__Output>): grpc.ClientUnaryCall;
  
}

export interface BackendHandlers extends grpc.UntypedServiceImplementation {
  info: grpc.handleUnaryCall<_Void__Output, _Info>;
  
  key_status: grpc.handleUnaryCall<_Void__Output, _KeyStatus>;
  
  key_unlock: grpc.handleUnaryCall<_KeyPair__Output, _Status>;
  
  notifications: grpc.handleUnaryCall<_Void__Output, _NotificationList>;
  
  remove_notification: grpc.handleUnaryCall<_NotificationIdentifier__Output, _Void>;
  
  state: grpc.handleUnaryCall<_Void__Output, _State>;
  
  stats_data: grpc.handleUnaryCall<_Void__Output, _StatsData>;
  
}

export interface BackendDefinition extends grpc.ServiceDefinition {
  info: MethodDefinition<_Void, _Info, _Void__Output, _Info__Output>
  key_status: MethodDefinition<_Void, _KeyStatus, _Void__Output, _KeyStatus__Output>
  key_unlock: MethodDefinition<_KeyPair, _Status, _KeyPair__Output, _Status__Output>
  notifications: MethodDefinition<_Void, _NotificationList, _Void__Output, _NotificationList__Output>
  remove_notification: MethodDefinition<_NotificationIdentifier, _Void, _NotificationIdentifier__Output, _Void__Output>
  state: MethodDefinition<_Void, _State, _Void__Output, _State__Output>
  stats_data: MethodDefinition<_Void, _StatsData, _Void__Output, _StatsData__Output>
}

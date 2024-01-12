// Original file: frontend_rpc/grpcdefs.proto

import type * as grpc from '@grpc/grpc-js'
import type { MethodDefinition } from '@grpc/proto-loader'
import type { Info as _Info, Info__Output as _Info__Output } from './Info';
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
  
}

export interface BackendHandlers extends grpc.UntypedServiceImplementation {
  info: grpc.handleUnaryCall<_Void__Output, _Info>;
  
}

export interface BackendDefinition extends grpc.ServiceDefinition {
  info: MethodDefinition<_Void, _Info, _Void__Output, _Info__Output>
}

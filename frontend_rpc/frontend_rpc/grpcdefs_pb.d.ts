import * as jspb from 'google-protobuf'



export class Void extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Void.AsObject;
  static toObject(includeInstance: boolean, msg: Void): Void.AsObject;
  static serializeBinaryToWriter(message: Void, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Void;
  static deserializeBinaryFromReader(message: Void, reader: jspb.BinaryReader): Void;
}

export namespace Void {
  export type AsObject = {
  }
}

export class Info extends jspb.Message {
  getProject(): string;
  setProject(value: string): Info;

  getVersion(): string;
  setVersion(value: string): Info;

  getDescription(): string;
  setDescription(value: string): Info;

  getAuthor(): string;
  setAuthor(value: string): Info;

  getContact(): string;
  setContact(value: string): Info;

  getLicense(): string;
  setLicense(value: string): Info;

  getTime(): number;
  setTime(value: number): Info;

  getCommit(): string;
  setCommit(value: string): Info;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Info.AsObject;
  static toObject(includeInstance: boolean, msg: Info): Info.AsObject;
  static serializeBinaryToWriter(message: Info, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Info;
  static deserializeBinaryFromReader(message: Info, reader: jspb.BinaryReader): Info;
}

export namespace Info {
  export type AsObject = {
    project: string,
    version: string,
    description: string,
    author: string,
    contact: string,
    license: string,
    time: number,
    commit: string,
  }
}


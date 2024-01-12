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

export class State extends jspb.Message {
  getName(): string;
  setName(value: string): State;

  getIsLocked(): boolean;
  setIsLocked(value: boolean): State;

  getCanDriveAuto(): boolean;
  setCanDriveAuto(value: boolean): State;

  getCanDriveManual(): boolean;
  setCanDriveManual(value: boolean): State;

  getIsFatal(): boolean;
  setIsFatal(value: boolean): State;

  getIsWarn(): boolean;
  setIsWarn(value: boolean): State;

  getSpeed(): Speed;
  setSpeed(value: Speed): State;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): State.AsObject;
  static toObject(includeInstance: boolean, msg: State): State.AsObject;
  static serializeBinaryToWriter(message: State, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): State;
  static deserializeBinaryFromReader(message: State, reader: jspb.BinaryReader): State;
}

export namespace State {
  export type AsObject = {
    name: string,
    isLocked: boolean,
    canDriveAuto: boolean,
    canDriveManual: boolean,
    isFatal: boolean,
    isWarn: boolean,
    speed: Speed,
  }
}

export class Notification extends jspb.Message {
  getId(): number;
  setId(value: number): Notification;

  getLevel(): Level;
  setLevel(value: Level): Notification;

  getTitle(): string;
  setTitle(value: string): Notification;

  getDescription(): string;
  setDescription(value: string): Notification;

  getLocation(): string;
  setLocation(value: string): Notification;

  getStartTime(): number;
  setStartTime(value: number): Notification;

  getErrorrnr(): string;
  setErrorrnr(value: string): Notification;

  getPossibleSourcesList(): Array<string>;
  setPossibleSourcesList(value: Array<string>): Notification;
  clearPossibleSourcesList(): Notification;
  addPossibleSources(value: string, index?: number): Notification;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Notification.AsObject;
  static toObject(includeInstance: boolean, msg: Notification): Notification.AsObject;
  static serializeBinaryToWriter(message: Notification, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Notification;
  static deserializeBinaryFromReader(message: Notification, reader: jspb.BinaryReader): Notification;
}

export namespace Notification {
  export type AsObject = {
    id: number,
    level: Level,
    title: string,
    description: string,
    location: string,
    startTime: number,
    errorrnr: string,
    possibleSourcesList: Array<string>,
  }
}

export class NotificationList extends jspb.Message {
  getNotificationsList(): Array<Notification>;
  setNotificationsList(value: Array<Notification>): NotificationList;
  clearNotificationsList(): NotificationList;
  addNotifications(value?: Notification, index?: number): Notification;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NotificationList.AsObject;
  static toObject(includeInstance: boolean, msg: NotificationList): NotificationList.AsObject;
  static serializeBinaryToWriter(message: NotificationList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NotificationList;
  static deserializeBinaryFromReader(message: NotificationList, reader: jspb.BinaryReader): NotificationList;
}

export namespace NotificationList {
  export type AsObject = {
    notificationsList: Array<Notification.AsObject>,
  }
}

export class NotificationIdentifier extends jspb.Message {
  getId(): number;
  setId(value: number): NotificationIdentifier;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NotificationIdentifier.AsObject;
  static toObject(includeInstance: boolean, msg: NotificationIdentifier): NotificationIdentifier.AsObject;
  static serializeBinaryToWriter(message: NotificationIdentifier, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NotificationIdentifier;
  static deserializeBinaryFromReader(message: NotificationIdentifier, reader: jspb.BinaryReader): NotificationIdentifier;
}

export namespace NotificationIdentifier {
  export type AsObject = {
    id: number,
  }
}

export class KeyPair extends jspb.Message {
  getId(): string;
  setId(value: string): KeyPair;

  getHmac(): string;
  setHmac(value: string): KeyPair;

  getUsername(): string;
  setUsername(value: string): KeyPair;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): KeyPair.AsObject;
  static toObject(includeInstance: boolean, msg: KeyPair): KeyPair.AsObject;
  static serializeBinaryToWriter(message: KeyPair, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): KeyPair;
  static deserializeBinaryFromReader(message: KeyPair, reader: jspb.BinaryReader): KeyPair;
}

export namespace KeyPair {
  export type AsObject = {
    id: string,
    hmac: string,
    username: string,
  }
}

export class Status extends jspb.Message {
  getValue(): boolean;
  setValue(value: boolean): Status;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Status.AsObject;
  static toObject(includeInstance: boolean, msg: Status): Status.AsObject;
  static serializeBinaryToWriter(message: Status, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Status;
  static deserializeBinaryFromReader(message: Status, reader: jspb.BinaryReader): Status;
}

export namespace Status {
  export type AsObject = {
    value: boolean,
  }
}

export class KeyStatus extends jspb.Message {
  getIsPulled(): boolean;
  setIsPulled(value: boolean): KeyStatus;

  getIsVerified(): boolean;
  setIsVerified(value: boolean): KeyStatus;

  getUsername(): string;
  setUsername(value: string): KeyStatus;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): KeyStatus.AsObject;
  static toObject(includeInstance: boolean, msg: KeyStatus): KeyStatus.AsObject;
  static serializeBinaryToWriter(message: KeyStatus, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): KeyStatus;
  static deserializeBinaryFromReader(message: KeyStatus, reader: jspb.BinaryReader): KeyStatus;
}

export namespace KeyStatus {
  export type AsObject = {
    isPulled: boolean,
    isVerified: boolean,
    username: string,
  }
}

export class StatsData extends jspb.Message {
  getNtcList(): Array<NTCStat>;
  setNtcList(value: Array<NTCStat>): StatsData;
  clearNtcList(): StatsData;
  addNtc(value?: NTCStat, index?: number): NTCStat;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): StatsData.AsObject;
  static toObject(includeInstance: boolean, msg: StatsData): StatsData.AsObject;
  static serializeBinaryToWriter(message: StatsData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): StatsData;
  static deserializeBinaryFromReader(message: StatsData, reader: jspb.BinaryReader): StatsData;
}

export namespace StatsData {
  export type AsObject = {
    ntcList: Array<NTCStat.AsObject>,
  }
}

export class NTCStat extends jspb.Message {
  getName(): string;
  setName(value: string): NTCStat;

  getId(): string;
  setId(value: string): NTCStat;

  getElementsList(): Array<NTCStatElement>;
  setElementsList(value: Array<NTCStatElement>): NTCStat;
  clearElementsList(): NTCStat;
  addElements(value?: NTCStatElement, index?: number): NTCStatElement;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NTCStat.AsObject;
  static toObject(includeInstance: boolean, msg: NTCStat): NTCStat.AsObject;
  static serializeBinaryToWriter(message: NTCStat, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NTCStat;
  static deserializeBinaryFromReader(message: NTCStat, reader: jspb.BinaryReader): NTCStat;
}

export namespace NTCStat {
  export type AsObject = {
    name: string,
    id: string,
    elementsList: Array<NTCStatElement.AsObject>,
  }
}

export class NTCStatElement extends jspb.Message {
  getTime(): number;
  setTime(value: number): NTCStatElement;

  getDegrees(): number;
  setDegrees(value: number): NTCStatElement;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NTCStatElement.AsObject;
  static toObject(includeInstance: boolean, msg: NTCStatElement): NTCStatElement.AsObject;
  static serializeBinaryToWriter(message: NTCStatElement, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NTCStatElement;
  static deserializeBinaryFromReader(message: NTCStatElement, reader: jspb.BinaryReader): NTCStatElement;
}

export namespace NTCStatElement {
  export type AsObject = {
    time: number,
    degrees: number,
  }
}

export enum Speed { 
  STOP = 0,
  SLOW = 1,
  MEDIUM = 2,
  FAST = 3,
}
export enum Level { 
  INFO = 0,
  WARNING = 1,
  FATAL = 2,
}

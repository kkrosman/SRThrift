/**
 * Autogenerated by Thrift Compiler (0.9.1)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.IO;
using Thrift;
using Thrift.Collections;
using System.Runtime.Serialization;
using Thrift.Protocol;
using Thrift.Transport;

namespace SRBanking.ThriftInterface
{

  #if !SILVERLIGHT
  [Serializable]
  #endif
  public partial class TransferID : TBase
  {
    private NodeID _Sender;
    private NodeID _Receiver;
    private long _LP;

    public NodeID Sender
    {
      get
      {
        return _Sender;
      }
      set
      {
        __isset.Sender = true;
        this._Sender = value;
      }
    }

    public NodeID Receiver
    {
      get
      {
        return _Receiver;
      }
      set
      {
        __isset.Receiver = true;
        this._Receiver = value;
      }
    }

    public long LP
    {
      get
      {
        return _LP;
      }
      set
      {
        __isset.LP = true;
        this._LP = value;
      }
    }


    public Isset __isset;
    #if !SILVERLIGHT
    [Serializable]
    #endif
    public struct Isset {
      public bool Sender;
      public bool Receiver;
      public bool LP;
    }

    public TransferID() {
    }

    public void Read (TProtocol iprot)
    {
      TField field;
      iprot.ReadStructBegin();
      while (true)
      {
        field = iprot.ReadFieldBegin();
        if (field.Type == TType.Stop) { 
          break;
        }
        switch (field.ID)
        {
          case 1:
            if (field.Type == TType.Struct) {
              Sender = new NodeID();
              Sender.Read(iprot);
            } else { 
              TProtocolUtil.Skip(iprot, field.Type);
            }
            break;
          case 2:
            if (field.Type == TType.Struct) {
              Receiver = new NodeID();
              Receiver.Read(iprot);
            } else { 
              TProtocolUtil.Skip(iprot, field.Type);
            }
            break;
          case 3:
            if (field.Type == TType.I64) {
              LP = iprot.ReadI64();
            } else { 
              TProtocolUtil.Skip(iprot, field.Type);
            }
            break;
          default: 
            TProtocolUtil.Skip(iprot, field.Type);
            break;
        }
        iprot.ReadFieldEnd();
      }
      iprot.ReadStructEnd();
    }

    public void Write(TProtocol oprot) {
      TStruct struc = new TStruct("TransferID");
      oprot.WriteStructBegin(struc);
      TField field = new TField();
      if (Sender != null && __isset.Sender) {
        field.Name = "Sender";
        field.Type = TType.Struct;
        field.ID = 1;
        oprot.WriteFieldBegin(field);
        Sender.Write(oprot);
        oprot.WriteFieldEnd();
      }
      if (Receiver != null && __isset.Receiver) {
        field.Name = "Receiver";
        field.Type = TType.Struct;
        field.ID = 2;
        oprot.WriteFieldBegin(field);
        Receiver.Write(oprot);
        oprot.WriteFieldEnd();
      }
      if (__isset.LP) {
        field.Name = "LP";
        field.Type = TType.I64;
        field.ID = 3;
        oprot.WriteFieldBegin(field);
        oprot.WriteI64(LP);
        oprot.WriteFieldEnd();
      }
      oprot.WriteFieldStop();
      oprot.WriteStructEnd();
    }

    public override string ToString() {
      StringBuilder sb = new StringBuilder("TransferID(");
      sb.Append("Sender: ");
      sb.Append(Sender== null ? "<null>" : Sender.ToString());
      sb.Append(",Receiver: ");
      sb.Append(Receiver== null ? "<null>" : Receiver.ToString());
      sb.Append(",LP: ");
      sb.Append(LP);
      sb.Append(")");
      return sb.ToString();
    }

  }

}
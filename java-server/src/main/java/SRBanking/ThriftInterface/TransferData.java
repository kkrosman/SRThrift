/**
 * Autogenerated by Thrift Compiler (0.9.1)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package SRBanking.ThriftInterface;

import org.apache.thrift.scheme.IScheme;
import org.apache.thrift.scheme.SchemeFactory;
import org.apache.thrift.scheme.StandardScheme;

import org.apache.thrift.scheme.TupleScheme;
import org.apache.thrift.protocol.TTupleProtocol;
import org.apache.thrift.protocol.TProtocolException;
import org.apache.thrift.EncodingUtils;
import org.apache.thrift.TException;
import org.apache.thrift.async.AsyncMethodCallback;
import org.apache.thrift.server.AbstractNonblockingServer.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.EnumMap;
import java.util.Set;
import java.util.HashSet;
import java.util.EnumSet;
import java.util.Collections;
import java.util.BitSet;
import java.nio.ByteBuffer;
import java.util.Arrays;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class TransferData implements org.apache.thrift.TBase<TransferData, TransferData._Fields>, java.io.Serializable, Cloneable, Comparable<TransferData> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("TransferData");

  private static final org.apache.thrift.protocol.TField TRANSFER_ID_FIELD_DESC = new org.apache.thrift.protocol.TField("transferID", org.apache.thrift.protocol.TType.STRUCT, (short)1);
  private static final org.apache.thrift.protocol.TField RECEIVER_FIELD_DESC = new org.apache.thrift.protocol.TField("receiver", org.apache.thrift.protocol.TType.STRUCT, (short)2);
  private static final org.apache.thrift.protocol.TField VALUE_FIELD_DESC = new org.apache.thrift.protocol.TField("value", org.apache.thrift.protocol.TType.I64, (short)3);

  private static final Map<Class<? extends IScheme>, SchemeFactory> schemes = new HashMap<Class<? extends IScheme>, SchemeFactory>();
  static {
    schemes.put(StandardScheme.class, new TransferDataStandardSchemeFactory());
    schemes.put(TupleScheme.class, new TransferDataTupleSchemeFactory());
  }

  public TransferID transferID; // required
  public NodeID receiver; // required
  public long value; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    TRANSFER_ID((short)1, "transferID"),
    RECEIVER((short)2, "receiver"),
    VALUE((short)3, "value");

    private static final Map<String, _Fields> byName = new HashMap<String, _Fields>();

    static {
      for (_Fields field : EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // TRANSFER_ID
          return TRANSFER_ID;
        case 2: // RECEIVER
          return RECEIVER;
        case 3: // VALUE
          return VALUE;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    public static _Fields findByName(String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final String _fieldName;

    _Fields(short thriftId, String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments
  private static final int __VALUE_ISSET_ID = 0;
  private byte __isset_bitfield = 0;
  public static final Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.TRANSFER_ID, new org.apache.thrift.meta_data.FieldMetaData("transferID", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, TransferID.class)));
    tmpMap.put(_Fields.RECEIVER, new org.apache.thrift.meta_data.FieldMetaData("receiver", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, NodeID.class)));
    tmpMap.put(_Fields.VALUE, new org.apache.thrift.meta_data.FieldMetaData("value", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.I64        , "AccountBalanceType")));
    metaDataMap = Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(TransferData.class, metaDataMap);
  }

  public TransferData() {
  }

  public TransferData(
    TransferID transferID,
    NodeID receiver,
    long value)
  {
    this();
    this.transferID = transferID;
    this.receiver = receiver;
    this.value = value;
    setValueIsSet(true);
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public TransferData(TransferData other) {
    __isset_bitfield = other.__isset_bitfield;
    if (other.isSetTransferID()) {
      this.transferID = new TransferID(other.transferID);
    }
    if (other.isSetReceiver()) {
      this.receiver = new NodeID(other.receiver);
    }
    this.value = other.value;
  }

  public TransferData deepCopy() {
    return new TransferData(this);
  }

  @Override
  public void clear() {
    this.transferID = null;
    this.receiver = null;
    setValueIsSet(false);
    this.value = 0;
  }

  public TransferID getTransferID() {
    return this.transferID;
  }

  public TransferData setTransferID(TransferID transferID) {
    this.transferID = transferID;
    return this;
  }

  public void unsetTransferID() {
    this.transferID = null;
  }

  /** Returns true if field transferID is set (has been assigned a value) and false otherwise */
  public boolean isSetTransferID() {
    return this.transferID != null;
  }

  public void setTransferIDIsSet(boolean value) {
    if (!value) {
      this.transferID = null;
    }
  }

  public NodeID getReceiver() {
    return this.receiver;
  }

  public TransferData setReceiver(NodeID receiver) {
    this.receiver = receiver;
    return this;
  }

  public void unsetReceiver() {
    this.receiver = null;
  }

  /** Returns true if field receiver is set (has been assigned a value) and false otherwise */
  public boolean isSetReceiver() {
    return this.receiver != null;
  }

  public void setReceiverIsSet(boolean value) {
    if (!value) {
      this.receiver = null;
    }
  }

  public long getValue() {
    return this.value;
  }

  public TransferData setValue(long value) {
    this.value = value;
    setValueIsSet(true);
    return this;
  }

  public void unsetValue() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __VALUE_ISSET_ID);
  }

  /** Returns true if field value is set (has been assigned a value) and false otherwise */
  public boolean isSetValue() {
    return EncodingUtils.testBit(__isset_bitfield, __VALUE_ISSET_ID);
  }

  public void setValueIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __VALUE_ISSET_ID, value);
  }

  public void setFieldValue(_Fields field, Object value) {
    switch (field) {
    case TRANSFER_ID:
      if (value == null) {
        unsetTransferID();
      } else {
        setTransferID((TransferID)value);
      }
      break;

    case RECEIVER:
      if (value == null) {
        unsetReceiver();
      } else {
        setReceiver((NodeID)value);
      }
      break;

    case VALUE:
      if (value == null) {
        unsetValue();
      } else {
        setValue((Long)value);
      }
      break;

    }
  }

  public Object getFieldValue(_Fields field) {
    switch (field) {
    case TRANSFER_ID:
      return getTransferID();

    case RECEIVER:
      return getReceiver();

    case VALUE:
      return Long.valueOf(getValue());

    }
    throw new IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new IllegalArgumentException();
    }

    switch (field) {
    case TRANSFER_ID:
      return isSetTransferID();
    case RECEIVER:
      return isSetReceiver();
    case VALUE:
      return isSetValue();
    }
    throw new IllegalStateException();
  }

  @Override
  public boolean equals(Object that) {
    if (that == null)
      return false;
    if (that instanceof TransferData)
      return this.equals((TransferData)that);
    return false;
  }

  public boolean equals(TransferData that) {
    if (that == null)
      return false;

    boolean this_present_transferID = true && this.isSetTransferID();
    boolean that_present_transferID = true && that.isSetTransferID();
    if (this_present_transferID || that_present_transferID) {
      if (!(this_present_transferID && that_present_transferID))
        return false;
      if (!this.transferID.equals(that.transferID))
        return false;
    }

    boolean this_present_receiver = true && this.isSetReceiver();
    boolean that_present_receiver = true && that.isSetReceiver();
    if (this_present_receiver || that_present_receiver) {
      if (!(this_present_receiver && that_present_receiver))
        return false;
      if (!this.receiver.equals(that.receiver))
        return false;
    }

    boolean this_present_value = true;
    boolean that_present_value = true;
    if (this_present_value || that_present_value) {
      if (!(this_present_value && that_present_value))
        return false;
      if (this.value != that.value)
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    return 0;
  }

  @Override
  public int compareTo(TransferData other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = Boolean.valueOf(isSetTransferID()).compareTo(other.isSetTransferID());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetTransferID()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.transferID, other.transferID);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetReceiver()).compareTo(other.isSetReceiver());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetReceiver()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.receiver, other.receiver);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetValue()).compareTo(other.isSetValue());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetValue()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.value, other.value);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    schemes.get(iprot.getScheme()).getScheme().read(iprot, this);
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    schemes.get(oprot.getScheme()).getScheme().write(oprot, this);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder("TransferData(");
    boolean first = true;

    sb.append("transferID:");
    if (this.transferID == null) {
      sb.append("null");
    } else {
      sb.append(this.transferID);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("receiver:");
    if (this.receiver == null) {
      sb.append("null");
    } else {
      sb.append(this.receiver);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("value:");
    sb.append(this.value);
    first = false;
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    // check for sub-struct validity
    if (transferID != null) {
      transferID.validate();
    }
    if (receiver != null) {
      receiver.validate();
    }
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, ClassNotFoundException {
    try {
      // it doesn't seem like you should have to do this, but java serialization is wacky, and doesn't call the default constructor.
      __isset_bitfield = 0;
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class TransferDataStandardSchemeFactory implements SchemeFactory {
    public TransferDataStandardScheme getScheme() {
      return new TransferDataStandardScheme();
    }
  }

  private static class TransferDataStandardScheme extends StandardScheme<TransferData> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, TransferData struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // TRANSFER_ID
            if (schemeField.type == org.apache.thrift.protocol.TType.STRUCT) {
              struct.transferID = new TransferID();
              struct.transferID.read(iprot);
              struct.setTransferIDIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // RECEIVER
            if (schemeField.type == org.apache.thrift.protocol.TType.STRUCT) {
              struct.receiver = new NodeID();
              struct.receiver.read(iprot);
              struct.setReceiverIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // VALUE
            if (schemeField.type == org.apache.thrift.protocol.TType.I64) {
              struct.value = iprot.readI64();
              struct.setValueIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          default:
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();

      // check for required fields of primitive type, which can't be checked in the validate method
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, TransferData struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.transferID != null) {
        oprot.writeFieldBegin(TRANSFER_ID_FIELD_DESC);
        struct.transferID.write(oprot);
        oprot.writeFieldEnd();
      }
      if (struct.receiver != null) {
        oprot.writeFieldBegin(RECEIVER_FIELD_DESC);
        struct.receiver.write(oprot);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldBegin(VALUE_FIELD_DESC);
      oprot.writeI64(struct.value);
      oprot.writeFieldEnd();
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class TransferDataTupleSchemeFactory implements SchemeFactory {
    public TransferDataTupleScheme getScheme() {
      return new TransferDataTupleScheme();
    }
  }

  private static class TransferDataTupleScheme extends TupleScheme<TransferData> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, TransferData struct) throws org.apache.thrift.TException {
      TTupleProtocol oprot = (TTupleProtocol) prot;
      BitSet optionals = new BitSet();
      if (struct.isSetTransferID()) {
        optionals.set(0);
      }
      if (struct.isSetReceiver()) {
        optionals.set(1);
      }
      if (struct.isSetValue()) {
        optionals.set(2);
      }
      oprot.writeBitSet(optionals, 3);
      if (struct.isSetTransferID()) {
        struct.transferID.write(oprot);
      }
      if (struct.isSetReceiver()) {
        struct.receiver.write(oprot);
      }
      if (struct.isSetValue()) {
        oprot.writeI64(struct.value);
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, TransferData struct) throws org.apache.thrift.TException {
      TTupleProtocol iprot = (TTupleProtocol) prot;
      BitSet incoming = iprot.readBitSet(3);
      if (incoming.get(0)) {
        struct.transferID = new TransferID();
        struct.transferID.read(iprot);
        struct.setTransferIDIsSet(true);
      }
      if (incoming.get(1)) {
        struct.receiver = new NodeID();
        struct.receiver.read(iprot);
        struct.setReceiverIsSet(true);
      }
      if (incoming.get(2)) {
        struct.value = iprot.readI64();
        struct.setValueIsSet(true);
      }
    }
  }

}


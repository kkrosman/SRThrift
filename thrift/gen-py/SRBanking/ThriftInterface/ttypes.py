#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class IPAddress:
  """
  Attributes:
   - IP
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'IP', None, None, ), # 1
  )

  def __init__(self, IP=None,):
    self.IP = IP

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.IP = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IPAddress')
    if self.IP is not None:
      oprot.writeFieldBegin('IP', TType.STRING, 1)
      oprot.writeString(self.IP)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class NodeID:
  """
  Attributes:
   - address
   - port
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'address', (IPAddress, IPAddress.thrift_spec), None, ), # 1
    (2, TType.I32, 'port', None, None, ), # 2
  )

  def __init__(self, address=None, port=None,):
    self.address = address
    self.port = port

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.address = IPAddress()
          self.address.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.port = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NodeID')
    if self.address is not None:
      oprot.writeFieldBegin('address', TType.STRUCT, 1)
      self.address.write(oprot)
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 2)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TransferID:
  """
  Attributes:
   - sender
   - receiver
   - counter
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'sender', (NodeID, NodeID.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'receiver', (NodeID, NodeID.thrift_spec), None, ), # 2
    (3, TType.I64, 'counter', None, None, ), # 3
  )

  def __init__(self, sender=None, receiver=None, counter=None,):
    self.sender = sender
    self.receiver = receiver
    self.counter = counter

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.sender = NodeID()
          self.sender.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.receiver = NodeID()
          self.receiver.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.counter = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TransferID')
    if self.sender is not None:
      oprot.writeFieldBegin('sender', TType.STRUCT, 1)
      self.sender.write(oprot)
      oprot.writeFieldEnd()
    if self.receiver is not None:
      oprot.writeFieldBegin('receiver', TType.STRUCT, 2)
      self.receiver.write(oprot)
      oprot.writeFieldEnd()
    if self.counter is not None:
      oprot.writeFieldBegin('counter', TType.I64, 3)
      oprot.writeI64(self.counter)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Swarm:
  """
  Attributes:
   - transfer
   - leader
   - members
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'transfer', (TransferID, TransferID.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'leader', (NodeID, NodeID.thrift_spec), None, ), # 2
    (3, TType.LIST, 'members', (TType.STRUCT,(NodeID, NodeID.thrift_spec)), None, ), # 3
  )

  def __init__(self, transfer=None, leader=None, members=None,):
    self.transfer = transfer
    self.leader = leader
    self.members = members

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.transfer = TransferID()
          self.transfer.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.leader = NodeID()
          self.leader.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.members = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = NodeID()
            _elem5.read(iprot)
            self.members.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Swarm')
    if self.transfer is not None:
      oprot.writeFieldBegin('transfer', TType.STRUCT, 1)
      self.transfer.write(oprot)
      oprot.writeFieldEnd()
    if self.leader is not None:
      oprot.writeFieldBegin('leader', TType.STRUCT, 2)
      self.leader.write(oprot)
      oprot.writeFieldEnd()
    if self.members is not None:
      oprot.writeFieldBegin('members', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.members))
      for iter6 in self.members:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TransferData:
  """
  Attributes:
   - transferID
   - value
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'transferID', (TransferID, TransferID.thrift_spec), None, ), # 1
    (2, TType.I64, 'value', None, None, ), # 2
  )

  def __init__(self, transferID=None, value=None,):
    self.transferID = transferID
    self.value = value

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.transferID = TransferID()
          self.transferID.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.value = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TransferData')
    if self.transferID is not None:
      oprot.writeFieldBegin('transferID', TType.STRUCT, 1)
      self.transferID.write(oprot)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.I64, 2)
      oprot.writeI64(self.value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class NotSwarmMemeber(TException):
  """
  Attributes:
   - receiverNode
   - transfer
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'receiverNode', (NodeID, NodeID.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'transfer', (TransferID, TransferID.thrift_spec), None, ), # 2
  )

  def __init__(self, receiverNode=None, transfer=None,):
    self.receiverNode = receiverNode
    self.transfer = transfer

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.receiverNode = NodeID()
          self.receiverNode.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.transfer = TransferID()
          self.transfer.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NotSwarmMemeber')
    if self.receiverNode is not None:
      oprot.writeFieldBegin('receiverNode', TType.STRUCT, 1)
      self.receiverNode.write(oprot)
      oprot.writeFieldEnd()
    if self.transfer is not None:
      oprot.writeFieldBegin('transfer', TType.STRUCT, 2)
      self.transfer.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class WrongSwarmLeader(TException):
  """
  Attributes:
   - receiverNode
   - leader
   - transfer
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'receiverNode', (NodeID, NodeID.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'leader', (NodeID, NodeID.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'transfer', (TransferID, TransferID.thrift_spec), None, ), # 3
  )

  def __init__(self, receiverNode=None, leader=None, transfer=None,):
    self.receiverNode = receiverNode
    self.leader = leader
    self.transfer = transfer

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.receiverNode = NodeID()
          self.receiverNode.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.leader = NodeID()
          self.leader.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.transfer = TransferID()
          self.transfer.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('WrongSwarmLeader')
    if self.receiverNode is not None:
      oprot.writeFieldBegin('receiverNode', TType.STRUCT, 1)
      self.receiverNode.write(oprot)
      oprot.writeFieldEnd()
    if self.leader is not None:
      oprot.writeFieldBegin('leader', TType.STRUCT, 2)
      self.leader.write(oprot)
      oprot.writeFieldEnd()
    if self.transfer is not None:
      oprot.writeFieldBegin('transfer', TType.STRUCT, 3)
      self.transfer.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AlreadySwarmMemeber(TException):
  """
  Attributes:
   - receiverNode
   - leader
   - transfer
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'receiverNode', (NodeID, NodeID.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'leader', (NodeID, NodeID.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'transfer', (TransferID, TransferID.thrift_spec), None, ), # 3
  )

  def __init__(self, receiverNode=None, leader=None, transfer=None,):
    self.receiverNode = receiverNode
    self.leader = leader
    self.transfer = transfer

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.receiverNode = NodeID()
          self.receiverNode.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.leader = NodeID()
          self.leader.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.transfer = TransferID()
          self.transfer.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AlreadySwarmMemeber')
    if self.receiverNode is not None:
      oprot.writeFieldBegin('receiverNode', TType.STRUCT, 1)
      self.receiverNode.write(oprot)
      oprot.writeFieldEnd()
    if self.leader is not None:
      oprot.writeFieldBegin('leader', TType.STRUCT, 2)
      self.leader.write(oprot)
      oprot.writeFieldEnd()
    if self.transfer is not None:
      oprot.writeFieldBegin('transfer', TType.STRUCT, 3)
      self.transfer.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
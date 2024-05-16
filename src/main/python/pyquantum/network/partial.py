from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import io.netty.channel.ChannelHandlerAdapter as _ChannelHandlerAdapter
_ChannelHandlerAdapter = _ChannelHandlerAdapter
import java.lang.String as _String
_String = _String
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import io.netty.channel.ChannelInboundHandlerAdapter as _ChannelInboundHandlerAdapter
_ChannelInboundHandlerAdapter = _ChannelInboundHandlerAdapter
import dev.ultreon.quantum.network.partial.PacketCombiner as _PacketCombiner
_PacketCombiner = _PacketCombiner
import io.netty.handler.codec.MessageToMessageDecoder as _MessageToMessageDecoder
_MessageToMessageDecoder = _MessageToMessageDecoder
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketCombiner():
    """dev.ultreon.quantum.network.partial.PacketCombiner"""
 
    @staticmethod
    def _wrap(java_value: _PacketCombiner) -> 'PacketCombiner':
        return PacketCombiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketCombiner):
        """
        Dynamic initializer for PacketCombiner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketCombiner__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketCombiner__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def channelActive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelActive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelActive(arg0)

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).handlerRemoved(arg0)

    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool._wrap(super(ChannelHandlerAdapter, self).isSharable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def channelUnregistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelUnregistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelUnregistered(arg0)

    @override
    @overload
    def channelReadComplete(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelReadComplete(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelReadComplete(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PacketCombiner()"""
        val = _PacketCombiner()
        self.__wrapper = val

    @override
    @overload
    def channelRegistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelRegistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelRegistered(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def channelWritabilityChanged(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelWritabilityChanged(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelWritabilityChanged(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PacketCombiner()"""
        val = _PacketCombiner()
        self.__wrapper = val

    @override
    @overload
    def channelInactive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelInactive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelInactive(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def userEventTriggered(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.userEventTriggered(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).userEventTriggered(arg0, arg1)

    @override
    @overload
    def channelRead(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.handler.codec.MessageToMessageDecoder.channelRead(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(_MessageToMessageDecoder, self).channelRead(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).handlerAdded(arg0)

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).exceptionCaught(arg0, arg1)

    @overload
    def acceptInboundMessage(self, arg0: object) -> bool:
        """public boolean io.netty.handler.codec.MessageToMessageDecoder.acceptInboundMessage(java.lang.Object) throws java.lang.Exception"""
        return bool._wrap(super(_MessageToMessageDecoder, self).acceptInboundMessage(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PacketCombiner
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import io.netty.channel.ChannelHandlerAdapter as _ChannelHandlerAdapter
_ChannelHandlerAdapter = _ChannelHandlerAdapter
import java.lang.String as _String
_String = _String
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import io.netty.channel.ChannelInboundHandlerAdapter as _ChannelInboundHandlerAdapter
_ChannelInboundHandlerAdapter = _ChannelInboundHandlerAdapter
import dev.ultreon.quantum.network.partial.PacketCombiner as _PacketCombiner
_PacketCombiner = _PacketCombiner
import io.netty.handler.codec.MessageToMessageDecoder as _MessageToMessageDecoder
_MessageToMessageDecoder = _MessageToMessageDecoder
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketCombiner():
    """dev.ultreon.quantum.network.partial.PacketCombiner"""
 
    @staticmethod
    def _wrap(java_value: _PacketCombiner) -> 'PacketCombiner':
        return PacketCombiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketCombiner):
        """
        Dynamic initializer for PacketCombiner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketCombiner__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketCombiner__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def channelActive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelActive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelActive(arg0)

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).handlerRemoved(arg0)

    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool._wrap(super(ChannelHandlerAdapter, self).isSharable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def channelUnregistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelUnregistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelUnregistered(arg0)

    @override
    @overload
    def channelReadComplete(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelReadComplete(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelReadComplete(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PacketCombiner()"""
        val = _PacketCombiner()
        self.__wrapper = val

    @override
    @overload
    def channelRegistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelRegistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelRegistered(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def channelWritabilityChanged(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelWritabilityChanged(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelWritabilityChanged(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PacketCombiner()"""
        val = _PacketCombiner()
        self.__wrapper = val

    @override
    @overload
    def channelInactive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelInactive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelInactive(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def userEventTriggered(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.userEventTriggered(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).userEventTriggered(arg0, arg1)

    @override
    @overload
    def channelRead(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.handler.codec.MessageToMessageDecoder.channelRead(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(_MessageToMessageDecoder, self).channelRead(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).handlerAdded(arg0)

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).exceptionCaught(arg0, arg1)

    @overload
    def acceptInboundMessage(self, arg0: object) -> bool:
        """public boolean io.netty.handler.codec.MessageToMessageDecoder.acceptInboundMessage(java.lang.Object) throws java.lang.Exception"""
        return bool._wrap(super(_MessageToMessageDecoder, self).acceptInboundMessage(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PacketCombiner 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PartialPacketEncoder
import dev.ultreon.quantum.network.partial.PartialPacketEncoder as _PartialPacketEncoder
_PartialPacketEncoder = _PartialPacketEncoder
import io.netty.handler.codec.MessageToByteEncoder as _MessageToByteEncoder
_MessageToByteEncoder = _MessageToByteEncoder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import io.netty.channel.ChannelOutboundHandlerAdapter as _ChannelOutboundHandlerAdapter
_ChannelOutboundHandlerAdapter = _ChannelOutboundHandlerAdapter
from builtins import type
import io.netty.channel.ChannelHandlerAdapter as _ChannelHandlerAdapter
_ChannelHandlerAdapter = _ChannelHandlerAdapter
import java.lang.String as _String
_String = _String
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import java.lang.Integer as _int
import java.net.SocketAddress as SocketAddress
import io.netty.channel.ChannelPromise as ChannelPromise
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PartialPacketEncoder():
    """dev.ultreon.quantum.network.partial.PartialPacketEncoder"""
 
    @staticmethod
    def _wrap(java_value: _PartialPacketEncoder) -> 'PartialPacketEncoder':
        return PartialPacketEncoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PartialPacketEncoder):
        """
        Dynamic initializer for PartialPacketEncoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PartialPacketEncoder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PartialPacketEncoder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PartialPacketEncoder()"""
        val = _PartialPacketEncoder()
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'ChannelHandlerContext', arg1: object, arg2: 'ChannelPromise'):
        """public void io.netty.handler.codec.MessageToByteEncoder.write(io.netty.channel.ChannelHandlerContext,java.lang.Object,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_MessageToByteEncoder, self).write(arg0, arg1, arg2)

    @override
    @overload
    def read(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.read(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).read(arg0)

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).handlerRemoved(arg0)

    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool._wrap(super(ChannelHandlerAdapter, self).isSharable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def flush(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.flush(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).flush(arg0)

    @override
    @overload
    def bind(self, arg0: 'ChannelHandlerContext', arg1: 'SocketAddress', arg2: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.bind(io.netty.channel.ChannelHandlerContext,java.net.SocketAddress,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).bind(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def deregister(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.deregister(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).deregister(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disconnect(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.disconnect(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).disconnect(arg0, arg1)

    @override
    @overload
    def close(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.close(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).close(arg0, arg1)

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).exceptionCaught(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def connect(self, arg0: 'ChannelHandlerContext', arg1: 'SocketAddress', arg2: 'SocketAddress', arg3: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.connect(io.netty.channel.ChannelHandlerContext,java.net.SocketAddress,java.net.SocketAddress,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).connect(arg0, arg1, arg2, arg3)

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).handlerAdded(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PartialPacketEncoder()"""
        val = _PartialPacketEncoder()
        self.__wrapper = val

    @overload
    def acceptOutboundMessage(self, arg0: object) -> bool:
        """public boolean io.netty.handler.codec.MessageToByteEncoder.acceptOutboundMessage(java.lang.Object) throws java.lang.Exception"""
        return bool._wrap(super(_MessageToByteEncoder, self).acceptOutboundMessage(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PartialPacketDecoder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import io.netty.channel.ChannelHandlerAdapter as _ChannelHandlerAdapter
_ChannelHandlerAdapter = _ChannelHandlerAdapter
import java.lang.String as _String
_String = _String
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import io.netty.channel.ChannelInboundHandlerAdapter as _ChannelInboundHandlerAdapter
_ChannelInboundHandlerAdapter = _ChannelInboundHandlerAdapter
import io.netty.handler.codec.ByteToMessageDecoder.Cumulator as Cumulator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import dev.ultreon.quantum.network.partial.PartialPacketDecoder as _PartialPacketDecoder
_PartialPacketDecoder = _PartialPacketDecoder
import java.lang.Long as _long
import io.netty.handler.codec.ByteToMessageDecoder as _ByteToMessageDecoder
_ByteToMessageDecoder = _ByteToMessageDecoder
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PartialPacketDecoder():
    """dev.ultreon.quantum.network.partial.PartialPacketDecoder"""
 
    @staticmethod
    def _wrap(java_value: _PartialPacketDecoder) -> 'PartialPacketDecoder':
        return PartialPacketDecoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PartialPacketDecoder):
        """
        Dynamic initializer for PartialPacketDecoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PartialPacketDecoder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PartialPacketDecoder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool._wrap(super(ChannelHandlerAdapter, self).isSharable())

    @override
    @overload
    def channelUnregistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelUnregistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelUnregistered(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public final void io.netty.handler.codec.ByteToMessageDecoder.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ByteToMessageDecoder, self).handlerRemoved(arg0)

    @override
    @overload
    def isSingleDecode(self) -> bool:
        """public boolean io.netty.handler.codec.ByteToMessageDecoder.isSingleDecode()"""
        return bool._wrap(super(ByteToMessageDecoder, self).isSingleDecode())

    @override
    @overload
    def channelRegistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelRegistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelRegistered(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def channelWritabilityChanged(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelWritabilityChanged(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelWritabilityChanged(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).handlerAdded(arg0)

    @override
    @overload
    def channelInactive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.handler.codec.ByteToMessageDecoder.channelInactive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ByteToMessageDecoder, self).channelInactive(arg0)

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).exceptionCaught(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def channelActive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelActive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelInboundHandlerAdapter, self).channelActive(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PartialPacketDecoder()"""
        val = _PartialPacketDecoder()
        self.__wrapper = val

    @override
    @overload
    def channelReadComplete(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.handler.codec.ByteToMessageDecoder.channelReadComplete(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ByteToMessageDecoder, self).channelReadComplete(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setCumulator(self, arg0: 'Cumulator'):
        """public void io.netty.handler.codec.ByteToMessageDecoder.setCumulator(io.netty.handler.codec.ByteToMessageDecoder$Cumulator)"""
        super(_ByteToMessageDecoder, self).setCumulator(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PartialPacketDecoder()"""
        val = _PartialPacketDecoder()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def userEventTriggered(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.handler.codec.ByteToMessageDecoder.userEventTriggered(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(_ByteToMessageDecoder, self).userEventTriggered(arg0, arg1)

    @override
    @overload
    def channelRead(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.handler.codec.ByteToMessageDecoder.channelRead(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(_ByteToMessageDecoder, self).channelRead(arg0, arg1)

    @override
    @overload
    def setDiscardAfterReads(self, arg0: int):
        """public void io.netty.handler.codec.ByteToMessageDecoder.setDiscardAfterReads(int)"""
        super(_ByteToMessageDecoder, self).setDiscardAfterReads(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setSingleDecode(self, arg0: bool):
        """public void io.netty.handler.codec.ByteToMessageDecoder.setSingleDecode(boolean)"""
        super(_ByteToMessageDecoder, self).setSingleDecode(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PartialMergeData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.network.partial.PartialMergeData as _PartialMergeData
_PartialMergeData = _PartialMergeData
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class PartialMergeData():
    """dev.ultreon.quantum.network.partial.PartialMergeData"""
 
    @staticmethod
    def _wrap(java_value: _PartialMergeData) -> 'PartialMergeData':
        return PartialMergeData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PartialMergeData):
        """
        Dynamic initializer for PartialMergeData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PartialMergeData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PartialMergeData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.partial.PartialMergeData.toString()"""
        return str._wrap(super(PartialMergeData, self).toString())

    @overload
    def totalLength(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialMergeData.totalLength()"""
        return int._wrap(super(PartialMergeData, self).totalLength())

    @overload
    def integrityCheck(self):
        """public void dev.ultreon.quantum.network.partial.PartialMergeData.integrityCheck() throws dev.ultreon.quantum.network.PacketIntegrityException"""
        super(PartialMergeData, self).integrityCheck()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.partial.PartialMergeData.equals(java.lang.Object)"""
        return bool._wrap(super(_PartialMergeData, self).equals(arg0))

    @overload
    def sequenceId(self) -> int:
        """public long dev.ultreon.quantum.network.partial.PartialMergeData.sequenceId()"""
        return int._wrap(super(PartialMergeData, self).sequenceId())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialMergeData.hashCode()"""
        return int._wrap(super(PartialMergeData, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def parts(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.network.partial.PartialPacket> dev.ultreon.quantum.network.partial.PartialMergeData.parts()"""
        return 'List'._wrap(super(PartialMergeData, self).parts())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def length(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialMergeData.length()"""
        return int._wrap(super(PartialMergeData, self).length())

    @overload
    def packetId(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialMergeData.packetId()"""
        return int._wrap(super(PartialMergeData, self).packetId())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isComplete(self) -> bool:
        """public boolean dev.ultreon.quantum.network.partial.PartialMergeData.isComplete()"""
        return bool._wrap(super(PartialMergeData, self).isComplete())

    @overload
    def load(self, arg0: 'PartialPacket'):
        """public void dev.ultreon.quantum.network.partial.PartialMergeData.load(dev.ultreon.quantum.network.partial.PartialPacket)"""
        super(_PartialMergeData, self).load(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: 'PartialPacket'):
        """public dev.ultreon.quantum.network.partial.PartialMergeData(long,dev.ultreon.quantum.network.partial.PartialPacket)"""
        val = _PartialMergeData(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PacketSplitter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import io.netty.channel.ChannelOutboundHandlerAdapter as _ChannelOutboundHandlerAdapter
_ChannelOutboundHandlerAdapter = _ChannelOutboundHandlerAdapter
from builtins import type
import io.netty.channel.ChannelHandlerAdapter as _ChannelHandlerAdapter
_ChannelHandlerAdapter = _ChannelHandlerAdapter
import java.lang.String as _String
_String = _String
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import java.lang.Integer as _int
import java.net.SocketAddress as SocketAddress
import io.netty.handler.codec.MessageToMessageEncoder as _MessageToMessageEncoder
_MessageToMessageEncoder = _MessageToMessageEncoder
import io.netty.channel.ChannelPromise as ChannelPromise
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.network.partial.PacketSplitter as _PacketSplitter
_PacketSplitter = _PacketSplitter
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketSplitter():
    """dev.ultreon.quantum.network.partial.PacketSplitter"""
 
    @staticmethod
    def _wrap(java_value: _PacketSplitter) -> 'PacketSplitter':
        return PacketSplitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketSplitter):
        """
        Dynamic initializer for PacketSplitter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketSplitter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketSplitter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PacketSplitter()"""
        val = _PacketSplitter()
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.read(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).read(arg0)

    @override
    @overload
    def write(self, arg0: 'ChannelHandlerContext', arg1: object, arg2: 'ChannelPromise'):
        """public void io.netty.handler.codec.MessageToMessageEncoder.write(io.netty.channel.ChannelHandlerContext,java.lang.Object,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_MessageToMessageEncoder, self).write(arg0, arg1, arg2)

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).handlerRemoved(arg0)

    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool._wrap(super(ChannelHandlerAdapter, self).isSharable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def acceptOutboundMessage(self, arg0: object) -> bool:
        """public boolean io.netty.handler.codec.MessageToMessageEncoder.acceptOutboundMessage(java.lang.Object) throws java.lang.Exception"""
        return bool._wrap(super(_MessageToMessageEncoder, self).acceptOutboundMessage(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def flush(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.flush(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).flush(arg0)

    @override
    @overload
    def bind(self, arg0: 'ChannelHandlerContext', arg1: 'SocketAddress', arg2: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.bind(io.netty.channel.ChannelHandlerContext,java.net.SocketAddress,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).bind(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PacketSplitter()"""
        val = _PacketSplitter()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def deregister(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.deregister(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).deregister(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def disconnect(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.disconnect(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).disconnect(arg0, arg1)

    @override
    @overload
    def close(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.close(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).close(arg0, arg1)

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).exceptionCaught(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def connect(self, arg0: 'ChannelHandlerContext', arg1: 'SocketAddress', arg2: 'SocketAddress', arg3: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.connect(io.netty.channel.ChannelHandlerContext,java.net.SocketAddress,java.net.SocketAddress,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(_ChannelOutboundHandlerAdapter, self).connect(arg0, arg1, arg2, arg3)

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(_ChannelHandlerAdapter, self).handlerAdded(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PacketBufferInfo
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.network.PacketIO as _PacketIO
_PacketIO = _PacketIO
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import dev.ultreon.quantum.network.partial.PacketBufferInfo as _PacketBufferInfo
_PacketBufferInfo = _PacketBufferInfo
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketBufferInfo():
    """dev.ultreon.quantum.network.partial.PacketBufferInfo"""
 
    @staticmethod
    def _wrap(java_value: _PacketBufferInfo) -> 'PacketBufferInfo':
        return PacketBufferInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketBufferInfo):
        """
        Dynamic initializer for PacketBufferInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketBufferInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketBufferInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'PacketIO'):
        """public dev.ultreon.quantum.network.partial.PacketBufferInfo(int,long,dev.ultreon.quantum.network.PacketIO)"""
        val = _PacketBufferInfo(_int.valueOf(arg0), _long.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def sequence(self) -> int:
        """public long dev.ultreon.quantum.network.partial.PacketBufferInfo.sequence()"""
        return int._wrap(super(PacketBufferInfo, self).sequence())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def buffer(self) -> 'network.PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.partial.PacketBufferInfo.buffer()"""
        return 'network.PacketIO'._wrap(super(PacketBufferInfo, self).buffer())

    @overload
    def packetId(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PacketBufferInfo.packetId()"""
        return int._wrap(super(PacketBufferInfo, self).packetId())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PacketBufferInfo.hashCode()"""
        return int._wrap(super(PacketBufferInfo, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.partial.PacketBufferInfo.toString()"""
        return str._wrap(super(PacketBufferInfo, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.partial.PacketBufferInfo.equals(java.lang.Object)"""
        return bool._wrap(super(_PacketBufferInfo, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PartialPacket
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import io.netty.buffer.ByteBuf as _ByteBuf
_ByteBuf = _ByteBuf
import dev.ultreon.quantum.network.partial.PartialPacket as _PartialPacket
_PartialPacket = _PartialPacket
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import io.netty.buffer.ByteBuf as ByteBuf
import java.lang.Class as _Class
_Class = _Class
 
class PartialPacket():
    """dev.ultreon.quantum.network.partial.PartialPacket"""
 
    @staticmethod
    def _wrap(java_value: _PartialPacket) -> 'PartialPacket':
        return PartialPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PartialPacket):
        """
        Dynamic initializer for PartialPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PartialPacket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PartialPacket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def sequenceId(self) -> int:
        """public long dev.ultreon.quantum.network.partial.PartialPacket.sequenceId()"""
        return int._wrap(super(PartialPacket, self).sequenceId())

    @overload
    def packetId(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialPacket.packetId()"""
        return int._wrap(super(PartialPacket, self).packetId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def dataOffset(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialPacket.dataOffset()"""
        return int._wrap(super(PartialPacket, self).dataOffset())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def dataLength(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialPacket.dataLength()"""
        return int._wrap(super(PartialPacket, self).dataLength())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.partial.PartialPacket.equals(java.lang.Object)"""
        return bool._wrap(super(_PartialPacket, self).equals(arg0))

    @overload
    def encode(self, arg0: 'ByteBuf'):
        """public void dev.ultreon.quantum.network.partial.PartialPacket.encode(io.netty.buffer.ByteBuf)"""
        super(_PartialPacket, self).encode(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def data(self) -> 'ByteBuf':
        """public io.netty.buffer.ByteBuf dev.ultreon.quantum.network.partial.PartialPacket.data()"""
        return 'ByteBuf'._wrap(super(PartialPacket, self).data())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer'):
        """public dev.ultreon.quantum.network.partial.PartialPacket(int,long,int,int,java.nio.ByteBuffer)"""
        val = _PartialPacket(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'ByteBuf'):
        """public dev.ultreon.quantum.network.partial.PartialPacket(int,long,int,int,io.netty.buffer.ByteBuf)"""
        val = _PartialPacket(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.partial.PartialPacket.toString()"""
        return str._wrap(super(PartialPacket, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialPacket.hashCode()"""
        return int._wrap(super(PartialPacket, self).hashCode())
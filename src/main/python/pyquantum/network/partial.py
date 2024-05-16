from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.network.partial.PacketCombiner as __PacketCombiner
__PacketCombiner = __PacketCombiner
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import io.netty.handler.codec.MessageToMessageDecoder as __MessageToMessageDecoder
__MessageToMessageDecoder = __MessageToMessageDecoder
import io.netty.channel.ChannelHandlerAdapter as __ChannelHandlerAdapter
__ChannelHandlerAdapter = __ChannelHandlerAdapter
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import io.netty.channel.ChannelInboundHandlerAdapter as __ChannelInboundHandlerAdapter
__ChannelInboundHandlerAdapter = __ChannelInboundHandlerAdapter
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketCombiner(__MessageToMessageDecoder, MessageToMessageDecoder):
    """dev.ultreon.quantum.network.partial.PacketCombiner"""
 
    @staticmethod
    def __wrap(java_value: __PacketCombiner) -> 'PacketCombiner':
        return PacketCombiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketCombiner):
        """
        Dynamic initializer for PacketCombiner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def channelRegistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelRegistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelRegistered(arg0)

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).handlerAdded(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def channelUnregistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelUnregistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelUnregistered(arg0)

    @override
    @overload
    def channelWritabilityChanged(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelWritabilityChanged(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelWritabilityChanged(arg0)

    @override
    @overload
    def userEventTriggered(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.userEventTriggered(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).userEventTriggered(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def channelRead(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.handler.codec.MessageToMessageDecoder.channelRead(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(__MessageToMessageDecoder, self).channelRead(arg0, arg1)

    @override
    @overload
    def channelInactive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelInactive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelInactive(arg0)

    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool.__wrap(super(ChannelHandlerAdapter, self).isSharable())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PacketCombiner()"""
        val = __PacketCombiner()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def channelActive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelActive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelActive(arg0)

    @override
    @overload
    def channelReadComplete(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelReadComplete(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelReadComplete(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PacketCombiner()"""
        val = __PacketCombiner()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def acceptInboundMessage(self, arg0: object) -> bool:
        """public boolean io.netty.handler.codec.MessageToMessageDecoder.acceptInboundMessage(java.lang.Object) throws java.lang.Exception"""
        return bool.__wrap(super(__MessageToMessageDecoder, self).acceptInboundMessage(arg0))

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).handlerRemoved(arg0)

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).exceptionCaught(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PacketCombiner
import dev.ultreon.quantum.network.partial.PacketCombiner as __PacketCombiner
__PacketCombiner = __PacketCombiner
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import io.netty.handler.codec.MessageToMessageDecoder as __MessageToMessageDecoder
__MessageToMessageDecoder = __MessageToMessageDecoder
import io.netty.channel.ChannelHandlerAdapter as __ChannelHandlerAdapter
__ChannelHandlerAdapter = __ChannelHandlerAdapter
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import io.netty.channel.ChannelInboundHandlerAdapter as __ChannelInboundHandlerAdapter
__ChannelInboundHandlerAdapter = __ChannelInboundHandlerAdapter
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketCombiner(__MessageToMessageDecoder, MessageToMessageDecoder):
    """dev.ultreon.quantum.network.partial.PacketCombiner"""
 
    @staticmethod
    def __wrap(java_value: __PacketCombiner) -> 'PacketCombiner':
        return PacketCombiner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketCombiner):
        """
        Dynamic initializer for PacketCombiner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def channelRegistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelRegistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelRegistered(arg0)

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).handlerAdded(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def channelUnregistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelUnregistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelUnregistered(arg0)

    @override
    @overload
    def channelWritabilityChanged(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelWritabilityChanged(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelWritabilityChanged(arg0)

    @override
    @overload
    def userEventTriggered(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.userEventTriggered(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).userEventTriggered(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def channelRead(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.handler.codec.MessageToMessageDecoder.channelRead(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(__MessageToMessageDecoder, self).channelRead(arg0, arg1)

    @override
    @overload
    def channelInactive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelInactive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelInactive(arg0)

    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool.__wrap(super(ChannelHandlerAdapter, self).isSharable())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PacketCombiner()"""
        val = __PacketCombiner()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def channelActive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelActive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelActive(arg0)

    @override
    @overload
    def channelReadComplete(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelReadComplete(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelReadComplete(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PacketCombiner()"""
        val = __PacketCombiner()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def acceptInboundMessage(self, arg0: object) -> bool:
        """public boolean io.netty.handler.codec.MessageToMessageDecoder.acceptInboundMessage(java.lang.Object) throws java.lang.Exception"""
        return bool.__wrap(super(__MessageToMessageDecoder, self).acceptInboundMessage(arg0))

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).handlerRemoved(arg0)

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).exceptionCaught(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PacketCombiner 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PartialPacketEncoder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import io.netty.handler.codec.MessageToByteEncoder as __MessageToByteEncoder
__MessageToByteEncoder = __MessageToByteEncoder
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import dev.ultreon.quantum.network.partial.PartialPacketEncoder as __PartialPacketEncoder
__PartialPacketEncoder = __PartialPacketEncoder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import io.netty.channel.ChannelOutboundHandlerAdapter as __ChannelOutboundHandlerAdapter
__ChannelOutboundHandlerAdapter = __ChannelOutboundHandlerAdapter
import io.netty.channel.ChannelHandlerAdapter as __ChannelHandlerAdapter
__ChannelHandlerAdapter = __ChannelHandlerAdapter
import java.lang.String as __String
__String = __String
import java.net.SocketAddress as SocketAddress
import io.netty.channel.ChannelPromise as ChannelPromise
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PartialPacketEncoder(__MessageToByteEncoder, MessageToByteEncoder):
    """dev.ultreon.quantum.network.partial.PartialPacketEncoder"""
 
    @staticmethod
    def __wrap(java_value: __PartialPacketEncoder) -> 'PartialPacketEncoder':
        return PartialPacketEncoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PartialPacketEncoder):
        """
        Dynamic initializer for PartialPacketEncoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PartialPacketEncoder()"""
        val = __PartialPacketEncoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def close(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.close(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).close(arg0, arg1)

    @override
    @overload
    def flush(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.flush(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).flush(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def read(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.read(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).read(arg0)

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).handlerAdded(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def bind(self, arg0: 'ChannelHandlerContext', arg1: 'SocketAddress', arg2: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.bind(io.netty.channel.ChannelHandlerContext,java.net.SocketAddress,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).bind(arg0, arg1, arg2)

    @override
    @overload
    def disconnect(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.disconnect(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).disconnect(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def write(self, arg0: 'ChannelHandlerContext', arg1: object, arg2: 'ChannelPromise'):
        """public void io.netty.handler.codec.MessageToByteEncoder.write(io.netty.channel.ChannelHandlerContext,java.lang.Object,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__MessageToByteEncoder, self).write(arg0, arg1, arg2)

    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool.__wrap(super(ChannelHandlerAdapter, self).isSharable())

    @overload
    def acceptOutboundMessage(self, arg0: object) -> bool:
        """public boolean io.netty.handler.codec.MessageToByteEncoder.acceptOutboundMessage(java.lang.Object) throws java.lang.Exception"""
        return bool.__wrap(super(__MessageToByteEncoder, self).acceptOutboundMessage(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def connect(self, arg0: 'ChannelHandlerContext', arg1: 'SocketAddress', arg2: 'SocketAddress', arg3: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.connect(io.netty.channel.ChannelHandlerContext,java.net.SocketAddress,java.net.SocketAddress,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).connect(arg0, arg1, arg2, arg3)

    @override
    @overload
    def deregister(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.deregister(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).deregister(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).handlerRemoved(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PartialPacketEncoder()"""
        val = __PartialPacketEncoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).exceptionCaught(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PartialPacketDecoder
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import io.netty.handler.codec.ByteToMessageDecoder as __ByteToMessageDecoder
__ByteToMessageDecoder = __ByteToMessageDecoder
import dev.ultreon.quantum.network.partial.PartialPacketDecoder as __PartialPacketDecoder
__PartialPacketDecoder = __PartialPacketDecoder
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import io.netty.handler.codec.ByteToMessageDecoder.Cumulator as Cumulator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import io.netty.channel.ChannelHandlerAdapter as __ChannelHandlerAdapter
__ChannelHandlerAdapter = __ChannelHandlerAdapter
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import io.netty.channel.ChannelInboundHandlerAdapter as __ChannelInboundHandlerAdapter
__ChannelInboundHandlerAdapter = __ChannelInboundHandlerAdapter
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PartialPacketDecoder(__ByteToMessageDecoder, ByteToMessageDecoder):
    """dev.ultreon.quantum.network.partial.PartialPacketDecoder"""
 
    @staticmethod
    def __wrap(java_value: __PartialPacketDecoder) -> 'PartialPacketDecoder':
        return PartialPacketDecoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PartialPacketDecoder):
        """
        Dynamic initializer for PartialPacketDecoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isSingleDecode(self) -> bool:
        """public boolean io.netty.handler.codec.ByteToMessageDecoder.isSingleDecode()"""
        return bool.__wrap(super(ByteToMessageDecoder, self).isSingleDecode())

    @override
    @overload
    def channelRead(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.handler.codec.ByteToMessageDecoder.channelRead(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(__ByteToMessageDecoder, self).channelRead(arg0, arg1)

    @override
    @overload
    def channelRegistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelRegistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelRegistered(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def channelInactive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.handler.codec.ByteToMessageDecoder.channelInactive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ByteToMessageDecoder, self).channelInactive(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PartialPacketDecoder()"""
        val = __PartialPacketDecoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setSingleDecode(self, arg0: bool):
        """public void io.netty.handler.codec.ByteToMessageDecoder.setSingleDecode(boolean)"""
        super(__ByteToMessageDecoder, self).setSingleDecode(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PartialPacketDecoder()"""
        val = __PartialPacketDecoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def userEventTriggered(self, arg0: 'ChannelHandlerContext', arg1: object):
        """public void io.netty.handler.codec.ByteToMessageDecoder.userEventTriggered(io.netty.channel.ChannelHandlerContext,java.lang.Object) throws java.lang.Exception"""
        super(__ByteToMessageDecoder, self).userEventTriggered(arg0, arg1)

    @override
    @overload
    def setDiscardAfterReads(self, arg0: int):
        """public void io.netty.handler.codec.ByteToMessageDecoder.setDiscardAfterReads(int)"""
        super(__ByteToMessageDecoder, self).setDiscardAfterReads(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).handlerAdded(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def channelUnregistered(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelUnregistered(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelUnregistered(arg0)

    @override
    @overload
    def channelWritabilityChanged(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelWritabilityChanged(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelWritabilityChanged(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setCumulator(self, arg0: 'Cumulator'):
        """public void io.netty.handler.codec.ByteToMessageDecoder.setCumulator(io.netty.handler.codec.ByteToMessageDecoder$Cumulator)"""
        super(__ByteToMessageDecoder, self).setCumulator(arg0)

    @override
    @overload
    def channelReadComplete(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.handler.codec.ByteToMessageDecoder.channelReadComplete(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ByteToMessageDecoder, self).channelReadComplete(arg0)

    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool.__wrap(super(ChannelHandlerAdapter, self).isSharable())

    @override
    @overload
    def channelActive(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.channelActive(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).channelActive(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public final void io.netty.handler.codec.ByteToMessageDecoder.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ByteToMessageDecoder, self).handlerRemoved(arg0)

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelInboundHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(__ChannelInboundHandlerAdapter, self).exceptionCaught(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PartialMergeData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.partial.PartialMergeData as __PartialMergeData
__PartialMergeData = __PartialMergeData
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class PartialMergeData():
    """dev.ultreon.quantum.network.partial.PartialMergeData"""
 
    @staticmethod
    def __wrap(java_value: __PartialMergeData) -> 'PartialMergeData':
        return PartialMergeData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PartialMergeData):
        """
        Dynamic initializer for PartialMergeData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self, arg0: 'PartialPacket'):
        """public void dev.ultreon.quantum.network.partial.PartialMergeData.load(dev.ultreon.quantum.network.partial.PartialPacket)"""
        super(__PartialMergeData, self).load(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialMergeData.hashCode()"""
        return int.__wrap(super(PartialMergeData, self).hashCode())

    @overload
    def integrityCheck(self):
        """public void dev.ultreon.quantum.network.partial.PartialMergeData.integrityCheck() throws dev.ultreon.quantum.network.PacketIntegrityException"""
        super(PartialMergeData, self).integrityCheck()

    @overload
    def isComplete(self) -> bool:
        """public boolean dev.ultreon.quantum.network.partial.PartialMergeData.isComplete()"""
        return bool.__wrap(super(PartialMergeData, self).isComplete())

    @overload
    def length(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialMergeData.length()"""
        return int.__wrap(super(PartialMergeData, self).length())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def sequenceId(self) -> int:
        """public long dev.ultreon.quantum.network.partial.PartialMergeData.sequenceId()"""
        return int.__wrap(super(PartialMergeData, self).sequenceId())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.partial.PartialMergeData.equals(java.lang.Object)"""
        return bool.__wrap(super(__PartialMergeData, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def totalLength(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialMergeData.totalLength()"""
        return int.__wrap(super(PartialMergeData, self).totalLength())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.partial.PartialMergeData.toString()"""
        return str.__wrap(super(PartialMergeData, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: 'PartialPacket'):
        """public dev.ultreon.quantum.network.partial.PartialMergeData(long,dev.ultreon.quantum.network.partial.PartialPacket)"""
        val = __PartialMergeData(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def packetId(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialMergeData.packetId()"""
        return int.__wrap(super(PartialMergeData, self).packetId())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def parts(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.network.partial.PartialPacket> dev.ultreon.quantum.network.partial.PartialMergeData.parts()"""
        return 'List'.__wrap(super(PartialMergeData, self).parts()) 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PacketSplitter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.partial.PacketSplitter as __PacketSplitter
__PacketSplitter = __PacketSplitter
import io.netty.channel.ChannelHandlerContext as ChannelHandlerContext
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import io.netty.channel.ChannelOutboundHandlerAdapter as __ChannelOutboundHandlerAdapter
__ChannelOutboundHandlerAdapter = __ChannelOutboundHandlerAdapter
import io.netty.channel.ChannelHandlerAdapter as __ChannelHandlerAdapter
__ChannelHandlerAdapter = __ChannelHandlerAdapter
import java.lang.String as __String
__String = __String
import java.net.SocketAddress as SocketAddress
import io.netty.channel.ChannelPromise as ChannelPromise
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import io.netty.handler.codec.MessageToMessageEncoder as __MessageToMessageEncoder
__MessageToMessageEncoder = __MessageToMessageEncoder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketSplitter(__MessageToMessageEncoder, MessageToMessageEncoder):
    """dev.ultreon.quantum.network.partial.PacketSplitter"""
 
    @staticmethod
    def __wrap(java_value: __PacketSplitter) -> 'PacketSplitter':
        return PacketSplitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketSplitter):
        """
        Dynamic initializer for PacketSplitter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.partial.PacketSplitter()"""
        val = __PacketSplitter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def close(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.close(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).close(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'ChannelHandlerContext', arg1: object, arg2: 'ChannelPromise'):
        """public void io.netty.handler.codec.MessageToMessageEncoder.write(io.netty.channel.ChannelHandlerContext,java.lang.Object,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__MessageToMessageEncoder, self).write(arg0, arg1, arg2)

    @override
    @overload
    def flush(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.flush(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).flush(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def read(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.read(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).read(arg0)

    @override
    @overload
    def handlerAdded(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerAdded(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).handlerAdded(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.partial.PacketSplitter()"""
        val = __PacketSplitter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def bind(self, arg0: 'ChannelHandlerContext', arg1: 'SocketAddress', arg2: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.bind(io.netty.channel.ChannelHandlerContext,java.net.SocketAddress,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).bind(arg0, arg1, arg2)

    @override
    @overload
    def disconnect(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.disconnect(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).disconnect(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def acceptOutboundMessage(self, arg0: object) -> bool:
        """public boolean io.netty.handler.codec.MessageToMessageEncoder.acceptOutboundMessage(java.lang.Object) throws java.lang.Exception"""
        return bool.__wrap(super(__MessageToMessageEncoder, self).acceptOutboundMessage(arg0))

    @override
    @overload
    def isSharable(self) -> bool:
        """public boolean io.netty.channel.ChannelHandlerAdapter.isSharable()"""
        return bool.__wrap(super(ChannelHandlerAdapter, self).isSharable())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def connect(self, arg0: 'ChannelHandlerContext', arg1: 'SocketAddress', arg2: 'SocketAddress', arg3: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.connect(io.netty.channel.ChannelHandlerContext,java.net.SocketAddress,java.net.SocketAddress,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).connect(arg0, arg1, arg2, arg3)

    @override
    @overload
    def deregister(self, arg0: 'ChannelHandlerContext', arg1: 'ChannelPromise'):
        """public void io.netty.channel.ChannelOutboundHandlerAdapter.deregister(io.netty.channel.ChannelHandlerContext,io.netty.channel.ChannelPromise) throws java.lang.Exception"""
        super(__ChannelOutboundHandlerAdapter, self).deregister(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def handlerRemoved(self, arg0: 'ChannelHandlerContext'):
        """public void io.netty.channel.ChannelHandlerAdapter.handlerRemoved(io.netty.channel.ChannelHandlerContext) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).handlerRemoved(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def exceptionCaught(self, arg0: 'ChannelHandlerContext', arg1: 'Throwable'):
        """public void io.netty.channel.ChannelHandlerAdapter.exceptionCaught(io.netty.channel.ChannelHandlerContext,java.lang.Throwable) throws java.lang.Exception"""
        super(__ChannelHandlerAdapter, self).exceptionCaught(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PacketBufferInfo
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.partial.PacketBufferInfo as __PacketBufferInfo
__PacketBufferInfo = __PacketBufferInfo
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.network.PacketIO as __PacketIO
__PacketIO = __PacketIO
from builtins import int
 
class PacketBufferInfo():
    """dev.ultreon.quantum.network.partial.PacketBufferInfo"""
 
    @staticmethod
    def __wrap(java_value: __PacketBufferInfo) -> 'PacketBufferInfo':
        return PacketBufferInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketBufferInfo):
        """
        Dynamic initializer for PacketBufferInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.partial.PacketBufferInfo.toString()"""
        return str.__wrap(super(PacketBufferInfo, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'PacketIO'):
        """public dev.ultreon.quantum.network.partial.PacketBufferInfo(int,long,dev.ultreon.quantum.network.PacketIO)"""
        val = __PacketBufferInfo(__int.valueOf(arg0), __long.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.partial.PacketBufferInfo.equals(java.lang.Object)"""
        return bool.__wrap(super(__PacketBufferInfo, self).equals(arg0))

    @overload
    def sequence(self) -> int:
        """public long dev.ultreon.quantum.network.partial.PacketBufferInfo.sequence()"""
        return int.__wrap(super(PacketBufferInfo, self).sequence())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PacketBufferInfo.hashCode()"""
        return int.__wrap(super(PacketBufferInfo, self).hashCode())

    @overload
    def packetId(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PacketBufferInfo.packetId()"""
        return int.__wrap(super(PacketBufferInfo, self).packetId())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def buffer(self) -> 'network.PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.partial.PacketBufferInfo.buffer()"""
        return 'network.PacketIO'.__wrap(super(PacketBufferInfo, self).buffer())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.network.partial.PartialPacket
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.network.partial.PartialPacket as __PartialPacket
__PartialPacket = __PartialPacket
import java.lang.Object as __Object
__Object = __Object
import io.netty.buffer.ByteBuf as __ByteBuf
__ByteBuf = __ByteBuf
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
import io.netty.buffer.ByteBuf as ByteBuf
 
class PartialPacket():
    """dev.ultreon.quantum.network.partial.PartialPacket"""
 
    @staticmethod
    def __wrap(java_value: __PartialPacket) -> 'PartialPacket':
        return PartialPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PartialPacket):
        """
        Dynamic initializer for PartialPacket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialPacket.hashCode()"""
        return int.__wrap(super(PartialPacket, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer'):
        """public dev.ultreon.quantum.network.partial.PartialPacket(int,long,int,int,java.nio.ByteBuffer)"""
        val = __PartialPacket(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.partial.PartialPacket.toString()"""
        return str.__wrap(super(PartialPacket, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def encode(self, arg0: 'ByteBuf'):
        """public void dev.ultreon.quantum.network.partial.PartialPacket.encode(io.netty.buffer.ByteBuf)"""
        super(__PartialPacket, self).encode(arg0)

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'ByteBuf'):
        """public dev.ultreon.quantum.network.partial.PartialPacket(int,long,int,int,io.netty.buffer.ByteBuf)"""
        val = __PartialPacket(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def data(self) -> 'ByteBuf':
        """public io.netty.buffer.ByteBuf dev.ultreon.quantum.network.partial.PartialPacket.data()"""
        return 'ByteBuf'.__wrap(super(PartialPacket, self).data())

    @overload
    def dataOffset(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialPacket.dataOffset()"""
        return int.__wrap(super(PartialPacket, self).dataOffset())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.partial.PartialPacket.equals(java.lang.Object)"""
        return bool.__wrap(super(__PartialPacket, self).equals(arg0))

    @overload
    def sequenceId(self) -> int:
        """public long dev.ultreon.quantum.network.partial.PartialPacket.sequenceId()"""
        return int.__wrap(super(PartialPacket, self).sequenceId())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def packetId(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialPacket.packetId()"""
        return int.__wrap(super(PartialPacket, self).packetId())

    @overload
    def dataLength(self) -> int:
        """public int dev.ultreon.quantum.network.partial.PartialPacket.dataLength()"""
        return int.__wrap(super(PartialPacket, self).dataLength())
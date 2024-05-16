from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.net.ServerSocketHints as __ServerSocketHints
__ServerSocketHints = __ServerSocketHints
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ServerSocketHints():
    """com.badlogic.gdx.net.ServerSocketHints"""
 
    @staticmethod
    def __wrap(java_value: __ServerSocketHints) -> 'ServerSocketHints':
        return ServerSocketHints(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerSocketHints):
        """
        Dynamic initializer for ServerSocketHints.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.net.ServerSocketHints()"""
        val = __ServerSocketHints()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.net.ServerSocketHints()"""
        val = __ServerSocketHints()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.net.ServerSocketHints
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.net.ServerSocketHints as __ServerSocketHints
__ServerSocketHints = __ServerSocketHints
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ServerSocketHints():
    """com.badlogic.gdx.net.ServerSocketHints"""
 
    @staticmethod
    def __wrap(java_value: __ServerSocketHints) -> 'ServerSocketHints':
        return ServerSocketHints(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerSocketHints):
        """
        Dynamic initializer for ServerSocketHints.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.net.ServerSocketHints()"""
        val = __ServerSocketHints()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.net.ServerSocketHints()"""
        val = __ServerSocketHints()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.net.ServerSocketHints 
 
 
# CLASS: com.badlogic.gdx.net.ServerSocket
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
import com.badlogic.gdx.net.ServerSocket as __ServerSocket
__ServerSocket = __ServerSocket
 
class ServerSocket(ABC, pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.net.ServerSocket"""
 
    @staticmethod
    def __wrap(java_value: __ServerSocket) -> 'ServerSocket':
        return ServerSocket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerSocket):
        """
        Dynamic initializer for ServerSocket.
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
 
    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def accept(self, arg0: 'SocketHints'):
        """public abstract com.badlogic.gdx.net.Socket com.badlogic.gdx.net.ServerSocket.accept(com.badlogic.gdx.net.SocketHints)"""
        pass

    @abstractmethod
    def getProtocol(self, ):
        """public abstract com.badlogic.gdx.Net$Protocol com.badlogic.gdx.net.ServerSocket.getProtocol()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.net.HttpRequestBuilder
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.Net as __Net_HttpRequest
__HttpRequest = __Net_HttpRequest.HttpRequest
import com.badlogic.gdx.net.HttpRequestBuilder as __HttpRequestBuilder
__HttpRequestBuilder = __HttpRequestBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class HttpRequestBuilder():
    """com.badlogic.gdx.net.HttpRequestBuilder"""
 
    @staticmethod
    def __wrap(java_value: __HttpRequestBuilder) -> 'HttpRequestBuilder':
        return HttpRequestBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpRequestBuilder):
        """
        Dynamic initializer for HttpRequestBuilder.
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
    def timeout(self, arg0: int) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.timeout(int)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).timeout(__int.valueOf(arg0)))

    @overload
    def jsonContent(self, arg0: object) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.jsonContent(java.lang.Object)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).jsonContent(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.net.HttpRequestBuilder()"""
        val = __HttpRequestBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def basicAuthentication(self, arg0: str, arg1: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.basicAuthentication(java.lang.String,java.lang.String)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).basicAuthentication(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def method(self, arg0: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.method(java.lang.String)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).method(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def formEncodedContent(self, arg0: 'Map') -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.formEncodedContent(java.util.Map<java.lang.String, java.lang.String>)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).formEncodedContent(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.net.HttpRequestBuilder()"""
        val = __HttpRequestBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def followRedirects(self, arg0: bool) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.followRedirects(boolean)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).followRedirects(__boolean.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def build(self) -> 'pygdx.Net$HttpRequest':
        """public com.badlogic.gdx.Net$HttpRequest com.badlogic.gdx.net.HttpRequestBuilder.build()"""
        return 'pygdx.Net$HttpRequest'.__wrap(super(HttpRequestBuilder, self).build())

    @overload
    def header(self, arg0: str, arg1: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.header(java.lang.String,java.lang.String)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).header(arg0, arg1))

    @overload
    def content(self, arg0: 'InputStream', arg1: int) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.content(java.io.InputStream,long)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).content(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def url(self, arg0: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.url(java.lang.String)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).url(arg0))

    @overload
    def includeCredentials(self, arg0: bool) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.includeCredentials(boolean)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).includeCredentials(__boolean.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def newRequest(self) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.newRequest()"""
        return 'HttpRequestBuilder'.__wrap(super(HttpRequestBuilder, self).newRequest())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def content(self, arg0: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.content(java.lang.String)"""
        return 'HttpRequestBuilder'.__wrap(super(__HttpRequestBuilder, self).content(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.net.HttpStatus
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.net.HttpStatus as __HttpStatus
__HttpStatus = __HttpStatus
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HttpStatus():
    """com.badlogic.gdx.net.HttpStatus"""
 
    @staticmethod
    def __wrap(java_value: __HttpStatus) -> 'HttpStatus':
        return HttpStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpStatus):
        """
        Dynamic initializer for HttpStatus.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getStatusCode(self) -> int:
        """public int com.badlogic.gdx.net.HttpStatus.getStatusCode()"""
        return int.__wrap(super(HttpStatus, self).getStatusCode())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.net.HttpStatus(int)"""
        val = __HttpStatus(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.net.NetJavaSocketImpl
from pyquantum_helper import import_once as __import_once__
import java.net.Socket as Socket
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import com.badlogic.gdx.net.NetJavaSocketImpl as __NetJavaSocketImpl
__NetJavaSocketImpl = __NetJavaSocketImpl
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NetJavaSocketImpl(__Socket, Socket):
    """com.badlogic.gdx.net.NetJavaSocketImpl"""
 
    @staticmethod
    def __wrap(java_value: __NetJavaSocketImpl) -> 'NetJavaSocketImpl':
        return NetJavaSocketImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NetJavaSocketImpl):
        """
        Dynamic initializer for NetJavaSocketImpl.
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
    def getRemoteAddress(self) -> str:
        """public java.lang.String com.badlogic.gdx.net.NetJavaSocketImpl.getRemoteAddress()"""
        return str.__wrap(super(NetJavaSocketImpl, self).getRemoteAddress())

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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getInputStream(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.net.NetJavaSocketImpl.getInputStream()"""
        return 'InputStream'.__wrap(super(NetJavaSocketImpl, self).getInputStream())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.net.NetJavaSocketImpl.dispose()"""
        super(NetJavaSocketImpl, self).dispose()

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean com.badlogic.gdx.net.NetJavaSocketImpl.isConnected()"""
        return bool.__wrap(super(NetJavaSocketImpl, self).isConnected())

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Socket', arg1: 'SocketHints'):
        """public com.badlogic.gdx.net.NetJavaSocketImpl(java.net.Socket,com.badlogic.gdx.net.SocketHints)"""
        val = __NetJavaSocketImpl(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getOutputStream(self) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.net.NetJavaSocketImpl.getOutputStream()"""
        return 'OutputStream'.__wrap(super(NetJavaSocketImpl, self).getOutputStream())

    @overload
    def __init__(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'SocketHints'):
        """public com.badlogic.gdx.net.NetJavaSocketImpl(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.SocketHints)"""
        val = __NetJavaSocketImpl(arg0, arg1, __int.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.net.NetJavaServerSocketImpl
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.net.Socket as __Socket
__Socket = __Socket
import com.badlogic.gdx.Net as __Net_Protocol
__Protocol = __Net_Protocol.Protocol
import com.badlogic.gdx.net.NetJavaServerSocketImpl as __NetJavaServerSocketImpl
__NetJavaServerSocketImpl = __NetJavaServerSocketImpl
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NetJavaServerSocketImpl(__ServerSocket, ServerSocket):
    """com.badlogic.gdx.net.NetJavaServerSocketImpl"""
 
    @staticmethod
    def __wrap(java_value: __NetJavaServerSocketImpl) -> 'NetJavaServerSocketImpl':
        return NetJavaServerSocketImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NetJavaServerSocketImpl):
        """
        Dynamic initializer for NetJavaServerSocketImpl.
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
    def __init__(self, arg0: 'Protocol', arg1: int, arg2: 'ServerSocketHints'):
        """public com.badlogic.gdx.net.NetJavaServerSocketImpl(com.badlogic.gdx.Net$Protocol,int,com.badlogic.gdx.net.ServerSocketHints)"""
        val = __NetJavaServerSocketImpl(arg0, __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getProtocol(self) -> 'pygdx.Net$Protocol':
        """public com.badlogic.gdx.Net$Protocol com.badlogic.gdx.net.NetJavaServerSocketImpl.getProtocol()"""
        return 'pygdx.Net$Protocol'.__wrap(super(NetJavaServerSocketImpl, self).getProtocol())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def accept(self, arg0: 'SocketHints') -> 'Socket':
        """public com.badlogic.gdx.net.Socket com.badlogic.gdx.net.NetJavaServerSocketImpl.accept(com.badlogic.gdx.net.SocketHints)"""
        return 'Socket'.__wrap(super(__NetJavaServerSocketImpl, self).accept(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.net.NetJavaServerSocketImpl.dispose()"""
        super(NetJavaServerSocketImpl, self).dispose()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'ServerSocketHints'):
        """public com.badlogic.gdx.net.NetJavaServerSocketImpl(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.ServerSocketHints)"""
        val = __NetJavaServerSocketImpl(arg0, arg1, __int.valueOf(arg2), arg3)
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.net.HttpParametersUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
import com.badlogic.gdx.net.HttpParametersUtils as __HttpParametersUtils
__HttpParametersUtils = __HttpParametersUtils
from builtins import int
 
class HttpParametersUtils():
    """com.badlogic.gdx.net.HttpParametersUtils"""
 
    @staticmethod
    def __wrap(java_value: __HttpParametersUtils) -> 'HttpParametersUtils':
        return HttpParametersUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpParametersUtils):
        """
        Dynamic initializer for HttpParametersUtils.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def convertHttpParameters(arg0: 'Map') -> str:
        """public static java.lang.String com.badlogic.gdx.net.HttpParametersUtils.convertHttpParameters(java.util.Map<java.lang.String, java.lang.String>)"""
        return str.__wrap(__HttpParametersUtils.convertHttpParameters(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.net.HttpResponseHeader
import com.badlogic.gdx.net.HttpResponseHeader as __HttpResponseHeader
__HttpResponseHeader = __HttpResponseHeader
 
class HttpResponseHeader(ABC):
    """com.badlogic.gdx.net.HttpResponseHeader"""
 
    @staticmethod
    def __wrap(java_value: __HttpResponseHeader) -> 'HttpResponseHeader':
        return HttpResponseHeader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpResponseHeader):
        """
        Dynamic initializer for HttpResponseHeader.
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
 
 
# CLASS: com.badlogic.gdx.net.Socket
import com.badlogic.gdx.net.Socket as __Socket
__Socket = __Socket
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
 
class Socket(ABC, pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.net.Socket"""
 
    @staticmethod
    def __wrap(java_value: __Socket) -> 'Socket':
        return Socket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Socket):
        """
        Dynamic initializer for Socket.
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
 
    @abstractmethod
    def getRemoteAddress(self, ):
        """public abstract java.lang.String com.badlogic.gdx.net.Socket.getRemoteAddress()"""
        pass

    @abstractmethod
    def isConnected(self, ):
        """public abstract boolean com.badlogic.gdx.net.Socket.isConnected()"""
        pass

    @abstractmethod
    def getOutputStream(self, ):
        """public abstract java.io.OutputStream com.badlogic.gdx.net.Socket.getOutputStream()"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def getInputStream(self, ):
        """public abstract java.io.InputStream com.badlogic.gdx.net.Socket.getInputStream()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.net.NetJavaImpl
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.net.NetJavaImpl as __NetJavaImpl
__NetJavaImpl = __NetJavaImpl
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NetJavaImpl():
    """com.badlogic.gdx.net.NetJavaImpl"""
 
    @staticmethod
    def __wrap(java_value: __NetJavaImpl) -> 'NetJavaImpl':
        return NetJavaImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NetJavaImpl):
        """
        Dynamic initializer for NetJavaImpl.
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
    def __init__(self):
        """public com.badlogic.gdx.net.NetJavaImpl()"""
        val = __NetJavaImpl()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.net.NetJavaImpl()"""
        val = __NetJavaImpl()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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

    @overload
    def sendHttpRequest(self, arg0: 'HttpRequest', arg1: 'HttpResponseListener'):
        """public void com.badlogic.gdx.net.NetJavaImpl.sendHttpRequest(com.badlogic.gdx.Net$HttpRequest,com.badlogic.gdx.Net$HttpResponseListener)"""
        super(__NetJavaImpl, self).sendHttpRequest(arg0, arg1)

    @overload
    def cancelHttpRequest(self, arg0: 'HttpRequest'):
        """public void com.badlogic.gdx.net.NetJavaImpl.cancelHttpRequest(com.badlogic.gdx.Net$HttpRequest)"""
        super(__NetJavaImpl, self).cancelHttpRequest(arg0)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.net.NetJavaImpl(int)"""
        val = __NetJavaImpl(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.net.SocketHints
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.net.SocketHints as __SocketHints
__SocketHints = __SocketHints
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SocketHints():
    """com.badlogic.gdx.net.SocketHints"""
 
    @staticmethod
    def __wrap(java_value: __SocketHints) -> 'SocketHints':
        return SocketHints(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SocketHints):
        """
        Dynamic initializer for SocketHints.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.net.SocketHints()"""
        val = __SocketHints()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.net.SocketHints()"""
        val = __SocketHints()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.net.HttpRequestHeader
import com.badlogic.gdx.net.HttpRequestHeader as __HttpRequestHeader
__HttpRequestHeader = __HttpRequestHeader
 
class HttpRequestHeader(ABC):
    """com.badlogic.gdx.net.HttpRequestHeader"""
 
    @staticmethod
    def __wrap(java_value: __HttpRequestHeader) -> 'HttpRequestHeader':
        return HttpRequestHeader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpRequestHeader):
        """
        Dynamic initializer for HttpRequestHeader.
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
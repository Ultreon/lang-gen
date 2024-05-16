from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.net.HttpResponseHeader as _HttpResponseHeader
_HttpResponseHeader = _HttpResponseHeader
 
class HttpResponseHeader():
    """com.badlogic.gdx.net.HttpResponseHeader"""
 
    @staticmethod
    def _wrap(java_value: _HttpResponseHeader) -> 'HttpResponseHeader':
        return HttpResponseHeader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpResponseHeader):
        """
        Dynamic initializer for HttpResponseHeader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpResponseHeader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpResponseHeader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
  
 
 
# CLASS: com.badlogic.gdx.net.HttpResponseHeader
import com.badlogic.gdx.net.HttpResponseHeader as _HttpResponseHeader
_HttpResponseHeader = _HttpResponseHeader
 
class HttpResponseHeader():
    """com.badlogic.gdx.net.HttpResponseHeader"""
 
    @staticmethod
    def _wrap(java_value: _HttpResponseHeader) -> 'HttpResponseHeader':
        return HttpResponseHeader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpResponseHeader):
        """
        Dynamic initializer for HttpResponseHeader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpResponseHeader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpResponseHeader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
  
 
 
# CLASS: com.badlogic.gdx.net.HttpResponseHeader 
 
 
# CLASS: com.badlogic.gdx.net.Socket
import com.badlogic.gdx.net.Socket as _Socket
_Socket = _Socket
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
 
class Socket():
    """com.badlogic.gdx.net.Socket"""
 
    @staticmethod
    def _wrap(java_value: _Socket) -> 'Socket':
        return Socket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Socket):
        """
        Dynamic initializer for Socket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Socket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Socket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.net.ServerSocketHints
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.net.ServerSocketHints as _ServerSocketHints
_ServerSocketHints = _ServerSocketHints
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerSocketHints():
    """com.badlogic.gdx.net.ServerSocketHints"""
 
    @staticmethod
    def _wrap(java_value: _ServerSocketHints) -> 'ServerSocketHints':
        return ServerSocketHints(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerSocketHints):
        """
        Dynamic initializer for ServerSocketHints.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerSocketHints__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerSocketHints__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.net.ServerSocketHints()"""
        val = _ServerSocketHints()
        self.__wrapper = val

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.net.ServerSocketHints()"""
        val = _ServerSocketHints()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.net.HttpParametersUtils
from builtins import str
import com.badlogic.gdx.net.HttpParametersUtils as _HttpParametersUtils
_HttpParametersUtils = _HttpParametersUtils
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HttpParametersUtils():
    """com.badlogic.gdx.net.HttpParametersUtils"""
 
    @staticmethod
    def _wrap(java_value: _HttpParametersUtils) -> 'HttpParametersUtils':
        return HttpParametersUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpParametersUtils):
        """
        Dynamic initializer for HttpParametersUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpParametersUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpParametersUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def convertHttpParameters(arg0: 'Map') -> str:
        """public static java.lang.String com.badlogic.gdx.net.HttpParametersUtils.convertHttpParameters(java.util.Map<java.lang.String, java.lang.String>)"""
        return str._wrap(_HttpParametersUtils.convertHttpParameters(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.net.SocketHints
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.net.SocketHints as _SocketHints
_SocketHints = _SocketHints
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SocketHints():
    """com.badlogic.gdx.net.SocketHints"""
 
    @staticmethod
    def _wrap(java_value: _SocketHints) -> 'SocketHints':
        return SocketHints(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SocketHints):
        """
        Dynamic initializer for SocketHints.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SocketHints__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SocketHints__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.net.SocketHints()"""
        val = _SocketHints()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.net.SocketHints()"""
        val = _SocketHints()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.net.ServerSocket
import com.badlogic.gdx.net.ServerSocket as _ServerSocket
_ServerSocket = _ServerSocket
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as _Disposable
_Disposable = _Disposable
 
class ServerSocket():
    """com.badlogic.gdx.net.ServerSocket"""
 
    @staticmethod
    def _wrap(java_value: _ServerSocket) -> 'ServerSocket':
        return ServerSocket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerSocket):
        """
        Dynamic initializer for ServerSocket.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerSocket__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerSocket__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.net.HttpRequestHeader
import com.badlogic.gdx.net.HttpRequestHeader as _HttpRequestHeader
_HttpRequestHeader = _HttpRequestHeader
 
class HttpRequestHeader():
    """com.badlogic.gdx.net.HttpRequestHeader"""
 
    @staticmethod
    def _wrap(java_value: _HttpRequestHeader) -> 'HttpRequestHeader':
        return HttpRequestHeader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpRequestHeader):
        """
        Dynamic initializer for HttpRequestHeader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpRequestHeader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpRequestHeader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: com.badlogic.gdx.net.HttpStatus
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.net.HttpStatus as _HttpStatus
_HttpStatus = _HttpStatus
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HttpStatus():
    """com.badlogic.gdx.net.HttpStatus"""
 
    @staticmethod
    def _wrap(java_value: _HttpStatus) -> 'HttpStatus':
        return HttpStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpStatus):
        """
        Dynamic initializer for HttpStatus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpStatus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpStatus__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getStatusCode(self) -> int:
        """public int com.badlogic.gdx.net.HttpStatus.getStatusCode()"""
        return int._wrap(super(HttpStatus, self).getStatusCode())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.net.HttpStatus(int)"""
        val = _HttpStatus(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.net.NetJavaSocketImpl
from pyquantum_helper import import_once as _import_once
import java.net.Socket as Socket
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.lang.String as _string
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
import java.io.InputStream as InputStream
import com.badlogic.gdx.net.NetJavaSocketImpl as _NetJavaSocketImpl
_NetJavaSocketImpl = _NetJavaSocketImpl
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NetJavaSocketImpl():
    """com.badlogic.gdx.net.NetJavaSocketImpl"""
 
    @staticmethod
    def _wrap(java_value: _NetJavaSocketImpl) -> 'NetJavaSocketImpl':
        return NetJavaSocketImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NetJavaSocketImpl):
        """
        Dynamic initializer for NetJavaSocketImpl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NetJavaSocketImpl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NetJavaSocketImpl__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getRemoteAddress(self) -> str:
        """public java.lang.String com.badlogic.gdx.net.NetJavaSocketImpl.getRemoteAddress()"""
        return str._wrap(super(NetJavaSocketImpl, self).getRemoteAddress())

    @overload
    def __init__(self, arg0: 'Socket', arg1: 'SocketHints'):
        """public com.badlogic.gdx.net.NetJavaSocketImpl(java.net.Socket,com.badlogic.gdx.net.SocketHints)"""
        val = _NetJavaSocketImpl(arg0, arg1)
        self.__wrapper = val

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
    def dispose(self):
        """public void com.badlogic.gdx.net.NetJavaSocketImpl.dispose()"""
        super(NetJavaSocketImpl, self).dispose()

    @override
    @overload
    def getOutputStream(self) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.net.NetJavaSocketImpl.getOutputStream()"""
        return 'OutputStream'._wrap(super(NetJavaSocketImpl, self).getOutputStream())

    @override
    @overload
    def isConnected(self) -> bool:
        """public boolean com.badlogic.gdx.net.NetJavaSocketImpl.isConnected()"""
        return bool._wrap(super(NetJavaSocketImpl, self).isConnected())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getInputStream(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.net.NetJavaSocketImpl.getInputStream()"""
        return 'InputStream'._wrap(super(NetJavaSocketImpl, self).getInputStream())

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
    def __init__(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'SocketHints'):
        """public com.badlogic.gdx.net.NetJavaSocketImpl(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.SocketHints)"""
        val = _NetJavaSocketImpl(arg0, arg1, _int.valueOf(arg2), arg3)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.net.NetJavaImpl
from pyquantum_helper import import_once as _import_once
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.net.NetJavaImpl as _NetJavaImpl
_NetJavaImpl = _NetJavaImpl
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NetJavaImpl():
    """com.badlogic.gdx.net.NetJavaImpl"""
 
    @staticmethod
    def _wrap(java_value: _NetJavaImpl) -> 'NetJavaImpl':
        return NetJavaImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NetJavaImpl):
        """
        Dynamic initializer for NetJavaImpl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NetJavaImpl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NetJavaImpl__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def cancelHttpRequest(self, arg0: 'HttpRequest'):
        """public void com.badlogic.gdx.net.NetJavaImpl.cancelHttpRequest(com.badlogic.gdx.Net$HttpRequest)"""
        super(_NetJavaImpl, self).cancelHttpRequest(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.net.NetJavaImpl(int)"""
        val = _NetJavaImpl(_int.valueOf(arg0))
        self.__wrapper = val

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.net.NetJavaImpl()"""
        val = _NetJavaImpl()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.net.NetJavaImpl()"""
        val = _NetJavaImpl()
        self.__wrapper = val

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
    def sendHttpRequest(self, arg0: 'HttpRequest', arg1: 'HttpResponseListener'):
        """public void com.badlogic.gdx.net.NetJavaImpl.sendHttpRequest(com.badlogic.gdx.Net$HttpRequest,com.badlogic.gdx.Net$HttpResponseListener)"""
        super(_NetJavaImpl, self).sendHttpRequest(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.net.HttpRequestBuilder
from pyquantum_helper import import_once as _import_once
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.net.HttpRequestBuilder as _HttpRequestBuilder
_HttpRequestBuilder = _HttpRequestBuilder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.Net as _Net_HttpRequest
_HttpRequest = _Net_HttpRequest.HttpRequest
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.InputStream as InputStream
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HttpRequestBuilder():
    """com.badlogic.gdx.net.HttpRequestBuilder"""
 
    @staticmethod
    def _wrap(java_value: _HttpRequestBuilder) -> 'HttpRequestBuilder':
        return HttpRequestBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpRequestBuilder):
        """
        Dynamic initializer for HttpRequestBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpRequestBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpRequestBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def content(self, arg0: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.content(java.lang.String)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).content(arg0))

    @overload
    def timeout(self, arg0: int) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.timeout(int)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).timeout(_int.valueOf(arg0)))

    @overload
    def build(self) -> 'pygdx.Net$HttpRequest':
        """public com.badlogic.gdx.Net$HttpRequest com.badlogic.gdx.net.HttpRequestBuilder.build()"""
        return 'pygdx.Net$HttpRequest'._wrap(super(HttpRequestBuilder, self).build())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def url(self, arg0: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.url(java.lang.String)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).url(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def followRedirects(self, arg0: bool) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.followRedirects(boolean)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).followRedirects(_boolean.valueOf(arg0)))

    @overload
    def content(self, arg0: 'InputStream', arg1: int) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.content(java.io.InputStream,long)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).content(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def header(self, arg0: str, arg1: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.header(java.lang.String,java.lang.String)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).header(arg0, arg1))

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
    def __init__(self, ):
        """public com.badlogic.gdx.net.HttpRequestBuilder()"""
        val = _HttpRequestBuilder()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.net.HttpRequestBuilder()"""
        val = _HttpRequestBuilder()
        self.__wrapper = val

    @overload
    def jsonContent(self, arg0: object) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.jsonContent(java.lang.Object)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).jsonContent(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def includeCredentials(self, arg0: bool) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.includeCredentials(boolean)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).includeCredentials(_boolean.valueOf(arg0)))

    @overload
    def newRequest(self) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.newRequest()"""
        return 'HttpRequestBuilder'._wrap(super(HttpRequestBuilder, self).newRequest())

    @overload
    def basicAuthentication(self, arg0: str, arg1: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.basicAuthentication(java.lang.String,java.lang.String)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).basicAuthentication(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def method(self, arg0: str) -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.method(java.lang.String)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).method(arg0))

    @overload
    def formEncodedContent(self, arg0: 'Map') -> 'HttpRequestBuilder':
        """public com.badlogic.gdx.net.HttpRequestBuilder com.badlogic.gdx.net.HttpRequestBuilder.formEncodedContent(java.util.Map<java.lang.String, java.lang.String>)"""
        return 'HttpRequestBuilder'._wrap(super(_HttpRequestBuilder, self).formEncodedContent(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.net.NetJavaServerSocketImpl
from pyquantum_helper import import_once as _import_once
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.net.Socket as _Socket
_Socket = _Socket
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.Net as _Net_Protocol
_Protocol = _Net_Protocol.Protocol
import java.lang.String as _string
import com.badlogic.gdx.net.NetJavaServerSocketImpl as _NetJavaServerSocketImpl
_NetJavaServerSocketImpl = _NetJavaServerSocketImpl
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NetJavaServerSocketImpl():
    """com.badlogic.gdx.net.NetJavaServerSocketImpl"""
 
    @staticmethod
    def _wrap(java_value: _NetJavaServerSocketImpl) -> 'NetJavaServerSocketImpl':
        return NetJavaServerSocketImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NetJavaServerSocketImpl):
        """
        Dynamic initializer for NetJavaServerSocketImpl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NetJavaServerSocketImpl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NetJavaServerSocketImpl__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Protocol', arg1: int, arg2: 'ServerSocketHints'):
        """public com.badlogic.gdx.net.NetJavaServerSocketImpl(com.badlogic.gdx.Net$Protocol,int,com.badlogic.gdx.net.ServerSocketHints)"""
        val = _NetJavaServerSocketImpl(arg0, _int.valueOf(arg1), arg2)
        self.__wrapper = val

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.net.NetJavaServerSocketImpl.dispose()"""
        super(NetJavaServerSocketImpl, self).dispose()

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'ServerSocketHints'):
        """public com.badlogic.gdx.net.NetJavaServerSocketImpl(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.ServerSocketHints)"""
        val = _NetJavaServerSocketImpl(arg0, arg1, _int.valueOf(arg2), arg3)
        self.__wrapper = val

    @overload
    def accept(self, arg0: 'SocketHints') -> 'Socket':
        """public com.badlogic.gdx.net.Socket com.badlogic.gdx.net.NetJavaServerSocketImpl.accept(com.badlogic.gdx.net.SocketHints)"""
        return 'Socket'._wrap(super(_NetJavaServerSocketImpl, self).accept(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getProtocol(self) -> 'pygdx.Net$Protocol':
        """public com.badlogic.gdx.Net$Protocol com.badlogic.gdx.net.NetJavaServerSocketImpl.getProtocol()"""
        return 'pygdx.Net$Protocol'._wrap(super(NetJavaServerSocketImpl, self).getProtocol())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())
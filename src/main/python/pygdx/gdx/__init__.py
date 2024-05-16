from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ApplicationAdapter as _ApplicationAdapter
_ApplicationAdapter = _ApplicationAdapter
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ApplicationAdapter():
    """com.badlogic.gdx.ApplicationAdapter"""
 
    @staticmethod
    def _wrap(java_value: _ApplicationAdapter) -> 'ApplicationAdapter':
        return ApplicationAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ApplicationAdapter):
        """
        Dynamic initializer for ApplicationAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ApplicationAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ApplicationAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.ApplicationAdapter.resume()"""
        super(ApplicationAdapter, self).resume()

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.ApplicationAdapter.render()"""
        super(ApplicationAdapter, self).render()

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ApplicationAdapter()"""
        val = _ApplicationAdapter()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ApplicationAdapter.dispose()"""
        super(ApplicationAdapter, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def create(self):
        """public void com.badlogic.gdx.ApplicationAdapter.create()"""
        super(ApplicationAdapter, self).create()

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.ApplicationAdapter.pause()"""
        super(ApplicationAdapter, self).pause()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.ApplicationAdapter.resize(int,int)"""
        super(_ApplicationAdapter, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ApplicationAdapter()"""
        val = _ApplicationAdapter()
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.ApplicationAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ApplicationAdapter as _ApplicationAdapter
_ApplicationAdapter = _ApplicationAdapter
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ApplicationAdapter():
    """com.badlogic.gdx.ApplicationAdapter"""
 
    @staticmethod
    def _wrap(java_value: _ApplicationAdapter) -> 'ApplicationAdapter':
        return ApplicationAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ApplicationAdapter):
        """
        Dynamic initializer for ApplicationAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ApplicationAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ApplicationAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.ApplicationAdapter.resume()"""
        super(ApplicationAdapter, self).resume()

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.ApplicationAdapter.render()"""
        super(ApplicationAdapter, self).render()

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ApplicationAdapter()"""
        val = _ApplicationAdapter()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ApplicationAdapter.dispose()"""
        super(ApplicationAdapter, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def create(self):
        """public void com.badlogic.gdx.ApplicationAdapter.create()"""
        super(ApplicationAdapter, self).create()

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.ApplicationAdapter.pause()"""
        super(ApplicationAdapter, self).pause()

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.ApplicationAdapter.resize(int,int)"""
        super(_ApplicationAdapter, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ApplicationAdapter()"""
        val = _ApplicationAdapter()
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.ApplicationAdapter 
 
 
# CLASS: com.badlogic.gdx.Net$HttpRequest
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import com.badlogic.gdx.Net as _Net_HttpRequest
_HttpRequest = _Net_HttpRequest.HttpRequest
import java.lang.String as _String
_String = _String
import java.io.InputStream as _InputStream
_InputStream = _InputStream
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
 
class HttpRequest():
    """com.badlogic.gdx.Net.HttpRequest"""
 
    @staticmethod
    def _wrap(java_value: _HttpRequest) -> 'HttpRequest':
        return HttpRequest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpRequest):
        """
        Dynamic initializer for HttpRequest.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpRequest__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpRequest__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getContent(self) -> str:
        """public java.lang.String com.badlogic.gdx.Net$HttpRequest.getContent()"""
        return str._wrap(super(HttpRequest, self).getContent())

    @overload
    def setMethod(self, arg0: str):
        """public void com.badlogic.gdx.Net$HttpRequest.setMethod(java.lang.String)"""
        super(_HttpRequest, self).setMethod(arg0)

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.Net$HttpRequest(java.lang.String)"""
        val = _HttpRequest(arg0)
        self.__wrapper = val

    @overload
    def getFollowRedirects(self) -> bool:
        """public boolean com.badlogic.gdx.Net$HttpRequest.getFollowRedirects()"""
        return bool._wrap(super(HttpRequest, self).getFollowRedirects())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setContent(self, arg0: str):
        """public void com.badlogic.gdx.Net$HttpRequest.setContent(java.lang.String)"""
        super(_HttpRequest, self).setContent(arg0)

    @overload
    def getContentStream(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.Net$HttpRequest.getContentStream()"""
        return 'InputStream'._wrap(super(HttpRequest, self).getContentStream())

    @overload
    def getTimeOut(self) -> int:
        """public int com.badlogic.gdx.Net$HttpRequest.getTimeOut()"""
        return int._wrap(super(HttpRequest, self).getTimeOut())

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
        """public com.badlogic.gdx.Net$HttpRequest()"""
        val = _HttpRequest()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Net$HttpRequest()"""
        val = _HttpRequest()
        self.__wrapper = val

    @overload
    def setFollowRedirects(self, arg0: bool):
        """public void com.badlogic.gdx.Net$HttpRequest.setFollowRedirects(boolean) throws java.lang.IllegalArgumentException"""
        super(_HttpRequest, self).setFollowRedirects(_boolean.valueOf(arg0))

    @overload
    def getHeaders(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> com.badlogic.gdx.Net$HttpRequest.getHeaders()"""
        return 'Map'._wrap(super(HttpRequest, self).getHeaders())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setTimeOut(self, arg0: int):
        """public void com.badlogic.gdx.Net$HttpRequest.setTimeOut(int)"""
        super(_HttpRequest, self).setTimeOut(_int.valueOf(arg0))

    @overload
    def setUrl(self, arg0: str):
        """public void com.badlogic.gdx.Net$HttpRequest.setUrl(java.lang.String)"""
        super(_HttpRequest, self).setUrl(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.Net$HttpRequest.reset()"""
        super(HttpRequest, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getMethod(self) -> str:
        """public java.lang.String com.badlogic.gdx.Net$HttpRequest.getMethod()"""
        return str._wrap(super(HttpRequest, self).getMethod())

    @overload
    def getContentLength(self) -> int:
        """public long com.badlogic.gdx.Net$HttpRequest.getContentLength()"""
        return int._wrap(super(HttpRequest, self).getContentLength())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setHeader(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.Net$HttpRequest.setHeader(java.lang.String,java.lang.String)"""
        super(_HttpRequest, self).setHeader(arg0, arg1)

    @overload
    def getUrl(self) -> str:
        """public java.lang.String com.badlogic.gdx.Net$HttpRequest.getUrl()"""
        return str._wrap(super(HttpRequest, self).getUrl())

    @overload
    def setContent(self, arg0: 'InputStream', arg1: int):
        """public void com.badlogic.gdx.Net$HttpRequest.setContent(java.io.InputStream,long)"""
        super(_HttpRequest, self).setContent(arg0, _long.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getIncludeCredentials(self) -> bool:
        """public boolean com.badlogic.gdx.Net$HttpRequest.getIncludeCredentials()"""
        return bool._wrap(super(HttpRequest, self).getIncludeCredentials())

    @overload
    def setIncludeCredentials(self, arg0: bool):
        """public void com.badlogic.gdx.Net$HttpRequest.setIncludeCredentials(boolean)"""
        super(_HttpRequest, self).setIncludeCredentials(_boolean.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.Net$HttpResponse
import com.badlogic.gdx.Net as _Net_HttpResponse
_HttpResponse = _Net_HttpResponse.HttpResponse
from abc import abstractmethod, ABC
 
class HttpResponse():
    """com.badlogic.gdx.Net.HttpResponse"""
 
    @staticmethod
    def _wrap(java_value: _HttpResponse) -> 'HttpResponse':
        return HttpResponse(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpResponse):
        """
        Dynamic initializer for HttpResponse.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpResponse__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpResponse__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getResult(self, ):
        """public abstract byte[] com.badlogic.gdx.Net$HttpResponse.getResult()"""
        pass

    @abstractmethod
    def getResultAsStream(self, ):
        """public abstract java.io.InputStream com.badlogic.gdx.Net$HttpResponse.getResultAsStream()"""
        pass

    @abstractmethod
    def getHeaders(self, ):
        """public abstract java.util.Map<java.lang.String, java.util.List<java.lang.String>> com.badlogic.gdx.Net$HttpResponse.getHeaders()"""
        pass

    @abstractmethod
    def getHeader(self, arg0: str):
        """public abstract java.lang.String com.badlogic.gdx.Net$HttpResponse.getHeader(java.lang.String)"""
        pass

    @abstractmethod
    def getStatus(self, ):
        """public abstract com.badlogic.gdx.net.HttpStatus com.badlogic.gdx.Net$HttpResponse.getStatus()"""
        pass

    @abstractmethod
    def getResultAsString(self, ):
        """public abstract java.lang.String com.badlogic.gdx.Net$HttpResponse.getResultAsString()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Net$HttpResponseListener
import com.badlogic.gdx.Net as _Net_HttpResponseListener
_HttpResponseListener = _Net_HttpResponseListener.HttpResponseListener
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class HttpResponseListener():
    """com.badlogic.gdx.Net.HttpResponseListener"""
 
    @staticmethod
    def _wrap(java_value: _HttpResponseListener) -> 'HttpResponseListener':
        return HttpResponseListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpResponseListener):
        """
        Dynamic initializer for HttpResponseListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpResponseListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpResponseListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def cancelled(self, ):
        """public abstract void com.badlogic.gdx.Net$HttpResponseListener.cancelled()"""
        pass

    @abstractmethod
    def failed(self, arg0: 'Throwable'):
        """public abstract void com.badlogic.gdx.Net$HttpResponseListener.failed(java.lang.Throwable)"""
        pass

    @abstractmethod
    def handleHttpResponse(self, arg0: 'HttpResponse'):
        """public abstract void com.badlogic.gdx.Net$HttpResponseListener.handleHttpResponse(com.badlogic.gdx.Net$HttpResponse)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Input$Buttons
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.Input as _Input_Buttons
_Buttons = _Input_Buttons.Buttons
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buttons():
    """com.badlogic.gdx.Input.Buttons"""
 
    @staticmethod
    def _wrap(java_value: _Buttons) -> 'Buttons':
        return Buttons(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buttons):
        """
        Dynamic initializer for Buttons.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buttons__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buttons__wrapper":
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
        """public com.badlogic.gdx.Input$Buttons()"""
        val = _Buttons()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.Input$Buttons()"""
        val = _Buttons()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.Graphics$GraphicsType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.Graphics as _Graphics_GraphicsType
_GraphicsType = _Graphics_GraphicsType.GraphicsType
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GraphicsType():
    """com.badlogic.gdx.Graphics.GraphicsType"""
 
    @staticmethod
    def _wrap(java_value: _GraphicsType) -> 'GraphicsType':
        return GraphicsType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GraphicsType):
        """
        Dynamic initializer for GraphicsType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GraphicsType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GraphicsType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'GraphicsType':
        """public static com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.Graphics$GraphicsType.valueOf(java.lang.String)"""
        return GraphicsType._wrap(_GraphicsType.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['GraphicsType']:
        """public static com.badlogic.gdx.Graphics$GraphicsType[] com.badlogic.gdx.Graphics$GraphicsType.values()"""
        return List[GraphicsType]._wrap(_GraphicsType.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.Audio
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.Audio as _Audio
_Audio = _Audio
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from abc import abstractmethod, ABC
 
class Audio():
    """com.badlogic.gdx.Audio"""
 
    @staticmethod
    def _wrap(java_value: _Audio) -> 'Audio':
        return Audio(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Audio):
        """
        Dynamic initializer for Audio.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Audio__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Audio__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def newMusic(self, arg0: 'FileHandle'):
        """public abstract com.badlogic.gdx.audio.Music com.badlogic.gdx.Audio.newMusic(com.badlogic.gdx.files.FileHandle)"""
        pass

    @abstractmethod
    def getAvailableOutputDevices(self, ):
        """public abstract java.lang.String[] com.badlogic.gdx.Audio.getAvailableOutputDevices()"""
        pass

    @abstractmethod
    def newAudioDevice(self, arg0: int, arg1: bool):
        """public abstract com.badlogic.gdx.audio.AudioDevice com.badlogic.gdx.Audio.newAudioDevice(int,boolean)"""
        pass

    @abstractmethod
    def switchOutputDevice(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Audio.switchOutputDevice(java.lang.String)"""
        pass

    @abstractmethod
    def newSound(self, arg0: 'FileHandle'):
        """public abstract com.badlogic.gdx.audio.Sound com.badlogic.gdx.Audio.newSound(com.badlogic.gdx.files.FileHandle)"""
        pass

    @abstractmethod
    def newAudioRecorder(self, arg0: int, arg1: bool):
        """public abstract com.badlogic.gdx.audio.AudioRecorder com.badlogic.gdx.Audio.newAudioRecorder(int,boolean)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Input$VibrationType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import com.badlogic.gdx.Input as _Input_VibrationType
_VibrationType = _Input_VibrationType.VibrationType
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VibrationType():
    """com.badlogic.gdx.Input.VibrationType"""
 
    @staticmethod
    def _wrap(java_value: _VibrationType) -> 'VibrationType':
        return VibrationType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VibrationType):
        """
        Dynamic initializer for VibrationType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VibrationType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VibrationType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['VibrationType']:
        """public static com.badlogic.gdx.Input$VibrationType[] com.badlogic.gdx.Input$VibrationType.values()"""
        return List[VibrationType]._wrap(_VibrationType.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'VibrationType':
        """public static com.badlogic.gdx.Input$VibrationType com.badlogic.gdx.Input$VibrationType.valueOf(java.lang.String)"""
        return VibrationType._wrap(_VibrationType.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.Input$Keys
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.Input as _Input_Keys
_Keys = _Input_Keys.Keys
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Keys():
    """com.badlogic.gdx.Input.Keys"""
 
    @staticmethod
    def _wrap(java_value: _Keys) -> 'Keys':
        return Keys(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Keys):
        """
        Dynamic initializer for Keys.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Keys__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Keys__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> int:
        """public static int com.badlogic.gdx.Input$Keys.valueOf(java.lang.String)"""
        return int._wrap(_Keys.valueOf(arg0))

    @staticmethod
    @overload
    def toString(arg0: int) -> str:
        """public static java.lang.String com.badlogic.gdx.Input$Keys.toString(int)"""
        return str._wrap(_Keys.toString(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Input$Keys()"""
        val = _Keys()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.Input$Keys()"""
        val = _Keys()
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
 
 
# CLASS: com.badlogic.gdx.InputMultiplexer
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.InputMultiplexer as _InputMultiplexer
_InputMultiplexer = _InputMultiplexer
from builtins import str
import java.lang.Character as _char
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.utils.SnapshotArray as _SnapshotArray
_SnapshotArray = _SnapshotArray
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InputMultiplexer():
    """com.badlogic.gdx.InputMultiplexer"""
 
    @staticmethod
    def _wrap(java_value: _InputMultiplexer) -> 'InputMultiplexer':
        return InputMultiplexer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InputMultiplexer):
        """
        Dynamic initializer for InputMultiplexer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InputMultiplexer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InputMultiplexer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.keyUp(int)"""
        return bool._wrap(super(_InputMultiplexer, self).keyUp(_int.valueOf(arg0)))

    @overload
    def __init__(self, *arg0: 'InputProcessor'):
        """public com.badlogic.gdx.InputMultiplexer(com.badlogic.gdx.InputProcessor...)"""
        val = _InputMultiplexer(arg0)
        self.__wrapper = val

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.keyDown(int)"""
        return bool._wrap(super(_InputMultiplexer, self).keyDown(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.InputMultiplexer()"""
        val = _InputMultiplexer()
        self.__wrapper = val

    @overload
    def setProcessors(self, arg0: 'Array'):
        """public void com.badlogic.gdx.InputMultiplexer.setProcessors(com.badlogic.gdx.utils.Array<com.badlogic.gdx.InputProcessor>)"""
        super(_InputMultiplexer, self).setProcessors(arg0)

    @overload
    def removeProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.InputMultiplexer.removeProcessor(com.badlogic.gdx.InputProcessor)"""
        super(_InputMultiplexer, self).removeProcessor(arg0)

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
    def setProcessors(self, *arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.InputMultiplexer.setProcessors(com.badlogic.gdx.InputProcessor...)"""
        super(_InputMultiplexer, self).setProcessors(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.InputMultiplexer()"""
        val = _InputMultiplexer()
        self.__wrapper = val

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.mouseMoved(int,int)"""
        return bool._wrap(super(_InputMultiplexer, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addProcessor(self, arg0: int, arg1: 'InputProcessor'):
        """public void com.badlogic.gdx.InputMultiplexer.addProcessor(int,com.badlogic.gdx.InputProcessor)"""
        super(_InputMultiplexer, self).addProcessor(_int.valueOf(arg0), arg1)

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.touchDragged(int,int,int)"""
        return bool._wrap(super(_InputMultiplexer, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def removeProcessor(self, arg0: int):
        """public void com.badlogic.gdx.InputMultiplexer.removeProcessor(int)"""
        super(_InputMultiplexer, self).removeProcessor(_int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def addProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.InputMultiplexer.addProcessor(com.badlogic.gdx.InputProcessor)"""
        super(_InputMultiplexer, self).addProcessor(arg0)

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.scrolled(float,float)"""
        return bool._wrap(super(_InputMultiplexer, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.keyTyped(char)"""
        return bool._wrap(super(_InputMultiplexer, self).keyTyped(_char.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.InputMultiplexer.size()"""
        return int._wrap(super(InputMultiplexer, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.InputMultiplexer.clear()"""
        super(InputMultiplexer, self).clear()

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.touchUp(int,int,int,int)"""
        return bool._wrap(super(_InputMultiplexer, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_InputMultiplexer, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getProcessors(self) -> 'utils.SnapshotArray':
        """public com.badlogic.gdx.utils.SnapshotArray<com.badlogic.gdx.InputProcessor> com.badlogic.gdx.InputMultiplexer.getProcessors()"""
        return 'utils.SnapshotArray'._wrap(super(InputMultiplexer, self).getProcessors())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputMultiplexer.touchDown(int,int,int,int)"""
        return bool._wrap(super(_InputMultiplexer, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.Graphics
from pyquantum_helper import import_once as _import_once
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.Graphics as _Graphics
_Graphics = _Graphics
 
class Graphics():
    """com.badlogic.gdx.Graphics"""
 
    @staticmethod
    def _wrap(java_value: _Graphics) -> 'Graphics':
        return Graphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Graphics):
        """
        Dynamic initializer for Graphics.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Graphics__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Graphics__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def newCursor(self, arg0: 'Pixmap', arg1: int, arg2: int):
        """public abstract com.badlogic.gdx.graphics.Cursor com.badlogic.gdx.Graphics.newCursor(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        pass

    @abstractmethod
    def getSafeInsetLeft(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetLeft()"""
        pass

    @abstractmethod
    def setVSync(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setVSync(boolean)"""
        pass

    @abstractmethod
    def getSafeInsetTop(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetTop()"""
        pass

    @abstractmethod
    def getMonitor(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.Graphics.getMonitor()"""
        pass

    @abstractmethod
    def getDisplayMode(self, ):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.Graphics.getDisplayMode()"""
        pass

    @abstractmethod
    def getMonitors(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor[] com.badlogic.gdx.Graphics.getMonitors()"""
        pass

    @abstractmethod
    def setGL20(self, arg0: 'GL20'):
        """public abstract void com.badlogic.gdx.Graphics.setGL20(com.badlogic.gdx.graphics.GL20)"""
        pass

    @abstractmethod
    def setGL31(self, arg0: 'GL31'):
        """public abstract void com.badlogic.gdx.Graphics.setGL31(com.badlogic.gdx.graphics.GL31)"""
        pass

    @abstractmethod
    def getPpiX(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpiX()"""
        pass

    @abstractmethod
    def supportsExtension(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Graphics.supportsExtension(java.lang.String)"""
        pass

    @abstractmethod
    def isGL32Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL32Available()"""
        pass

    @abstractmethod
    def getBackBufferHeight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getBackBufferHeight()"""
        pass

    @abstractmethod
    def getPpcY(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpcY()"""
        pass

    @abstractmethod
    def getDisplayMode(self, arg0: 'Monitor'):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.Graphics.getDisplayMode(com.badlogic.gdx.Graphics$Monitor)"""
        pass

    @abstractmethod
    def getFrameId(self, ):
        """public abstract long com.badlogic.gdx.Graphics.getFrameId()"""
        pass

    @abstractmethod
    def getPpcX(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpcX()"""
        pass

    @abstractmethod
    def getSafeInsetBottom(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetBottom()"""
        pass

    @abstractmethod
    def setGL30(self, arg0: 'GL30'):
        """public abstract void com.badlogic.gdx.Graphics.setGL30(com.badlogic.gdx.graphics.GL30)"""
        pass

    @abstractmethod
    def getDisplayModes(self, ):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.Graphics.getDisplayModes()"""
        pass

    @abstractmethod
    def setTitle(self, arg0: str):
        """public abstract void com.badlogic.gdx.Graphics.setTitle(java.lang.String)"""
        pass

    @abstractmethod
    def supportsDisplayModeChange(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.supportsDisplayModeChange()"""
        pass

    @abstractmethod
    def getGL30(self, ):
        """public abstract com.badlogic.gdx.graphics.GL30 com.badlogic.gdx.Graphics.getGL30()"""
        pass

    @abstractmethod
    def setGL32(self, arg0: 'GL32'):
        """public abstract void com.badlogic.gdx.Graphics.setGL32(com.badlogic.gdx.graphics.GL32)"""
        pass

    @abstractmethod
    def setWindowedMode(self, arg0: int, arg1: int):
        """public abstract boolean com.badlogic.gdx.Graphics.setWindowedMode(int,int)"""
        pass

    @abstractmethod
    def isFullscreen(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isFullscreen()"""
        pass

    @abstractmethod
    def getGL32(self, ):
        """public abstract com.badlogic.gdx.graphics.GL32 com.badlogic.gdx.Graphics.getGL32()"""
        pass

    @abstractmethod
    def isGL31Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL31Available()"""
        pass

    @abstractmethod
    def getGLVersion(self, ):
        """public abstract com.badlogic.gdx.graphics.glutils.GLVersion com.badlogic.gdx.Graphics.getGLVersion()"""
        pass

    @abstractmethod
    def getPpiY(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpiY()"""
        pass

    @abstractmethod
    def getBackBufferScale(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getBackBufferScale()"""
        pass

    @abstractmethod
    def getBackBufferWidth(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getBackBufferWidth()"""
        pass

    @abstractmethod
    def getSafeInsetRight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetRight()"""
        pass

    @abstractmethod
    def getDensity(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getDensity()"""
        pass

    @abstractmethod
    def getBufferFormat(self, ):
        """public abstract com.badlogic.gdx.Graphics$BufferFormat com.badlogic.gdx.Graphics.getBufferFormat()"""
        pass

    @abstractmethod
    def isContinuousRendering(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isContinuousRendering()"""
        pass

    @abstractmethod
    def setContinuousRendering(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setContinuousRendering(boolean)"""
        pass

    @abstractmethod
    def getDeltaTime(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getDeltaTime()"""
        pass

    @abstractmethod
    def setFullscreenMode(self, arg0: 'DisplayMode'):
        """public abstract boolean com.badlogic.gdx.Graphics.setFullscreenMode(com.badlogic.gdx.Graphics$DisplayMode)"""
        pass

    @abstractmethod
    def setCursor(self, arg0: 'Cursor'):
        """public abstract void com.badlogic.gdx.Graphics.setCursor(com.badlogic.gdx.graphics.Cursor)"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.Graphics.getType()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getWidth()"""
        pass

    @abstractmethod
    def setResizable(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setResizable(boolean)"""
        pass

    @abstractmethod
    def setForegroundFPS(self, arg0: int):
        """public abstract void com.badlogic.gdx.Graphics.setForegroundFPS(int)"""
        pass

    @abstractmethod
    def requestRendering(self, ):
        """public abstract void com.badlogic.gdx.Graphics.requestRendering()"""
        pass

    @abstractmethod
    def getDisplayModes(self, arg0: 'Monitor'):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.Graphics.getDisplayModes(com.badlogic.gdx.Graphics$Monitor)"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getHeight()"""
        pass

    @abstractmethod
    def getFramesPerSecond(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getFramesPerSecond()"""
        pass

    @abstractmethod
    def isGL30Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL30Available()"""
        pass

    @abstractmethod
    def getGL31(self, ):
        """public abstract com.badlogic.gdx.graphics.GL31 com.badlogic.gdx.Graphics.getGL31()"""
        pass

    @abstractmethod
    def setUndecorated(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setUndecorated(boolean)"""
        pass

    @abstractmethod
    def setSystemCursor(self, arg0: 'SystemCursor'):
        """public abstract void com.badlogic.gdx.Graphics.setSystemCursor(com.badlogic.gdx.graphics.Cursor$SystemCursor)"""
        pass

    @abstractmethod
    def getPrimaryMonitor(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.Graphics.getPrimaryMonitor()"""
        pass

    @abstractmethod
    def getRawDeltaTime(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getRawDeltaTime()"""
        pass

    @abstractmethod
    def getGL20(self, ):
        """public abstract com.badlogic.gdx.graphics.GL20 com.badlogic.gdx.Graphics.getGL20()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Input$OnscreenKeyboardType
import com.badlogic.gdx.Input as _Input_OnscreenKeyboardType
_OnscreenKeyboardType = _Input_OnscreenKeyboardType.OnscreenKeyboardType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OnscreenKeyboardType():
    """com.badlogic.gdx.Input.OnscreenKeyboardType"""
 
    @staticmethod
    def _wrap(java_value: _OnscreenKeyboardType) -> 'OnscreenKeyboardType':
        return OnscreenKeyboardType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OnscreenKeyboardType):
        """
        Dynamic initializer for OnscreenKeyboardType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OnscreenKeyboardType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OnscreenKeyboardType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['OnscreenKeyboardType']:
        """public static com.badlogic.gdx.Input$OnscreenKeyboardType[] com.badlogic.gdx.Input$OnscreenKeyboardType.values()"""
        return List[OnscreenKeyboardType]._wrap(_OnscreenKeyboardType.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'OnscreenKeyboardType':
        """public static com.badlogic.gdx.Input$OnscreenKeyboardType com.badlogic.gdx.Input$OnscreenKeyboardType.valueOf(java.lang.String)"""
        return OnscreenKeyboardType._wrap(_OnscreenKeyboardType.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.Screen
import com.badlogic.gdx.Screen as _Screen
_Screen = _Screen
from abc import abstractmethod, ABC
 
class Screen():
    """com.badlogic.gdx.Screen"""
 
    @staticmethod
    def _wrap(java_value: _Screen) -> 'Screen':
        return Screen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Screen):
        """
        Dynamic initializer for Screen.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Screen__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Screen__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.Screen.pause()"""
        pass

    @abstractmethod
    def resume(self, ):
        """public abstract void com.badlogic.gdx.Screen.resume()"""
        pass

    @abstractmethod
    def render(self, arg0: float):
        """public abstract void com.badlogic.gdx.Screen.render(float)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.Screen.dispose()"""
        pass

    @abstractmethod
    def resize(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.Screen.resize(int,int)"""
        pass

    @abstractmethod
    def show(self, ):
        """public abstract void com.badlogic.gdx.Screen.show()"""
        pass

    @abstractmethod
    def hide(self, ):
        """public abstract void com.badlogic.gdx.Screen.hide()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Graphics$Monitor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.Graphics as _Graphics_Monitor
_Monitor = _Graphics_Monitor.Monitor
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Monitor():
    """com.badlogic.gdx.Graphics.Monitor"""
 
    @staticmethod
    def _wrap(java_value: _Monitor) -> 'Monitor':
        return Monitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Monitor):
        """
        Dynamic initializer for Monitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Monitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Monitor__wrapper":
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
 
 
# CLASS: com.badlogic.gdx.Version
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.Version as _Version
_Version = _Version
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Version():
    """com.badlogic.gdx.Version"""
 
    @staticmethod
    def _wrap(java_value: _Version) -> 'Version':
        return Version(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Version):
        """
        Dynamic initializer for Version.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Version__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Version__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.Version()"""
        val = _Version()
        self.__wrapper = val

    @staticmethod
    @overload
    def isLowerEqual(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.Version.isLowerEqual(int,int,int)"""
        return bool._wrap(_Version.isLowerEqual(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @staticmethod
    @overload
    def isHigher(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.Version.isHigher(int,int,int)"""
        return bool._wrap(_Version.isHigher(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def isLower(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.Version.isLower(int,int,int)"""
        return bool._wrap(_Version.isLower(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isHigherEqual(arg0: int, arg1: int, arg2: int) -> bool:
        """public static boolean com.badlogic.gdx.Version.isHigherEqual(int,int,int)"""
        return bool._wrap(_Version.isHigherEqual(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Version()"""
        val = _Version()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.InputProcessor
import com.badlogic.gdx.InputProcessor as _InputProcessor
_InputProcessor = _InputProcessor
from abc import abstractmethod, ABC
 
class InputProcessor():
    """com.badlogic.gdx.InputProcessor"""
 
    @staticmethod
    def _wrap(java_value: _InputProcessor) -> 'InputProcessor':
        return InputProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InputProcessor):
        """
        Dynamic initializer for InputProcessor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InputProcessor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InputProcessor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def keyTyped(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.InputProcessor.keyTyped(char)"""
        pass

    @abstractmethod
    def touchDragged(self, arg0: int, arg1: int, arg2: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchDragged(int,int,int)"""
        pass

    @abstractmethod
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchCancelled(int,int,int,int)"""
        pass

    @abstractmethod
    def keyDown(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.keyDown(int)"""
        pass

    @abstractmethod
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchDown(int,int,int,int)"""
        pass

    @abstractmethod
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.touchUp(int,int,int,int)"""
        pass

    @abstractmethod
    def mouseMoved(self, arg0: int, arg1: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.mouseMoved(int,int)"""
        pass

    @abstractmethod
    def keyUp(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.InputProcessor.keyUp(int)"""
        pass

    @abstractmethod
    def scrolled(self, arg0: float, arg1: float):
        """public abstract boolean com.badlogic.gdx.InputProcessor.scrolled(float,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Gdx
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.Gdx as _Gdx
_Gdx = _Gdx
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Gdx():
    """com.badlogic.gdx.Gdx"""
 
    @staticmethod
    def _wrap(java_value: _Gdx) -> 'Gdx':
        return Gdx(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Gdx):
        """
        Dynamic initializer for Gdx.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Gdx__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Gdx__wrapper":
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
    def __init__(self):
        """public com.badlogic.gdx.Gdx()"""
        val = _Gdx()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Gdx()"""
        val = _Gdx()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.Input$Orientation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import com.badlogic.gdx.Input as _Input_Orientation
_Orientation = _Input_Orientation.Orientation
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Orientation():
    """com.badlogic.gdx.Input.Orientation"""
 
    @staticmethod
    def _wrap(java_value: _Orientation) -> 'Orientation':
        return Orientation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Orientation):
        """
        Dynamic initializer for Orientation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Orientation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Orientation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['Orientation']:
        """public static com.badlogic.gdx.Input$Orientation[] com.badlogic.gdx.Input$Orientation.values()"""
        return List[Orientation]._wrap(_Orientation.values())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Orientation':
        """public static com.badlogic.gdx.Input$Orientation com.badlogic.gdx.Input$Orientation.valueOf(java.lang.String)"""
        return Orientation._wrap(_Orientation.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Application
import java.lang.Runnable as Runnable
import com.badlogic.gdx.Application as _Application
_Application = _Application
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class Application():
    """com.badlogic.gdx.Application"""
 
    @staticmethod
    def _wrap(java_value: _Application) -> 'Application':
        return Application(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Application):
        """
        Dynamic initializer for Application.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Application__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Application__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getNativeHeap(self, ):
        """public abstract long com.badlogic.gdx.Application.getNativeHeap()"""
        pass

    @abstractmethod
    def getJavaHeap(self, ):
        """public abstract long com.badlogic.gdx.Application.getJavaHeap()"""
        pass

    @abstractmethod
    def getInput(self, ):
        """public abstract com.badlogic.gdx.Input com.badlogic.gdx.Application.getInput()"""
        pass

    @abstractmethod
    def setLogLevel(self, arg0: int):
        """public abstract void com.badlogic.gdx.Application.setLogLevel(int)"""
        pass

    @abstractmethod
    def getPreferences(self, arg0: str):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Application.getPreferences(java.lang.String)"""
        pass

    @abstractmethod
    def getLogLevel(self, ):
        """public abstract int com.badlogic.gdx.Application.getLogLevel()"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.Application.log(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.Application.error(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def getVersion(self, ):
        """public abstract int com.badlogic.gdx.Application.getVersion()"""
        pass

    @abstractmethod
    def getApplicationLogger(self, ):
        """public abstract com.badlogic.gdx.ApplicationLogger com.badlogic.gdx.Application.getApplicationLogger()"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.Application.debug(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def getNet(self, ):
        """public abstract com.badlogic.gdx.Net com.badlogic.gdx.Application.getNet()"""
        pass

    @abstractmethod
    def removeLifecycleListener(self, arg0: 'LifecycleListener'):
        """public abstract void com.badlogic.gdx.Application.removeLifecycleListener(com.badlogic.gdx.LifecycleListener)"""
        pass

    @abstractmethod
    def getAudio(self, ):
        """public abstract com.badlogic.gdx.Audio com.badlogic.gdx.Application.getAudio()"""
        pass

    @abstractmethod
    def getApplicationListener(self, ):
        """public abstract com.badlogic.gdx.ApplicationListener com.badlogic.gdx.Application.getApplicationListener()"""
        pass

    @abstractmethod
    def getFiles(self, ):
        """public abstract com.badlogic.gdx.Files com.badlogic.gdx.Application.getFiles()"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.Application.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def getClipboard(self, ):
        """public abstract com.badlogic.gdx.utils.Clipboard com.badlogic.gdx.Application.getClipboard()"""
        pass

    @abstractmethod
    def postRunnable(self, arg0: 'Runnable'):
        """public abstract void com.badlogic.gdx.Application.postRunnable(java.lang.Runnable)"""
        pass

    @abstractmethod
    def getGraphics(self, ):
        """public abstract com.badlogic.gdx.Graphics com.badlogic.gdx.Application.getGraphics()"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.Application.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.Application$ApplicationType com.badlogic.gdx.Application.getType()"""
        pass

    @abstractmethod
    def setApplicationLogger(self, arg0: 'ApplicationLogger'):
        """public abstract void com.badlogic.gdx.Application.setApplicationLogger(com.badlogic.gdx.ApplicationLogger)"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.Application.log(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def exit(self, ):
        """public abstract void com.badlogic.gdx.Application.exit()"""
        pass

    @abstractmethod
    def addLifecycleListener(self, arg0: 'LifecycleListener'):
        """public abstract void com.badlogic.gdx.Application.addLifecycleListener(com.badlogic.gdx.LifecycleListener)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Graphics$DisplayMode
import com.badlogic.gdx.Graphics as _Graphics_DisplayMode
_DisplayMode = _Graphics_DisplayMode.DisplayMode
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
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DisplayMode():
    """com.badlogic.gdx.Graphics.DisplayMode"""
 
    @staticmethod
    def _wrap(java_value: _DisplayMode) -> 'DisplayMode':
        return DisplayMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DisplayMode):
        """
        Dynamic initializer for DisplayMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DisplayMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DisplayMode__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.Graphics$DisplayMode.toString()"""
        return str._wrap(super(DisplayMode, self).toString())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.Net
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.Net as _Net
_Net = _Net
try:
    from pygdx import net
except ImportError:
    net = _import_once("pygdx.net")

from abc import abstractmethod, ABC
 
class Net():
    """com.badlogic.gdx.Net"""
 
    @staticmethod
    def _wrap(java_value: _Net) -> 'Net':
        return Net(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Net):
        """
        Dynamic initializer for Net.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Net__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Net__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def cancelHttpRequest(self, arg0: 'HttpRequest'):
        """public abstract void com.badlogic.gdx.Net.cancelHttpRequest(com.badlogic.gdx.Net$HttpRequest)"""
        pass

    @abstractmethod
    def openURI(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Net.openURI(java.lang.String)"""
        pass

    @abstractmethod
    def sendHttpRequest(self, arg0: 'HttpRequest', arg1: 'HttpResponseListener'):
        """public abstract void com.badlogic.gdx.Net.sendHttpRequest(com.badlogic.gdx.Net$HttpRequest,com.badlogic.gdx.Net$HttpResponseListener)"""
        pass

    @abstractmethod
    def newServerSocket(self, arg0: 'Protocol', arg1: int, arg2: 'ServerSocketHints'):
        """public abstract com.badlogic.gdx.net.ServerSocket com.badlogic.gdx.Net.newServerSocket(com.badlogic.gdx.Net$Protocol,int,com.badlogic.gdx.net.ServerSocketHints)"""
        pass

    @abstractmethod
    def newClientSocket(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'SocketHints'):
        """public abstract com.badlogic.gdx.net.Socket com.badlogic.gdx.Net.newClientSocket(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.SocketHints)"""
        pass

    @abstractmethod
    def newServerSocket(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'ServerSocketHints'):
        """public abstract com.badlogic.gdx.net.ServerSocket com.badlogic.gdx.Net.newServerSocket(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.ServerSocketHints)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Files
import com.badlogic.gdx.Files as _Files
_Files = _Files
from abc import abstractmethod, ABC
 
class Files():
    """com.badlogic.gdx.Files"""
 
    @staticmethod
    def _wrap(java_value: _Files) -> 'Files':
        return Files(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Files):
        """
        Dynamic initializer for Files.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Files__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Files__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getLocalStoragePath(self, ):
        """public abstract java.lang.String com.badlogic.gdx.Files.getLocalStoragePath()"""
        pass

    @abstractmethod
    def local(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.local(java.lang.String)"""
        pass

    @abstractmethod
    def getExternalStoragePath(self, ):
        """public abstract java.lang.String com.badlogic.gdx.Files.getExternalStoragePath()"""
        pass

    @abstractmethod
    def external(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.external(java.lang.String)"""
        pass

    @abstractmethod
    def isExternalStorageAvailable(self, ):
        """public abstract boolean com.badlogic.gdx.Files.isExternalStorageAvailable()"""
        pass

    @abstractmethod
    def getFileHandle(self, arg0: str, arg1: 'FileType'):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.getFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        pass

    @abstractmethod
    def isLocalStorageAvailable(self, ):
        """public abstract boolean com.badlogic.gdx.Files.isLocalStorageAvailable()"""
        pass

    @abstractmethod
    def internal(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.internal(java.lang.String)"""
        pass

    @abstractmethod
    def classpath(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.classpath(java.lang.String)"""
        pass

    @abstractmethod
    def absolute(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.Files.absolute(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.AbstractInput
from builtins import str
import com.badlogic.gdx.Input as _Input
_Input = _Input
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.AbstractInput as _AbstractInput
_AbstractInput = _AbstractInput
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractInput():
    """com.badlogic.gdx.AbstractInput"""
 
    @staticmethod
    def _wrap(java_value: _AbstractInput) -> 'AbstractInput':
        return AbstractInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractInput):
        """
        Dynamic initializer for AbstractInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getRotation(self, ):
        """public abstract int com.badlogic.gdx.Input.getRotation()"""
        pass

    @abstractmethod
    def getNativeOrientation(self, ):
        """public abstract com.badlogic.gdx.Input$Orientation com.badlogic.gdx.Input.getNativeOrientation()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public abstract void com.badlogic.gdx.Input.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.AbstractInput()"""
        val = _AbstractInput()
        self.__wrapper = val

    @override
    @overload
    def setCatchKey(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.AbstractInput.setCatchKey(int,boolean)"""
        super(_AbstractInput, self).setCatchKey(_int.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getDeltaY(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getDeltaY(int)"""
        pass

    @abstractmethod
    def getMaxPointers(self, ):
        """public abstract int com.badlogic.gdx.Input.getMaxPointers()"""
        pass

    @abstractmethod
    def isTouched(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isTouched(int)"""
        pass

    @overload
    def __init__(self):
        """public com.badlogic.gdx.AbstractInput()"""
        val = _AbstractInput()
        self.__wrapper = val

    @abstractmethod
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public abstract void com.badlogic.gdx.Input.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def isButtonJustPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isButtonJustPressed(int)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @abstractmethod
    def getY(self, ):
        """public abstract int com.badlogic.gdx.Input.getY()"""
        pass

    @abstractmethod
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public abstract void com.badlogic.gdx.Input.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def getRoll(self, ):
        """public abstract float com.badlogic.gdx.Input.getRoll()"""
        pass

    @abstractmethod
    def getDeltaY(self, ):
        """public abstract int com.badlogic.gdx.Input.getDeltaY()"""
        pass

    @override
    @overload
    def isCatchMenuKey(self) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isCatchMenuKey()"""
        return bool._wrap(super(AbstractInput, self).isCatchMenuKey())

    @abstractmethod
    def getPressure(self, arg0: int):
        """public abstract float com.badlogic.gdx.Input.getPressure(int)"""
        pass

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

    @abstractmethod
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public abstract void com.badlogic.gdx.Input.vibrate(int,int,boolean)"""
        pass

    @abstractmethod
    def getX(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getX(int)"""
        pass

    @abstractmethod
    def isCursorCatched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isCursorCatched()"""
        pass

    @abstractmethod
    def isPeripheralAvailable(self, arg0: 'Peripheral'):
        """public abstract boolean com.badlogic.gdx.Input.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        pass

    @abstractmethod
    def getRotationMatrix(self, arg0: 'float'):
        """public abstract void com.badlogic.gdx.Input.getRotationMatrix(float[])"""
        pass

    @abstractmethod
    def getGyroscopeY(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeY()"""
        pass

    @abstractmethod
    def getGyroscopeX(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeX()"""
        pass

    @overload
    def isKeyPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isKeyPressed(int)"""
        return bool._wrap(super(_AbstractInput, self).isKeyPressed(_int.valueOf(arg0)))

    @abstractmethod
    def vibrate(self, arg0: 'VibrationType'):
        """public abstract void com.badlogic.gdx.Input.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        pass

    @overload
    def isCatchKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isCatchKey(int)"""
        return bool._wrap(super(_AbstractInput, self).isCatchKey(_int.valueOf(arg0)))

    @abstractmethod
    def getDeltaX(self, ):
        """public abstract int com.badlogic.gdx.Input.getDeltaX()"""
        pass

    @overload
    def isKeyJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isKeyJustPressed(int)"""
        return bool._wrap(super(_AbstractInput, self).isKeyJustPressed(_int.valueOf(arg0)))

    @abstractmethod
    def isTouched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isTouched()"""
        pass

    @abstractmethod
    def getPressure(self, ):
        """public abstract float com.badlogic.gdx.Input.getPressure()"""
        pass

    @abstractmethod
    def getPitch(self, ):
        """public abstract float com.badlogic.gdx.Input.getPitch()"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int, arg1: bool):
        """public abstract void com.badlogic.gdx.Input.vibrate(int,boolean)"""
        pass

    @override
    @overload
    def setCatchBackKey(self, arg0: bool):
        """public void com.badlogic.gdx.AbstractInput.setCatchBackKey(boolean)"""
        super(_AbstractInput, self).setCatchBackKey(_boolean.valueOf(arg0))

    @abstractmethod
    def setCursorCatched(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setCursorCatched(boolean)"""
        pass

    @abstractmethod
    def isButtonPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isButtonPressed(int)"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int):
        """public abstract void com.badlogic.gdx.Input.vibrate(int)"""
        pass

    @abstractmethod
    def getAccelerometerX(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerX()"""
        pass

    @abstractmethod
    def getAzimuth(self, ):
        """public abstract float com.badlogic.gdx.Input.getAzimuth()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public abstract void com.badlogic.gdx.Input.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        pass

    @override
    @overload
    def isCatchBackKey(self) -> bool:
        """public boolean com.badlogic.gdx.AbstractInput.isCatchBackKey()"""
        return bool._wrap(super(AbstractInput, self).isCatchBackKey())

    @abstractmethod
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setOnscreenKeyboardVisible(boolean)"""
        pass

    @abstractmethod
    def setCursorPosition(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.Input.setCursorPosition(int,int)"""
        pass

    @abstractmethod
    def getGyroscopeZ(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeZ()"""
        pass

    @abstractmethod
    def getY(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getY(int)"""
        pass

    @override
    @overload
    def setCatchMenuKey(self, arg0: bool):
        """public void com.badlogic.gdx.AbstractInput.setCatchMenuKey(boolean)"""
        super(_AbstractInput, self).setCatchMenuKey(_boolean.valueOf(arg0))

    @abstractmethod
    def getCurrentEventTime(self, ):
        """public abstract long com.badlogic.gdx.Input.getCurrentEventTime()"""
        pass

    @abstractmethod
    def getAccelerometerZ(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerZ()"""
        pass

    @abstractmethod
    def getDeltaX(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getDeltaX(int)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def justTouched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.justTouched()"""
        pass

    @abstractmethod
    def getInputProcessor(self, ):
        """public abstract com.badlogic.gdx.InputProcessor com.badlogic.gdx.Input.getInputProcessor()"""
        pass

    @abstractmethod
    def getX(self, ):
        """public abstract int com.badlogic.gdx.Input.getX()"""
        pass

    @abstractmethod
    def getAccelerometerY(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerY()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ApplicationLogger
import java.lang.Throwable as Throwable
import com.badlogic.gdx.ApplicationLogger as _ApplicationLogger
_ApplicationLogger = _ApplicationLogger
from abc import abstractmethod, ABC
 
class ApplicationLogger():
    """com.badlogic.gdx.ApplicationLogger"""
 
    @staticmethod
    def _wrap(java_value: _ApplicationLogger) -> 'ApplicationLogger':
        return ApplicationLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ApplicationLogger):
        """
        Dynamic initializer for ApplicationLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ApplicationLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ApplicationLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def error(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.ApplicationLogger.error(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.ApplicationLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.ApplicationLogger.log(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.ApplicationLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.ApplicationLogger.debug(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.ApplicationLogger.log(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Game
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ApplicationListener as _ApplicationListener
_ApplicationListener = _ApplicationListener
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.badlogic.gdx.Game as _Game
_Game = _Game
import java.lang.Integer as _int
import com.badlogic.gdx.Screen as _Screen
_Screen = _Screen
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Game():
    """com.badlogic.gdx.Game"""
 
    @staticmethod
    def _wrap(java_value: _Game) -> 'Game':
        return Game(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Game):
        """
        Dynamic initializer for Game.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Game__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Game__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.Game.pause()"""
        super(Game, self).pause()

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.Game.resume()"""
        super(Game, self).resume()

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

    @overload
    def setScreen(self, arg0: 'Screen'):
        """public void com.badlogic.gdx.Game.setScreen(com.badlogic.gdx.Screen)"""
        super(_Game, self).setScreen(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.Game.dispose()"""
        super(Game, self).dispose()

    @overload
    def getScreen(self) -> 'Screen':
        """public com.badlogic.gdx.Screen com.badlogic.gdx.Game.getScreen()"""
        return 'Screen'._wrap(super(Game, self).getScreen())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.Game()"""
        val = _Game()
        self.__wrapper = val

    @abstractmethod
    def create(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.create()"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.Game()"""
        val = _Game()
        self.__wrapper = val

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.Game.resize(int,int)"""
        super(_Game, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

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

    @override
    @overload
    def render(self):
        """public void com.badlogic.gdx.Game.render()"""
        super(Game, self).render()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.Preferences
import com.badlogic.gdx.Preferences as _Preferences
_Preferences = _Preferences
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class Preferences():
    """com.badlogic.gdx.Preferences"""
 
    @staticmethod
    def _wrap(java_value: _Preferences) -> 'Preferences':
        return Preferences(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Preferences):
        """
        Dynamic initializer for Preferences.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Preferences__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Preferences__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getBoolean(self, arg0: str, arg1: bool):
        """public abstract boolean com.badlogic.gdx.Preferences.getBoolean(java.lang.String,boolean)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void com.badlogic.gdx.Preferences.clear()"""
        pass

    @abstractmethod
    def put(self, arg0: 'Map'):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.put(java.util.Map<java.lang.String, ?>)"""
        pass

    @abstractmethod
    def getFloat(self, arg0: str):
        """public abstract float com.badlogic.gdx.Preferences.getFloat(java.lang.String)"""
        pass

    @abstractmethod
    def putBoolean(self, arg0: str, arg1: bool):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putBoolean(java.lang.String,boolean)"""
        pass

    @abstractmethod
    def getInteger(self, arg0: str):
        """public abstract int com.badlogic.gdx.Preferences.getInteger(java.lang.String)"""
        pass

    @abstractmethod
    def putFloat(self, arg0: str, arg1: float):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putFloat(java.lang.String,float)"""
        pass

    @abstractmethod
    def putString(self, arg0: str, arg1: str):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putString(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def getLong(self, arg0: str):
        """public abstract long com.badlogic.gdx.Preferences.getLong(java.lang.String)"""
        pass

    @abstractmethod
    def getLong(self, arg0: str, arg1: int):
        """public abstract long com.badlogic.gdx.Preferences.getLong(java.lang.String,long)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.Preferences.flush()"""
        pass

    @abstractmethod
    def getFloat(self, arg0: str, arg1: float):
        """public abstract float com.badlogic.gdx.Preferences.getFloat(java.lang.String,float)"""
        pass

    @abstractmethod
    def putInteger(self, arg0: str, arg1: int):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putInteger(java.lang.String,int)"""
        pass

    @abstractmethod
    def getString(self, arg0: str, arg1: str):
        """public abstract java.lang.String com.badlogic.gdx.Preferences.getString(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, arg0: str):
        """public abstract void com.badlogic.gdx.Preferences.remove(java.lang.String)"""
        pass

    @abstractmethod
    def get(self, ):
        """public abstract java.util.Map<java.lang.String, ?> com.badlogic.gdx.Preferences.get()"""
        pass

    @abstractmethod
    def getBoolean(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Preferences.getBoolean(java.lang.String)"""
        pass

    @abstractmethod
    def contains(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Preferences.contains(java.lang.String)"""
        pass

    @abstractmethod
    def getInteger(self, arg0: str, arg1: int):
        """public abstract int com.badlogic.gdx.Preferences.getInteger(java.lang.String,int)"""
        pass

    @abstractmethod
    def putLong(self, arg0: str, arg1: int):
        """public abstract com.badlogic.gdx.Preferences com.badlogic.gdx.Preferences.putLong(java.lang.String,long)"""
        pass

    @abstractmethod
    def getString(self, arg0: str):
        """public abstract java.lang.String com.badlogic.gdx.Preferences.getString(java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ScreenAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ScreenAdapter as _ScreenAdapter
_ScreenAdapter = _ScreenAdapter
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScreenAdapter():
    """com.badlogic.gdx.ScreenAdapter"""
 
    @staticmethod
    def _wrap(java_value: _ScreenAdapter) -> 'ScreenAdapter':
        return ScreenAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScreenAdapter):
        """
        Dynamic initializer for ScreenAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScreenAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScreenAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.ScreenAdapter()"""
        val = _ScreenAdapter()
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ScreenAdapter.dispose()"""
        super(ScreenAdapter, self).dispose()

    @override
    @overload
    def hide(self):
        """public void com.badlogic.gdx.ScreenAdapter.hide()"""
        super(ScreenAdapter, self).hide()

    @override
    @overload
    def show(self):
        """public void com.badlogic.gdx.ScreenAdapter.show()"""
        super(ScreenAdapter, self).show()

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
    def pause(self):
        """public void com.badlogic.gdx.ScreenAdapter.pause()"""
        super(ScreenAdapter, self).pause()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.ScreenAdapter.resize(int,int)"""
        super(_ScreenAdapter, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.ScreenAdapter.resume()"""
        super(ScreenAdapter, self).resume()

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
    def render(self, arg0: float):
        """public void com.badlogic.gdx.ScreenAdapter.render(float)"""
        super(_ScreenAdapter, self).render(_float.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ScreenAdapter()"""
        val = _ScreenAdapter()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.Input$TextInputListener
import com.badlogic.gdx.Input as _Input_TextInputListener
_TextInputListener = _Input_TextInputListener.TextInputListener
from abc import abstractmethod, ABC
 
class TextInputListener():
    """com.badlogic.gdx.Input.TextInputListener"""
 
    @staticmethod
    def _wrap(java_value: _TextInputListener) -> 'TextInputListener':
        return TextInputListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextInputListener):
        """
        Dynamic initializer for TextInputListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextInputListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextInputListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def input(self, arg0: str):
        """public abstract void com.badlogic.gdx.Input$TextInputListener.input(java.lang.String)"""
        pass

    @abstractmethod
    def canceled(self, ):
        """public abstract void com.badlogic.gdx.Input$TextInputListener.canceled()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.AbstractGraphics
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.AbstractGraphics as _AbstractGraphics
_AbstractGraphics = _AbstractGraphics
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.badlogic.gdx.Graphics as _Graphics
_Graphics = _Graphics
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractGraphics():
    """com.badlogic.gdx.AbstractGraphics"""
 
    @staticmethod
    def _wrap(java_value: _AbstractGraphics) -> 'AbstractGraphics':
        return AbstractGraphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractGraphics):
        """
        Dynamic initializer for AbstractGraphics.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractGraphics__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractGraphics__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def newCursor(self, arg0: 'Pixmap', arg1: int, arg2: int):
        """public abstract com.badlogic.gdx.graphics.Cursor com.badlogic.gdx.Graphics.newCursor(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def getSafeInsetLeft(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetLeft()"""
        pass

    @abstractmethod
    def setVSync(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setVSync(boolean)"""
        pass

    @abstractmethod
    def getSafeInsetTop(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetTop()"""
        pass

    @abstractmethod
    def getMonitor(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.Graphics.getMonitor()"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @abstractmethod
    def getDisplayMode(self, ):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.Graphics.getDisplayMode()"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getMonitors(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor[] com.badlogic.gdx.Graphics.getMonitors()"""
        pass

    @override
    @overload
    def getRawDeltaTime(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getRawDeltaTime()"""
        return float._wrap(super(AbstractGraphics, self).getRawDeltaTime())

    @abstractmethod
    def setGL20(self, arg0: 'GL20'):
        """public abstract void com.badlogic.gdx.Graphics.setGL20(com.badlogic.gdx.graphics.GL20)"""
        pass

    @abstractmethod
    def setGL31(self, arg0: 'GL31'):
        """public abstract void com.badlogic.gdx.Graphics.setGL31(com.badlogic.gdx.graphics.GL31)"""
        pass

    @abstractmethod
    def getPpiX(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpiX()"""
        pass

    @abstractmethod
    def supportsExtension(self, arg0: str):
        """public abstract boolean com.badlogic.gdx.Graphics.supportsExtension(java.lang.String)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @abstractmethod
    def isGL32Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL32Available()"""
        pass

    @abstractmethod
    def getBackBufferHeight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getBackBufferHeight()"""
        pass

    @abstractmethod
    def getPpcY(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpcY()"""
        pass

    @abstractmethod
    def getDisplayMode(self, arg0: 'Monitor'):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode com.badlogic.gdx.Graphics.getDisplayMode(com.badlogic.gdx.Graphics$Monitor)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def getFrameId(self, ):
        """public abstract long com.badlogic.gdx.Graphics.getFrameId()"""
        pass

    @abstractmethod
    def getPpcX(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpcX()"""
        pass

    @abstractmethod
    def getSafeInsetBottom(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetBottom()"""
        pass

    @abstractmethod
    def setGL30(self, arg0: 'GL30'):
        """public abstract void com.badlogic.gdx.Graphics.setGL30(com.badlogic.gdx.graphics.GL30)"""
        pass

    @abstractmethod
    def getDisplayModes(self, ):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.Graphics.getDisplayModes()"""
        pass

    @abstractmethod
    def setTitle(self, arg0: str):
        """public abstract void com.badlogic.gdx.Graphics.setTitle(java.lang.String)"""
        pass

    @abstractmethod
    def supportsDisplayModeChange(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.supportsDisplayModeChange()"""
        pass

    @abstractmethod
    def getGL30(self, ):
        """public abstract com.badlogic.gdx.graphics.GL30 com.badlogic.gdx.Graphics.getGL30()"""
        pass

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

    @abstractmethod
    def setGL32(self, arg0: 'GL32'):
        """public abstract void com.badlogic.gdx.Graphics.setGL32(com.badlogic.gdx.graphics.GL32)"""
        pass

    @override
    @overload
    def getBackBufferScale(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getBackBufferScale()"""
        return float._wrap(super(AbstractGraphics, self).getBackBufferScale())

    @abstractmethod
    def setWindowedMode(self, arg0: int, arg1: int):
        """public abstract boolean com.badlogic.gdx.Graphics.setWindowedMode(int,int)"""
        pass

    @abstractmethod
    def isFullscreen(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isFullscreen()"""
        pass

    @abstractmethod
    def getGL32(self, ):
        """public abstract com.badlogic.gdx.graphics.GL32 com.badlogic.gdx.Graphics.getGL32()"""
        pass

    @abstractmethod
    def isGL31Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL31Available()"""
        pass

    @abstractmethod
    def getGLVersion(self, ):
        """public abstract com.badlogic.gdx.graphics.glutils.GLVersion com.badlogic.gdx.Graphics.getGLVersion()"""
        pass

    @abstractmethod
    def getPpiY(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getPpiY()"""
        pass

    @abstractmethod
    def getBackBufferWidth(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getBackBufferWidth()"""
        pass

    @abstractmethod
    def getSafeInsetRight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getSafeInsetRight()"""
        pass

    @abstractmethod
    def getBufferFormat(self, ):
        """public abstract com.badlogic.gdx.Graphics$BufferFormat com.badlogic.gdx.Graphics.getBufferFormat()"""
        pass

    @abstractmethod
    def isContinuousRendering(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isContinuousRendering()"""
        pass

    @abstractmethod
    def setContinuousRendering(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setContinuousRendering(boolean)"""
        pass

    @abstractmethod
    def getDeltaTime(self, ):
        """public abstract float com.badlogic.gdx.Graphics.getDeltaTime()"""
        pass

    @abstractmethod
    def setFullscreenMode(self, arg0: 'DisplayMode'):
        """public abstract boolean com.badlogic.gdx.Graphics.setFullscreenMode(com.badlogic.gdx.Graphics$DisplayMode)"""
        pass

    @abstractmethod
    def setCursor(self, arg0: 'Cursor'):
        """public abstract void com.badlogic.gdx.Graphics.setCursor(com.badlogic.gdx.graphics.Cursor)"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.Graphics$GraphicsType com.badlogic.gdx.Graphics.getType()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getWidth()"""
        pass

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.AbstractGraphics()"""
        val = _AbstractGraphics()
        self.__wrapper = val

    @abstractmethod
    def setResizable(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setResizable(boolean)"""
        pass

    @abstractmethod
    def setForegroundFPS(self, arg0: int):
        """public abstract void com.badlogic.gdx.Graphics.setForegroundFPS(int)"""
        pass

    @abstractmethod
    def requestRendering(self, ):
        """public abstract void com.badlogic.gdx.Graphics.requestRendering()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def getDisplayModes(self, arg0: 'Monitor'):
        """public abstract com.badlogic.gdx.Graphics$DisplayMode[] com.badlogic.gdx.Graphics.getDisplayModes(com.badlogic.gdx.Graphics$Monitor)"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getHeight()"""
        pass

    @abstractmethod
    def getFramesPerSecond(self, ):
        """public abstract int com.badlogic.gdx.Graphics.getFramesPerSecond()"""
        pass

    @override
    @overload
    def getDensity(self) -> float:
        """public float com.badlogic.gdx.AbstractGraphics.getDensity()"""
        return float._wrap(super(AbstractGraphics, self).getDensity())

    @abstractmethod
    def isGL30Available(self, ):
        """public abstract boolean com.badlogic.gdx.Graphics.isGL30Available()"""
        pass

    @abstractmethod
    def getGL31(self, ):
        """public abstract com.badlogic.gdx.graphics.GL31 com.badlogic.gdx.Graphics.getGL31()"""
        pass

    @abstractmethod
    def setUndecorated(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Graphics.setUndecorated(boolean)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def setSystemCursor(self, arg0: 'SystemCursor'):
        """public abstract void com.badlogic.gdx.Graphics.setSystemCursor(com.badlogic.gdx.graphics.Cursor$SystemCursor)"""
        pass

    @abstractmethod
    def getPrimaryMonitor(self, ):
        """public abstract com.badlogic.gdx.Graphics$Monitor com.badlogic.gdx.Graphics.getPrimaryMonitor()"""
        pass

    @overload
    def __init__(self):
        """public com.badlogic.gdx.AbstractGraphics()"""
        val = _AbstractGraphics()
        self.__wrapper = val

    @abstractmethod
    def getGL20(self, ):
        """public abstract com.badlogic.gdx.graphics.GL20 com.badlogic.gdx.Graphics.getGL20()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ApplicationListener
import com.badlogic.gdx.ApplicationListener as _ApplicationListener
_ApplicationListener = _ApplicationListener
from abc import abstractmethod, ABC
 
class ApplicationListener():
    """com.badlogic.gdx.ApplicationListener"""
 
    @staticmethod
    def _wrap(java_value: _ApplicationListener) -> 'ApplicationListener':
        return ApplicationListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ApplicationListener):
        """
        Dynamic initializer for ApplicationListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ApplicationListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ApplicationListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def resize(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.ApplicationListener.resize(int,int)"""
        pass

    @abstractmethod
    def create(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.create()"""
        pass

    @abstractmethod
    def render(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.render()"""
        pass

    @abstractmethod
    def resume(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.resume()"""
        pass

    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.pause()"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.ApplicationListener.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.InputAdapter
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.InputAdapter as _InputAdapter
_InputAdapter = _InputAdapter
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InputAdapter():
    """com.badlogic.gdx.InputAdapter"""
 
    @staticmethod
    def _wrap(java_value: _InputAdapter) -> 'InputAdapter':
        return InputAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InputAdapter):
        """
        Dynamic initializer for InputAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InputAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InputAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchDown(int,int,int,int)"""
        return bool._wrap(super(_InputAdapter, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.InputAdapter()"""
        val = _InputAdapter()
        self.__wrapper = val

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.mouseMoved(int,int)"""
        return bool._wrap(super(_InputAdapter, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_InputAdapter, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.InputAdapter()"""
        val = _InputAdapter()
        self.__wrapper = val

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyDown(int)"""
        return bool._wrap(super(_InputAdapter, self).keyDown(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyUp(int)"""
        return bool._wrap(super(_InputAdapter, self).keyUp(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyTyped(char)"""
        return bool._wrap(super(_InputAdapter, self).keyTyped(_char.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchUp(int,int,int,int)"""
        return bool._wrap(super(_InputAdapter, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.scrolled(float,float)"""
        return bool._wrap(super(_InputAdapter, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

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
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.touchDragged(int,int,int)"""
        return bool._wrap(super(_InputAdapter, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.InputEventQueue
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.InputEventQueue as _InputEventQueue
_InputEventQueue = _InputEventQueue
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InputEventQueue():
    """com.badlogic.gdx.InputEventQueue"""
 
    @staticmethod
    def _wrap(java_value: _InputEventQueue) -> 'InputEventQueue':
        return InputEventQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InputEventQueue):
        """
        Dynamic initializer for InputEventQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InputEventQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InputEventQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.touchDown(int,int,int,int,long)"""
        return bool._wrap(super(_InputEventQueue, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @overload
    def drain(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.InputEventQueue.drain(com.badlogic.gdx.InputProcessor)"""
        super(_InputEventQueue, self).drain(arg0)

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.touchDragged(int,int,int,long)"""
        return bool._wrap(super(_InputEventQueue, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.InputEventQueue()"""
        val = _InputEventQueue()
        self.__wrapper = val

    @overload
    def getCurrentEventTime(self) -> int:
        """public long com.badlogic.gdx.InputEventQueue.getCurrentEventTime()"""
        return int._wrap(super(InputEventQueue, self).getCurrentEventTime())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.InputEventQueue()"""
        val = _InputEventQueue()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def scrolled(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.scrolled(float,float,long)"""
        return bool._wrap(super(_InputEventQueue, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2)))

    @overload
    def mouseMoved(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.mouseMoved(int,int,long)"""
        return bool._wrap(super(_InputEventQueue, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @overload
    def keyTyped(self, arg0: str, arg1: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.keyTyped(char,long)"""
        return bool._wrap(super(_InputEventQueue, self).keyTyped(_char.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.touchUp(int,int,int,int,long)"""
        return bool._wrap(super(_InputEventQueue, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def keyDown(self, arg0: int, arg1: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.keyDown(int,long)"""
        return bool._wrap(super(_InputEventQueue, self).keyDown(_int.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def keyUp(self, arg0: int, arg1: int) -> bool:
        """public synchronized boolean com.badlogic.gdx.InputEventQueue.keyUp(int,long)"""
        return bool._wrap(super(_InputEventQueue, self).keyUp(_int.valueOf(arg0), _long.valueOf(arg1)))

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
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.LifecycleListener
import com.badlogic.gdx.LifecycleListener as _LifecycleListener
_LifecycleListener = _LifecycleListener
from abc import abstractmethod, ABC
 
class LifecycleListener():
    """com.badlogic.gdx.LifecycleListener"""
 
    @staticmethod
    def _wrap(java_value: _LifecycleListener) -> 'LifecycleListener':
        return LifecycleListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LifecycleListener):
        """
        Dynamic initializer for LifecycleListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LifecycleListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LifecycleListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.LifecycleListener.dispose()"""
        pass

    @abstractmethod
    def resume(self, ):
        """public abstract void com.badlogic.gdx.LifecycleListener.resume()"""
        pass

    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.LifecycleListener.pause()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Input$Peripheral
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import com.badlogic.gdx.Input as _Input_Peripheral
_Peripheral = _Input_Peripheral.Peripheral
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Peripheral():
    """com.badlogic.gdx.Input.Peripheral"""
 
    @staticmethod
    def _wrap(java_value: _Peripheral) -> 'Peripheral':
        return Peripheral(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Peripheral):
        """
        Dynamic initializer for Peripheral.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Peripheral__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Peripheral__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['Peripheral']:
        """public static com.badlogic.gdx.Input$Peripheral[] com.badlogic.gdx.Input$Peripheral.values()"""
        return List[Peripheral]._wrap(_Peripheral.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Peripheral':
        """public static com.badlogic.gdx.Input$Peripheral com.badlogic.gdx.Input$Peripheral.valueOf(java.lang.String)"""
        return Peripheral._wrap(_Peripheral.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.Input
import com.badlogic.gdx.Input as _Input
_Input = _Input
from builtins import float
from abc import abstractmethod, ABC
 
class Input():
    """com.badlogic.gdx.Input"""
 
    @staticmethod
    def _wrap(java_value: _Input) -> 'Input':
        return Input(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Input):
        """
        Dynamic initializer for Input.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Input__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Input__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getRotation(self, ):
        """public abstract int com.badlogic.gdx.Input.getRotation()"""
        pass

    @abstractmethod
    def setCatchBackKey(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setCatchBackKey(boolean)"""
        pass

    @abstractmethod
    def getNativeOrientation(self, ):
        """public abstract com.badlogic.gdx.Input$Orientation com.badlogic.gdx.Input.getNativeOrientation()"""
        pass

    @abstractmethod
    def isKeyJustPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isKeyJustPressed(int)"""
        pass

    @abstractmethod
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public abstract void com.badlogic.gdx.Input.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        pass

    @abstractmethod
    def isKeyPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isKeyPressed(int)"""
        pass

    @abstractmethod
    def getDeltaY(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getDeltaY(int)"""
        pass

    @abstractmethod
    def getMaxPointers(self, ):
        """public abstract int com.badlogic.gdx.Input.getMaxPointers()"""
        pass

    @abstractmethod
    def isTouched(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isTouched(int)"""
        pass

    @abstractmethod
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public abstract void com.badlogic.gdx.Input.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def isButtonJustPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isButtonJustPressed(int)"""
        pass

    @abstractmethod
    def getY(self, ):
        """public abstract int com.badlogic.gdx.Input.getY()"""
        pass

    @abstractmethod
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public abstract void com.badlogic.gdx.Input.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        pass

    @abstractmethod
    def getRoll(self, ):
        """public abstract float com.badlogic.gdx.Input.getRoll()"""
        pass

    @abstractmethod
    def getDeltaY(self, ):
        """public abstract int com.badlogic.gdx.Input.getDeltaY()"""
        pass

    @abstractmethod
    def isCatchKey(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isCatchKey(int)"""
        pass

    @abstractmethod
    def getPressure(self, arg0: int):
        """public abstract float com.badlogic.gdx.Input.getPressure(int)"""
        pass

    @abstractmethod
    def setCatchKey(self, arg0: int, arg1: bool):
        """public abstract void com.badlogic.gdx.Input.setCatchKey(int,boolean)"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public abstract void com.badlogic.gdx.Input.vibrate(int,int,boolean)"""
        pass

    @abstractmethod
    def getX(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getX(int)"""
        pass

    @abstractmethod
    def isCursorCatched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isCursorCatched()"""
        pass

    @abstractmethod
    def isPeripheralAvailable(self, arg0: 'Peripheral'):
        """public abstract boolean com.badlogic.gdx.Input.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        pass

    @abstractmethod
    def getRotationMatrix(self, arg0: 'float'):
        """public abstract void com.badlogic.gdx.Input.getRotationMatrix(float[])"""
        pass

    @abstractmethod
    def getGyroscopeY(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeY()"""
        pass

    @abstractmethod
    def getGyroscopeX(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeX()"""
        pass

    @abstractmethod
    def vibrate(self, arg0: 'VibrationType'):
        """public abstract void com.badlogic.gdx.Input.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        pass

    @abstractmethod
    def isCatchBackKey(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isCatchBackKey()"""
        pass

    @abstractmethod
    def getDeltaX(self, ):
        """public abstract int com.badlogic.gdx.Input.getDeltaX()"""
        pass

    @abstractmethod
    def isTouched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isTouched()"""
        pass

    @abstractmethod
    def getPressure(self, ):
        """public abstract float com.badlogic.gdx.Input.getPressure()"""
        pass

    @abstractmethod
    def getPitch(self, ):
        """public abstract float com.badlogic.gdx.Input.getPitch()"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int, arg1: bool):
        """public abstract void com.badlogic.gdx.Input.vibrate(int,boolean)"""
        pass

    @abstractmethod
    def setCursorCatched(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setCursorCatched(boolean)"""
        pass

    @abstractmethod
    def isButtonPressed(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.Input.isButtonPressed(int)"""
        pass

    @abstractmethod
    def vibrate(self, arg0: int):
        """public abstract void com.badlogic.gdx.Input.vibrate(int)"""
        pass

    @abstractmethod
    def getAccelerometerX(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerX()"""
        pass

    @abstractmethod
    def getAzimuth(self, ):
        """public abstract float com.badlogic.gdx.Input.getAzimuth()"""
        pass

    @abstractmethod
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public abstract void com.badlogic.gdx.Input.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        pass

    @abstractmethod
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setOnscreenKeyboardVisible(boolean)"""
        pass

    @abstractmethod
    def setCursorPosition(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.Input.setCursorPosition(int,int)"""
        pass

    @abstractmethod
    def isCatchMenuKey(self, ):
        """public abstract boolean com.badlogic.gdx.Input.isCatchMenuKey()"""
        pass

    @abstractmethod
    def getGyroscopeZ(self, ):
        """public abstract float com.badlogic.gdx.Input.getGyroscopeZ()"""
        pass

    @abstractmethod
    def getY(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getY(int)"""
        pass

    @abstractmethod
    def getCurrentEventTime(self, ):
        """public abstract long com.badlogic.gdx.Input.getCurrentEventTime()"""
        pass

    @abstractmethod
    def getAccelerometerZ(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerZ()"""
        pass

    @abstractmethod
    def getDeltaX(self, arg0: int):
        """public abstract int com.badlogic.gdx.Input.getDeltaX(int)"""
        pass

    @abstractmethod
    def justTouched(self, ):
        """public abstract boolean com.badlogic.gdx.Input.justTouched()"""
        pass

    @abstractmethod
    def getInputProcessor(self, ):
        """public abstract com.badlogic.gdx.InputProcessor com.badlogic.gdx.Input.getInputProcessor()"""
        pass

    @abstractmethod
    def getX(self, ):
        """public abstract int com.badlogic.gdx.Input.getX()"""
        pass

    @abstractmethod
    def setCatchMenuKey(self, arg0: bool):
        """public abstract void com.badlogic.gdx.Input.setCatchMenuKey(boolean)"""
        pass

    @abstractmethod
    def getAccelerometerY(self, ):
        """public abstract float com.badlogic.gdx.Input.getAccelerometerY()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.Files$FileType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.Files as _Files_FileType
_FileType = _Files_FileType.FileType
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileType():
    """com.badlogic.gdx.Files.FileType"""
 
    @staticmethod
    def _wrap(java_value: _FileType) -> 'FileType':
        return FileType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileType):
        """
        Dynamic initializer for FileType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FileType':
        """public static com.badlogic.gdx.Files$FileType com.badlogic.gdx.Files$FileType.valueOf(java.lang.String)"""
        return FileType._wrap(_FileType.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['FileType']:
        """public static com.badlogic.gdx.Files$FileType[] com.badlogic.gdx.Files$FileType.values()"""
        return List[FileType]._wrap(_FileType.values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.Net$Protocol
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import com.badlogic.gdx.Net as _Net_Protocol
_Protocol = _Net_Protocol.Protocol
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Protocol():
    """com.badlogic.gdx.Net.Protocol"""
 
    @staticmethod
    def _wrap(java_value: _Protocol) -> 'Protocol':
        return Protocol(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Protocol):
        """
        Dynamic initializer for Protocol.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Protocol__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Protocol__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['Protocol']:
        """public static com.badlogic.gdx.Net$Protocol[] com.badlogic.gdx.Net$Protocol.values()"""
        return List[Protocol]._wrap(_Protocol.values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Protocol':
        """public static com.badlogic.gdx.Net$Protocol com.badlogic.gdx.Net$Protocol.valueOf(java.lang.String)"""
        return Protocol._wrap(_Protocol.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.Application$ApplicationType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.Application as _Application_ApplicationType
_ApplicationType = _Application_ApplicationType.ApplicationType
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ApplicationType():
    """com.badlogic.gdx.Application.ApplicationType"""
 
    @staticmethod
    def _wrap(java_value: _ApplicationType) -> 'ApplicationType':
        return ApplicationType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ApplicationType):
        """
        Dynamic initializer for ApplicationType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ApplicationType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ApplicationType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ApplicationType':
        """public static com.badlogic.gdx.Application$ApplicationType com.badlogic.gdx.Application$ApplicationType.valueOf(java.lang.String)"""
        return ApplicationType._wrap(_ApplicationType.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['ApplicationType']:
        """public static com.badlogic.gdx.Application$ApplicationType[] com.badlogic.gdx.Application$ApplicationType.values()"""
        return List[ApplicationType]._wrap(_ApplicationType.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.Net$HttpMethods
import com.badlogic.gdx.Net as _Net_HttpMethods
_HttpMethods = _Net_HttpMethods.HttpMethods
 
class HttpMethods():
    """com.badlogic.gdx.Net.HttpMethods"""
 
    @staticmethod
    def _wrap(java_value: _HttpMethods) -> 'HttpMethods':
        return HttpMethods(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpMethods):
        """
        Dynamic initializer for HttpMethods.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpMethods__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpMethods__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: com.badlogic.gdx.Graphics$BufferFormat
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.Graphics as _Graphics_BufferFormat
_BufferFormat = _Graphics_BufferFormat.BufferFormat
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BufferFormat():
    """com.badlogic.gdx.Graphics.BufferFormat"""
 
    @staticmethod
    def _wrap(java_value: _BufferFormat) -> 'BufferFormat':
        return BufferFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BufferFormat):
        """
        Dynamic initializer for BufferFormat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BufferFormat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BufferFormat__wrapper":
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
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool):
        """public com.badlogic.gdx.Graphics$BufferFormat(int,int,int,int,int,int,int,boolean)"""
        val = _BufferFormat(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _boolean.valueOf(arg7))
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
        """public java.lang.String com.badlogic.gdx.Graphics$BufferFormat.toString()"""
        return str._wrap(super(BufferFormat, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())
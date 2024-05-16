from __future__ import annotations
from overload import overload


 
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
import java.lang.String as _string
import com.badlogic.gdx.input.RemoteSender as _RemoteSender
_RemoteSender = _RemoteSender
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemoteSender():
    """com.badlogic.gdx.input.RemoteSender"""
 
    @staticmethod
    def _wrap(java_value: _RemoteSender) -> 'RemoteSender':
        return RemoteSender(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemoteSender):
        """
        Dynamic initializer for RemoteSender.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemoteSender__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemoteSender__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_RemoteSender, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchUp(int,int,int,int)"""
        return bool._wrap(super(_RemoteSender, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.mouseMoved(int,int)"""
        return bool._wrap(super(_RemoteSender, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.scrolled(float,float)"""
        return bool._wrap(super(_RemoteSender, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.keyUp(int)"""
        return bool._wrap(super(_RemoteSender, self).keyUp(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.keyDown(int)"""
        return bool._wrap(super(_RemoteSender, self).keyDown(_int.valueOf(arg0)))

    @overload
    def sendUpdate(self):
        """public void com.badlogic.gdx.input.RemoteSender.sendUpdate()"""
        super(RemoteSender, self).sendUpdate()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchDown(int,int,int,int)"""
        return bool._wrap(super(_RemoteSender, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.keyTyped(char)"""
        return bool._wrap(super(_RemoteSender, self).keyTyped(_char.valueOf(arg0)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchDragged(int,int,int)"""
        return bool._wrap(super(_RemoteSender, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.input.RemoteSender(java.lang.String,int)"""
        val = _RemoteSender(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def isConnected(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.isConnected()"""
        return bool._wrap(super(RemoteSender, self).isConnected())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.input.RemoteSender
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
import java.lang.String as _string
import com.badlogic.gdx.input.RemoteSender as _RemoteSender
_RemoteSender = _RemoteSender
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemoteSender():
    """com.badlogic.gdx.input.RemoteSender"""
 
    @staticmethod
    def _wrap(java_value: _RemoteSender) -> 'RemoteSender':
        return RemoteSender(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemoteSender):
        """
        Dynamic initializer for RemoteSender.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemoteSender__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemoteSender__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_RemoteSender, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchUp(int,int,int,int)"""
        return bool._wrap(super(_RemoteSender, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.mouseMoved(int,int)"""
        return bool._wrap(super(_RemoteSender, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.scrolled(float,float)"""
        return bool._wrap(super(_RemoteSender, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.keyUp(int)"""
        return bool._wrap(super(_RemoteSender, self).keyUp(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.keyDown(int)"""
        return bool._wrap(super(_RemoteSender, self).keyDown(_int.valueOf(arg0)))

    @overload
    def sendUpdate(self):
        """public void com.badlogic.gdx.input.RemoteSender.sendUpdate()"""
        super(RemoteSender, self).sendUpdate()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchDown(int,int,int,int)"""
        return bool._wrap(super(_RemoteSender, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

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
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.keyTyped(char)"""
        return bool._wrap(super(_RemoteSender, self).keyTyped(_char.valueOf(arg0)))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchDragged(int,int,int)"""
        return bool._wrap(super(_RemoteSender, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.input.RemoteSender(java.lang.String,int)"""
        val = _RemoteSender(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def isConnected(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.isConnected()"""
        return bool._wrap(super(RemoteSender, self).isConnected())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.input.RemoteSender 
 
 
# CLASS: com.badlogic.gdx.input.GestureDetector$GestureAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.input.GestureDetector as _GestureDetector_GestureAdapter
_GestureAdapter = _GestureDetector_GestureAdapter.GestureAdapter
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GestureAdapter():
    """com.badlogic.gdx.input.GestureDetector.GestureAdapter"""
 
    @staticmethod
    def _wrap(java_value: _GestureAdapter) -> 'GestureAdapter':
        return GestureAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GestureAdapter):
        """
        Dynamic initializer for GestureAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GestureAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GestureAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def panStop(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.panStop(float,float,int,int)"""
        return bool._wrap(super(_GestureAdapter, self).panStop(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def fling(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.fling(float,float,int)"""
        return bool._wrap(super(_GestureAdapter, self).fling(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def zoom(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.zoom(float,float)"""
        return bool._wrap(super(_GestureAdapter, self).zoom(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.touchDown(float,float,int,int)"""
        return bool._wrap(super(_GestureAdapter, self).touchDown(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.input.GestureDetector$GestureAdapter()"""
        val = _GestureAdapter()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def pinch(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.pinch(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_GestureAdapter, self).pinch(arg0, arg1, arg2, arg3))

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
    def pan(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.pan(float,float,float,float)"""
        return bool._wrap(super(_GestureAdapter, self).pan(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def longPress(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.longPress(float,float)"""
        return bool._wrap(super(_GestureAdapter, self).longPress(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def tap(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.tap(float,float,int,int)"""
        return bool._wrap(super(_GestureAdapter, self).tap(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def pinchStop(self):
        """public void com.badlogic.gdx.input.GestureDetector$GestureAdapter.pinchStop()"""
        super(GestureAdapter, self).pinchStop()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.input.GestureDetector$GestureAdapter()"""
        val = _GestureAdapter()
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
 
 
# CLASS: com.badlogic.gdx.input.GestureDetector
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.input.GestureDetector as _GestureDetector
_GestureDetector = _GestureDetector
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.InputAdapter as _InputAdapter
_InputAdapter = _InputAdapter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GestureDetector():
    """com.badlogic.gdx.input.GestureDetector"""
 
    @staticmethod
    def _wrap(java_value: _GestureDetector) -> 'GestureDetector':
        return GestureDetector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GestureDetector):
        """
        Dynamic initializer for GestureDetector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GestureDetector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GestureDetector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDown(float,float,int,int)"""
        return bool._wrap(super(_GestureDetector, self).touchDown(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'GestureListener'):
        """public com.badlogic.gdx.input.GestureDetector(float,float,float,float,com.badlogic.gdx.input.GestureDetector$GestureListener)"""
        val = _GestureDetector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)
        self.__wrapper = val

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchUp(int,int,int,int)"""
        return bool._wrap(super(_GestureDetector, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def reset(self):
        """public void com.badlogic.gdx.input.GestureDetector.reset()"""
        super(GestureDetector, self).reset()

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDragged(int,int,int)"""
        return bool._wrap(super(_GestureDetector, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyDown(int)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).keyDown(_int.valueOf(arg0)))

    @overload
    def isPanning(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isPanning()"""
        return bool._wrap(super(GestureDetector, self).isPanning())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLongPressSeconds(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setLongPressSeconds(float)"""
        super(_GestureDetector, self).setLongPressSeconds(_float.valueOf(arg0))

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
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_GestureDetector, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def setTapRectangleSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapRectangleSize(float,float)"""
        super(_GestureDetector, self).setTapRectangleSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'GestureListener'):
        """public com.badlogic.gdx.input.GestureDetector(com.badlogic.gdx.input.GestureDetector$GestureListener)"""
        val = _GestureDetector(arg0)
        self.__wrapper = val

    @overload
    def isLongPressed(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed()"""
        return bool._wrap(super(GestureDetector, self).isLongPressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'GestureListener'):
        """public com.badlogic.gdx.input.GestureDetector(float,float,float,float,float,com.badlogic.gdx.input.GestureDetector$GestureListener)"""
        val = _GestureDetector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5)
        self.__wrapper = val

    @overload
    def isLongPressed(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed(float)"""
        return bool._wrap(super(_GestureDetector, self).isLongPressed(_float.valueOf(arg0)))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.scrolled(float,float)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def touchDragged(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDragged(float,float,int)"""
        return bool._wrap(super(_GestureDetector, self).touchDragged(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDown(int,int,int,int)"""
        return bool._wrap(super(_GestureDetector, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.mouseMoved(int,int)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def touchUp(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchUp(float,float,int,int)"""
        return bool._wrap(super(_GestureDetector, self).touchUp(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyTyped(char)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).keyTyped(_char.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setTapCountInterval(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapCountInterval(float)"""
        super(_GestureDetector, self).setTapCountInterval(_float.valueOf(arg0))

    @overload
    def setMaxFlingDelay(self, arg0: int):
        """public void com.badlogic.gdx.input.GestureDetector.setMaxFlingDelay(long)"""
        super(_GestureDetector, self).setMaxFlingDelay(_long.valueOf(arg0))

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapSquareSize(float)"""
        super(_GestureDetector, self).setTapSquareSize(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def invalidateTapSquare(self):
        """public void com.badlogic.gdx.input.GestureDetector.invalidateTapSquare()"""
        super(GestureDetector, self).invalidateTapSquare()

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyUp(int)"""
        return bool._wrap(super(_pygdx.InputAdapter, self).keyUp(_int.valueOf(arg0)))

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.input.GestureDetector.cancel()"""
        super(GestureDetector, self).cancel()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.input.GestureDetector$GestureListener
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.input.GestureDetector as _GestureDetector_GestureListener
_GestureListener = _GestureDetector_GestureListener.GestureListener
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

 
class GestureListener():
    """com.badlogic.gdx.input.GestureDetector.GestureListener"""
 
    @staticmethod
    def _wrap(java_value: _GestureListener) -> 'GestureListener':
        return GestureListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GestureListener):
        """
        Dynamic initializer for GestureListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GestureListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GestureListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def pinchStop(self, ):
        """public abstract void com.badlogic.gdx.input.GestureDetector$GestureListener.pinchStop()"""
        pass

    @abstractmethod
    def fling(self, arg0: float, arg1: float, arg2: int):
        """public abstract boolean com.badlogic.gdx.input.GestureDetector$GestureListener.fling(float,float,int)"""
        pass

    @abstractmethod
    def panStop(self, arg0: float, arg1: float, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.input.GestureDetector$GestureListener.panStop(float,float,int,int)"""
        pass

    @abstractmethod
    def longPress(self, arg0: float, arg1: float):
        """public abstract boolean com.badlogic.gdx.input.GestureDetector$GestureListener.longPress(float,float)"""
        pass

    @abstractmethod
    def tap(self, arg0: float, arg1: float, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.input.GestureDetector$GestureListener.tap(float,float,int,int)"""
        pass

    @abstractmethod
    def pinch(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2'):
        """public abstract boolean com.badlogic.gdx.input.GestureDetector$GestureListener.pinch(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        pass

    @abstractmethod
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int):
        """public abstract boolean com.badlogic.gdx.input.GestureDetector$GestureListener.touchDown(float,float,int,int)"""
        pass

    @abstractmethod
    def pan(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract boolean com.badlogic.gdx.input.GestureDetector$GestureListener.pan(float,float,float,float)"""
        pass

    @abstractmethod
    def zoom(self, arg0: float, arg1: float):
        """public abstract boolean com.badlogic.gdx.input.GestureDetector$GestureListener.zoom(float,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.input.RemoteInput
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
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.String as _string
import com.badlogic.gdx.input.RemoteInput as _RemoteInput
_RemoteInput = _RemoteInput
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.Input as _Input_Orientation
_Orientation = _Input_Orientation.Orientation
import com.badlogic.gdx.InputProcessor as _InputProcessor
_InputProcessor = _InputProcessor
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemoteInput():
    """com.badlogic.gdx.input.RemoteInput"""
 
    @staticmethod
    def _wrap(java_value: _RemoteInput) -> 'RemoteInput':
        return RemoteInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemoteInput):
        """
        Dynamic initializer for RemoteInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemoteInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemoteInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAccelerometerX(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getAccelerometerX()"""
        return float._wrap(super(RemoteInput, self).getAccelerometerX())

    @override
    @overload
    def vibrate(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.input.RemoteInput.vibrate(int,boolean)"""
        super(_RemoteInput, self).vibrate(_int.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getX()"""
        return int._wrap(super(RemoteInput, self).getX())

    @overload
    def isPeripheralAvailable(self, arg0: 'Peripheral') -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        return bool._wrap(super(_RemoteInput, self).isPeripheralAvailable(arg0))

    @override
    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.input.RemoteInput.setCursorPosition(int,int)"""
        super(_RemoteInput, self).setCursorPosition(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isButtonPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isButtonPressed(int)"""
        return bool._wrap(super(_RemoteInput, self).isButtonPressed(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getX(int)"""
        return int._wrap(super(_RemoteInput, self).getX(_int.valueOf(arg0)))

    @override
    @overload
    def getAccelerometerY(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getAccelerometerY()"""
        return float._wrap(super(RemoteInput, self).getAccelerometerY())

    @overload
    def __init__(self, arg0: int, arg1: 'RemoteInputListener'):
        """public com.badlogic.gdx.input.RemoteInput(int,com.badlogic.gdx.input.RemoteInput$RemoteInputListener)"""
        val = _RemoteInput(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def getCurrentEventTime(self) -> int:
        """public long com.badlogic.gdx.input.RemoteInput.getCurrentEventTime()"""
        return int._wrap(super(RemoteInput, self).getCurrentEventTime())

    @override
    @overload
    def getMaxPointers(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getMaxPointers()"""
        return int._wrap(super(RemoteInput, self).getMaxPointers())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.input.RemoteInput(int)"""
        val = _RemoteInput(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setCatchMenuKey(self, arg0: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setCatchMenuKey(boolean)"""
        super(_RemoteInput, self).setCatchMenuKey(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.input.RemoteInput()"""
        val = _RemoteInput()
        self.__wrapper = val

    @overload
    def isKeyPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isKeyPressed(int)"""
        return bool._wrap(super(_RemoteInput, self).isKeyPressed(_int.valueOf(arg0)))

    @overload
    def isConnected(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isConnected()"""
        return bool._wrap(super(RemoteInput, self).isConnected())

    @override
    @overload
    def getAccelerometerZ(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getAccelerometerZ()"""
        return float._wrap(super(RemoteInput, self).getAccelerometerZ())

    @override
    @overload
    def getRotationMatrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.input.RemoteInput.getRotationMatrix(float[])"""
        super(_RemoteInput, self).getRotationMatrix(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setCursorCatched(self, arg0: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setCursorCatched(boolean)"""
        super(_RemoteInput, self).setCursorCatched(_boolean.valueOf(arg0))

    @override
    @overload
    def isTouched(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isTouched()"""
        return bool._wrap(super(RemoteInput, self).isTouched())

    @override
    @overload
    def vibrate(self, arg0: int):
        """public void com.badlogic.gdx.input.RemoteInput.vibrate(int)"""
        super(_RemoteInput, self).vibrate(_int.valueOf(arg0))

    @override
    @overload
    def setCatchKey(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setCatchKey(int,boolean)"""
        super(_RemoteInput, self).setCatchKey(_int.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.input.RemoteInput()"""
        val = _RemoteInput()
        self.__wrapper = val

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.input.RemoteInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(_RemoteInput, self).getTextInput(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getIPs(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.input.RemoteInput.getIPs()"""
        return List[str]._wrap(super(RemoteInput, self).getIPs())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def getPressure(self, arg0: int) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getPressure(int)"""
        return float._wrap(super(_RemoteInput, self).getPressure(_int.valueOf(arg0)))

    @overload
    def isTouched(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isTouched(int)"""
        return bool._wrap(super(_RemoteInput, self).isTouched(_int.valueOf(arg0)))

    @override
    @overload
    def getInputProcessor(self) -> 'pygdx.InputProcessor':
        """public com.badlogic.gdx.InputProcessor com.badlogic.gdx.input.RemoteInput.getInputProcessor()"""
        return 'pygdx.InputProcessor'._wrap(super(RemoteInput, self).getInputProcessor())

    @override
    @overload
    def getDeltaX(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getDeltaX()"""
        return int._wrap(super(RemoteInput, self).getDeltaX())

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.input.RemoteInput.run()"""
        super(RemoteInput, self).run()

    @override
    @overload
    def setCatchBackKey(self, arg0: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setCatchBackKey(boolean)"""
        super(_RemoteInput, self).setCatchBackKey(_boolean.valueOf(arg0))

    @override
    @overload
    def isCursorCatched(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isCursorCatched()"""
        return bool._wrap(super(RemoteInput, self).isCursorCatched())

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setOnscreenKeyboardVisible(boolean)"""
        super(_RemoteInput, self).setOnscreenKeyboardVisible(_boolean.valueOf(arg0))

    @overload
    def isCatchKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isCatchKey(int)"""
        return bool._wrap(super(_RemoteInput, self).isCatchKey(_int.valueOf(arg0)))

    @override
    @overload
    def getAzimuth(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getAzimuth()"""
        return float._wrap(super(RemoteInput, self).getAzimuth())

    @override
    @overload
    def getNativeOrientation(self) -> 'pygdx.Input$Orientation':
        """public com.badlogic.gdx.Input$Orientation com.badlogic.gdx.input.RemoteInput.getNativeOrientation()"""
        return 'pygdx.Input$Orientation'._wrap(super(RemoteInput, self).getNativeOrientation())

    @override
    @overload
    def isCatchMenuKey(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isCatchMenuKey()"""
        return bool._wrap(super(RemoteInput, self).isCatchMenuKey())

    @overload
    def getY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getY(int)"""
        return int._wrap(super(_RemoteInput, self).getY(_int.valueOf(arg0)))

    @overload
    def isKeyJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isKeyJustPressed(int)"""
        return bool._wrap(super(_RemoteInput, self).isKeyJustPressed(_int.valueOf(arg0)))

    @override
    @overload
    def getDeltaY(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getDeltaY()"""
        return int._wrap(super(RemoteInput, self).getDeltaY())

    @overload
    def __init__(self, arg0: 'RemoteInputListener'):
        """public com.badlogic.gdx.input.RemoteInput(com.badlogic.gdx.input.RemoteInput$RemoteInputListener)"""
        val = _RemoteInput(arg0)
        self.__wrapper = val

    @override
    @overload
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.input.RemoteInput.vibrate(int,int,boolean)"""
        super(_RemoteInput, self).vibrate(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def justTouched(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.justTouched()"""
        return bool._wrap(super(RemoteInput, self).justTouched())

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public void com.badlogic.gdx.input.RemoteInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        super(_RemoteInput, self).getTextInput(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getGyroscopeZ(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getGyroscopeZ()"""
        return float._wrap(super(RemoteInput, self).getGyroscopeZ())

    @override
    @overload
    def isCatchBackKey(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isCatchBackKey()"""
        return bool._wrap(super(RemoteInput, self).isCatchBackKey())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getGyroscopeY(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getGyroscopeY()"""
        return float._wrap(super(RemoteInput, self).getGyroscopeY())

    @override
    @overload
    def getGyroscopeX(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getGyroscopeX()"""
        return float._wrap(super(RemoteInput, self).getGyroscopeX())

    @override
    @overload
    def getRotation(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getRotation()"""
        return int._wrap(super(RemoteInput, self).getRotation())

    @overload
    def getDeltaX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getDeltaX(int)"""
        return int._wrap(super(_RemoteInput, self).getDeltaX(_int.valueOf(arg0)))

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.input.RemoteInput.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(_RemoteInput, self).setOnscreenKeyboardVisible(_boolean.valueOf(arg0), arg1)

    @overload
    def isButtonJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isButtonJustPressed(int)"""
        return bool._wrap(super(_RemoteInput, self).isButtonJustPressed(_int.valueOf(arg0)))

    @override
    @overload
    def getPressure(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getPressure()"""
        return float._wrap(super(RemoteInput, self).getPressure())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getDeltaY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getDeltaY(int)"""
        return int._wrap(super(_RemoteInput, self).getDeltaY(_int.valueOf(arg0)))

    @override
    @overload
    def getPitch(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getPitch()"""
        return float._wrap(super(RemoteInput, self).getPitch())

    @override
    @overload
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.input.RemoteInput.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        super(_RemoteInput, self).setInputProcessor(arg0)

    @override
    @overload
    def getRoll(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getRoll()"""
        return float._wrap(super(RemoteInput, self).getRoll())

    @override
    @overload
    def vibrate(self, arg0: 'VibrationType'):
        """public void com.badlogic.gdx.input.RemoteInput.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        super(_RemoteInput, self).vibrate(arg0)

    @override
    @overload
    def getY(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getY()"""
        return int._wrap(super(RemoteInput, self).getY()) 
 
 
# CLASS: com.badlogic.gdx.input.RemoteInput$RemoteInputListener
import com.badlogic.gdx.input.RemoteInput as _RemoteInput_RemoteInputListener
_RemoteInputListener = _RemoteInput_RemoteInputListener.RemoteInputListener
from abc import abstractmethod, ABC
 
class RemoteInputListener():
    """com.badlogic.gdx.input.RemoteInput.RemoteInputListener"""
 
    @staticmethod
    def _wrap(java_value: _RemoteInputListener) -> 'RemoteInputListener':
        return RemoteInputListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemoteInputListener):
        """
        Dynamic initializer for RemoteInputListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemoteInputListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemoteInputListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onDisconnected(self, ):
        """public abstract void com.badlogic.gdx.input.RemoteInput$RemoteInputListener.onDisconnected()"""
        pass

    @abstractmethod
    def onConnected(self, ):
        """public abstract void com.badlogic.gdx.input.RemoteInput$RemoteInputListener.onConnected()"""
        pass
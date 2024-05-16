from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.InputAdapter as __InputAdapter
__InputAdapter = __InputAdapter
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.input.GestureDetector as __GestureDetector
__GestureDetector = __GestureDetector
from builtins import int
 
class GestureDetector(pygdx.__InputAdapter, pygdx.InputAdapter):
    """com.badlogic.gdx.input.GestureDetector"""
 
    @staticmethod
    def __wrap(java_value: __GestureDetector) -> 'GestureDetector':
        return GestureDetector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GestureDetector):
        """
        Dynamic initializer for GestureDetector.
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
    def touchDragged(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDragged(float,float,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchDragged(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setTapCountInterval(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapCountInterval(float)"""
        super(__GestureDetector, self).setTapCountInterval(__float.valueOf(arg0))

    @overload
    def reset(self):
        """public void com.badlogic.gdx.input.GestureDetector.reset()"""
        super(GestureDetector, self).reset()

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def isLongPressed(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed(float)"""
        return bool.__wrap(super(__GestureDetector, self).isLongPressed(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLongPressSeconds(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setLongPressSeconds(float)"""
        super(__GestureDetector, self).setLongPressSeconds(__float.valueOf(arg0))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def touchUp(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchUp(float,float,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchUp(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setMaxFlingDelay(self, arg0: int):
        """public void com.badlogic.gdx.input.GestureDetector.setMaxFlingDelay(long)"""
        super(__GestureDetector, self).setMaxFlingDelay(__long.valueOf(arg0))

    @overload
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDown(float,float,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchDown(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyTyped(char)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).keyTyped(__char.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'GestureListener'):
        """public com.badlogic.gdx.input.GestureDetector(float,float,float,float,com.badlogic.gdx.input.GestureDetector$GestureListener)"""
        val = __GestureDetector(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setTapRectangleSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapRectangleSize(float,float)"""
        super(__GestureDetector, self).setTapRectangleSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyUp(int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).keyUp(__int.valueOf(arg0)))

    @overload
    def isLongPressed(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed()"""
        return bool.__wrap(super(GestureDetector, self).isLongPressed())

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.scrolled(float,float)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def isPanning(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isPanning()"""
        return bool.__wrap(super(GestureDetector, self).isPanning())

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapSquareSize(float)"""
        super(__GestureDetector, self).setTapSquareSize(__float.valueOf(arg0))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDragged(int,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'GestureListener'):
        """public com.badlogic.gdx.input.GestureDetector(com.badlogic.gdx.input.GestureDetector$GestureListener)"""
        val = __GestureDetector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.mouseMoved(int,int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyDown(int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).keyDown(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'GestureListener'):
        """public com.badlogic.gdx.input.GestureDetector(float,float,float,float,float,com.badlogic.gdx.input.GestureDetector$GestureListener)"""
        val = __GestureDetector(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def invalidateTapSquare(self):
        """public void com.badlogic.gdx.input.GestureDetector.invalidateTapSquare()"""
        super(GestureDetector, self).invalidateTapSquare()

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.input.GestureDetector.cancel()"""
        super(GestureDetector, self).cancel()

 
 
 
# CLASS: com.badlogic.gdx.input.GestureDetector
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.InputAdapter as __InputAdapter
__InputAdapter = __InputAdapter
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.input.GestureDetector as __GestureDetector
__GestureDetector = __GestureDetector
from builtins import int
 
class GestureDetector(pygdx.__InputAdapter, pygdx.InputAdapter):
    """com.badlogic.gdx.input.GestureDetector"""
 
    @staticmethod
    def __wrap(java_value: __GestureDetector) -> 'GestureDetector':
        return GestureDetector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GestureDetector):
        """
        Dynamic initializer for GestureDetector.
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
    def touchDragged(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDragged(float,float,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchDragged(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setTapCountInterval(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapCountInterval(float)"""
        super(__GestureDetector, self).setTapCountInterval(__float.valueOf(arg0))

    @overload
    def reset(self):
        """public void com.badlogic.gdx.input.GestureDetector.reset()"""
        super(GestureDetector, self).reset()

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def isLongPressed(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed(float)"""
        return bool.__wrap(super(__GestureDetector, self).isLongPressed(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLongPressSeconds(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setLongPressSeconds(float)"""
        super(__GestureDetector, self).setLongPressSeconds(__float.valueOf(arg0))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def touchUp(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchUp(float,float,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchUp(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setMaxFlingDelay(self, arg0: int):
        """public void com.badlogic.gdx.input.GestureDetector.setMaxFlingDelay(long)"""
        super(__GestureDetector, self).setMaxFlingDelay(__long.valueOf(arg0))

    @overload
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDown(float,float,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchDown(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyTyped(char)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).keyTyped(__char.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'GestureListener'):
        """public com.badlogic.gdx.input.GestureDetector(float,float,float,float,com.badlogic.gdx.input.GestureDetector$GestureListener)"""
        val = __GestureDetector(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setTapRectangleSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapRectangleSize(float,float)"""
        super(__GestureDetector, self).setTapRectangleSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyUp(int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).keyUp(__int.valueOf(arg0)))

    @overload
    def isLongPressed(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isLongPressed()"""
        return bool.__wrap(super(GestureDetector, self).isLongPressed())

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.scrolled(float,float)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def isPanning(self) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.isPanning()"""
        return bool.__wrap(super(GestureDetector, self).isPanning())

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.input.GestureDetector.setTapSquareSize(float)"""
        super(__GestureDetector, self).setTapSquareSize(__float.valueOf(arg0))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDragged(int,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__GestureDetector, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def __init__(self, arg0: 'GestureListener'):
        """public com.badlogic.gdx.input.GestureDetector(com.badlogic.gdx.input.GestureDetector$GestureListener)"""
        val = __GestureDetector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.mouseMoved(int,int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.InputAdapter.keyDown(int)"""
        return bool.__wrap(super(__pygdx.InputAdapter, self).keyDown(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'GestureListener'):
        """public com.badlogic.gdx.input.GestureDetector(float,float,float,float,float,com.badlogic.gdx.input.GestureDetector$GestureListener)"""
        val = __GestureDetector(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def invalidateTapSquare(self):
        """public void com.badlogic.gdx.input.GestureDetector.invalidateTapSquare()"""
        super(GestureDetector, self).invalidateTapSquare()

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.input.GestureDetector.cancel()"""
        super(GestureDetector, self).cancel()

 
 
 
# CLASS: com.badlogic.gdx.input.GestureDetector 
 
 
# CLASS: com.badlogic.gdx.input.GestureDetector$GestureAdapter
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.input.GestureDetector as __GestureDetector_GestureAdapter
__GestureAdapter = __GestureDetector_GestureAdapter.GestureAdapter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class GestureAdapter(__GestureListener, GestureListener):
    """com.badlogic.gdx.input.GestureDetector.GestureAdapter"""
 
    @staticmethod
    def __wrap(java_value: __GestureAdapter) -> 'GestureAdapter':
        return GestureAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GestureAdapter):
        """
        Dynamic initializer for GestureAdapter.
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

    @overload
    def fling(self, arg0: float, arg1: float, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.fling(float,float,int)"""
        return bool.__wrap(super(__GestureAdapter, self).fling(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def panStop(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.panStop(float,float,int,int)"""
        return bool.__wrap(super(__GestureAdapter, self).panStop(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def longPress(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.longPress(float,float)"""
        return bool.__wrap(super(__GestureAdapter, self).longPress(__float.valueOf(arg0), __float.valueOf(arg1)))

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
    def zoom(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.zoom(float,float)"""
        return bool.__wrap(super(__GestureAdapter, self).zoom(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def tap(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.tap(float,float,int,int)"""
        return bool.__wrap(super(__GestureAdapter, self).tap(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.input.GestureDetector$GestureAdapter()"""
        val = __GestureAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def pinch(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.pinch(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__GestureAdapter, self).pinch(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def pinchStop(self):
        """public void com.badlogic.gdx.input.GestureDetector$GestureAdapter.pinchStop()"""
        super(GestureAdapter, self).pinchStop()

    @overload
    def touchDown(self, arg0: float, arg1: float, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.touchDown(float,float,int,int)"""
        return bool.__wrap(super(__GestureAdapter, self).touchDown(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.input.GestureDetector$GestureAdapter()"""
        val = __GestureAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def pan(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.input.GestureDetector$GestureAdapter.pan(float,float,float,float)"""
        return bool.__wrap(super(__GestureAdapter, self).pan(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.input.RemoteSender
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.input.RemoteSender as __RemoteSender
__RemoteSender = __RemoteSender
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RemoteSender(pygdx.__InputProcessor, pygdx.InputProcessor):
    """com.badlogic.gdx.input.RemoteSender"""
 
    @staticmethod
    def __wrap(java_value: __RemoteSender) -> 'RemoteSender':
        return RemoteSender(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemoteSender):
        """
        Dynamic initializer for RemoteSender.
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

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__RemoteSender, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__RemoteSender, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public com.badlogic.gdx.input.RemoteSender(java.lang.String,int)"""
        val = __RemoteSender(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def sendUpdate(self):
        """public void com.badlogic.gdx.input.RemoteSender.sendUpdate()"""
        super(RemoteSender, self).sendUpdate()

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchDragged(int,int,int)"""
        return bool.__wrap(super(__RemoteSender, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.scrolled(float,float)"""
        return bool.__wrap(super(__RemoteSender, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.mouseMoved(int,int)"""
        return bool.__wrap(super(__RemoteSender, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.keyUp(int)"""
        return bool.__wrap(super(__RemoteSender, self).keyUp(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__RemoteSender, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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
    def isConnected(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.isConnected()"""
        return bool.__wrap(super(RemoteSender, self).isConnected())

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.keyTyped(char)"""
        return bool.__wrap(super(__RemoteSender, self).keyTyped(__char.valueOf(arg0)))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteSender.keyDown(int)"""
        return bool.__wrap(super(__RemoteSender, self).keyDown(__int.valueOf(arg0)))

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
 
 
# CLASS: com.badlogic.gdx.input.RemoteInput
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
import com.badlogic.gdx.Input as __Input_Orientation
__Orientation = __Input_Orientation.Orientation
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.InputProcessor as __InputProcessor
__InputProcessor = __InputProcessor
from typing import List
import com.badlogic.gdx.input.RemoteInput as __RemoteInput
__RemoteInput = __RemoteInput
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RemoteInput(__Runnable, Runnable, pygdx.__Input, pygdx.Input):
    """com.badlogic.gdx.input.RemoteInput"""
 
    @staticmethod
    def __wrap(java_value: __RemoteInput) -> 'RemoteInput':
        return RemoteInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemoteInput):
        """
        Dynamic initializer for RemoteInput.
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
    def setCatchKey(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setCatchKey(int,boolean)"""
        super(__RemoteInput, self).setCatchKey(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def getRoll(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getRoll()"""
        return float.__wrap(super(RemoteInput, self).getRoll())

    @override
    @overload
    def getMaxPointers(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getMaxPointers()"""
        return int.__wrap(super(RemoteInput, self).getMaxPointers())

    @overload
    def getX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getX(int)"""
        return int.__wrap(super(__RemoteInput, self).getX(__int.valueOf(arg0)))

    @override
    @overload
    def getAccelerometerY(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getAccelerometerY()"""
        return float.__wrap(super(RemoteInput, self).getAccelerometerY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'RemoteInputListener'):
        """public com.badlogic.gdx.input.RemoteInput(com.badlogic.gdx.input.RemoteInput$RemoteInputListener)"""
        val = __RemoteInput(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isKeyJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isKeyJustPressed(int)"""
        return bool.__wrap(super(__RemoteInput, self).isKeyJustPressed(__int.valueOf(arg0)))

    @overload
    def isKeyPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isKeyPressed(int)"""
        return bool.__wrap(super(__RemoteInput, self).isKeyPressed(__int.valueOf(arg0)))

    @overload
    def getPressure(self, arg0: int) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getPressure(int)"""
        return float.__wrap(super(__RemoteInput, self).getPressure(__int.valueOf(arg0)))

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.input.RemoteInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(__RemoteInput, self).getTextInput(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getAccelerometerX(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getAccelerometerX()"""
        return float.__wrap(super(RemoteInput, self).getAccelerometerX())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.input.RemoteInput()"""
        val = __RemoteInput()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.input.RemoteInput.vibrate(int,int,boolean)"""
        super(__RemoteInput, self).vibrate(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getAzimuth(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getAzimuth()"""
        return float.__wrap(super(RemoteInput, self).getAzimuth())

    @overload
    def isPeripheralAvailable(self, arg0: 'Peripheral') -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        return bool.__wrap(super(__RemoteInput, self).isPeripheralAvailable(arg0))

    @overload
    def getDeltaX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getDeltaX(int)"""
        return int.__wrap(super(__RemoteInput, self).getDeltaX(__int.valueOf(arg0)))

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public void com.badlogic.gdx.input.RemoteInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        super(__RemoteInput, self).getTextInput(arg0, arg1, arg2, arg3)

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.input.RemoteInput.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(__RemoteInput, self).setOnscreenKeyboardVisible(__boolean.valueOf(arg0), arg1)

    @override
    @overload
    def getInputProcessor(self) -> 'pygdx.InputProcessor':
        """public com.badlogic.gdx.InputProcessor com.badlogic.gdx.input.RemoteInput.getInputProcessor()"""
        return 'pygdx.InputProcessor'.__wrap(super(RemoteInput, self).getInputProcessor())

    @override
    @overload
    def isCursorCatched(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isCursorCatched()"""
        return bool.__wrap(super(RemoteInput, self).isCursorCatched())

    @override
    @overload
    def getRotation(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getRotation()"""
        return int.__wrap(super(RemoteInput, self).getRotation())

    @override
    @overload
    def getX(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getX()"""
        return int.__wrap(super(RemoteInput, self).getX())

    @overload
    def __init__(self, arg0: int, arg1: 'RemoteInputListener'):
        """public com.badlogic.gdx.input.RemoteInput(int,com.badlogic.gdx.input.RemoteInput$RemoteInputListener)"""
        val = __RemoteInput(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getIPs(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.input.RemoteInput.getIPs()"""
        return List[str].__wrap(super(RemoteInput, self).getIPs())

    @overload
    def isButtonPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isButtonPressed(int)"""
        return bool.__wrap(super(__RemoteInput, self).isButtonPressed(__int.valueOf(arg0)))

    @override
    @overload
    def vibrate(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.input.RemoteInput.vibrate(int,boolean)"""
        super(__RemoteInput, self).vibrate(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def getGyroscopeX(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getGyroscopeX()"""
        return float.__wrap(super(RemoteInput, self).getGyroscopeX())

    @overload
    def isTouched(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isTouched(int)"""
        return bool.__wrap(super(__RemoteInput, self).isTouched(__int.valueOf(arg0)))

    @overload
    def isButtonJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isButtonJustPressed(int)"""
        return bool.__wrap(super(__RemoteInput, self).isButtonJustPressed(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isTouched(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isTouched()"""
        return bool.__wrap(super(RemoteInput, self).isTouched())

    @override
    @overload
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.input.RemoteInput.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        super(__RemoteInput, self).setInputProcessor(arg0)

    @override
    @overload
    def setCatchMenuKey(self, arg0: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setCatchMenuKey(boolean)"""
        super(__RemoteInput, self).setCatchMenuKey(__boolean.valueOf(arg0))

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.input.RemoteInput.run()"""
        super(RemoteInput, self).run()

    @overload
    def isCatchKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isCatchKey(int)"""
        return bool.__wrap(super(__RemoteInput, self).isCatchKey(__int.valueOf(arg0)))

    @override
    @overload
    def isCatchMenuKey(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isCatchMenuKey()"""
        return bool.__wrap(super(RemoteInput, self).isCatchMenuKey())

    @override
    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.input.RemoteInput.setCursorPosition(int,int)"""
        super(__RemoteInput, self).setCursorPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def vibrate(self, arg0: int):
        """public void com.badlogic.gdx.input.RemoteInput.vibrate(int)"""
        super(__RemoteInput, self).vibrate(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.input.RemoteInput()"""
        val = __RemoteInput()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getGyroscopeZ(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getGyroscopeZ()"""
        return float.__wrap(super(RemoteInput, self).getGyroscopeZ())

    @override
    @overload
    def setCursorCatched(self, arg0: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setCursorCatched(boolean)"""
        super(__RemoteInput, self).setCursorCatched(__boolean.valueOf(arg0))

    @override
    @overload
    def justTouched(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.justTouched()"""
        return bool.__wrap(super(RemoteInput, self).justTouched())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getPressure(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getPressure()"""
        return float.__wrap(super(RemoteInput, self).getPressure())

    @override
    @overload
    def getGyroscopeY(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getGyroscopeY()"""
        return float.__wrap(super(RemoteInput, self).getGyroscopeY())

    @override
    @overload
    def getCurrentEventTime(self) -> int:
        """public long com.badlogic.gdx.input.RemoteInput.getCurrentEventTime()"""
        return int.__wrap(super(RemoteInput, self).getCurrentEventTime())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.input.RemoteInput(int)"""
        val = __RemoteInput(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def vibrate(self, arg0: 'VibrationType'):
        """public void com.badlogic.gdx.input.RemoteInput.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        super(__RemoteInput, self).vibrate(arg0)

    @override
    @overload
    def getAccelerometerZ(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getAccelerometerZ()"""
        return float.__wrap(super(RemoteInput, self).getAccelerometerZ())

    @override
    @overload
    def getRotationMatrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.input.RemoteInput.getRotationMatrix(float[])"""
        super(__RemoteInput, self).getRotationMatrix(arg0)

    @overload
    def isConnected(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isConnected()"""
        return bool.__wrap(super(RemoteInput, self).isConnected())

    @override
    @overload
    def getY(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getY()"""
        return int.__wrap(super(RemoteInput, self).getY())

    @overload
    def getDeltaY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getDeltaY(int)"""
        return int.__wrap(super(__RemoteInput, self).getDeltaY(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getPitch(self) -> float:
        """public float com.badlogic.gdx.input.RemoteInput.getPitch()"""
        return float.__wrap(super(RemoteInput, self).getPitch())

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setOnscreenKeyboardVisible(boolean)"""
        super(__RemoteInput, self).setOnscreenKeyboardVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def isCatchBackKey(self) -> bool:
        """public boolean com.badlogic.gdx.input.RemoteInput.isCatchBackKey()"""
        return bool.__wrap(super(RemoteInput, self).isCatchBackKey())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getNativeOrientation(self) -> 'pygdx.Input$Orientation':
        """public com.badlogic.gdx.Input$Orientation com.badlogic.gdx.input.RemoteInput.getNativeOrientation()"""
        return 'pygdx.Input$Orientation'.__wrap(super(RemoteInput, self).getNativeOrientation())

    @overload
    def getY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getY(int)"""
        return int.__wrap(super(__RemoteInput, self).getY(__int.valueOf(arg0)))

    @override
    @overload
    def getDeltaX(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getDeltaX()"""
        return int.__wrap(super(RemoteInput, self).getDeltaX())

    @override
    @overload
    def setCatchBackKey(self, arg0: bool):
        """public void com.badlogic.gdx.input.RemoteInput.setCatchBackKey(boolean)"""
        super(__RemoteInput, self).setCatchBackKey(__boolean.valueOf(arg0))

    @override
    @overload
    def getDeltaY(self) -> int:
        """public int com.badlogic.gdx.input.RemoteInput.getDeltaY()"""
        return int.__wrap(super(RemoteInput, self).getDeltaY()) 
 
 
# CLASS: com.badlogic.gdx.input.RemoteInput$RemoteInputListener
import com.badlogic.gdx.input.RemoteInput as __RemoteInput_RemoteInputListener
__RemoteInputListener = __RemoteInput_RemoteInputListener.RemoteInputListener
from abc import abstractmethod, ABC
 
class RemoteInputListener(ABC):
    """com.badlogic.gdx.input.RemoteInput.RemoteInputListener"""
 
    @staticmethod
    def __wrap(java_value: __RemoteInputListener) -> 'RemoteInputListener':
        return RemoteInputListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemoteInputListener):
        """
        Dynamic initializer for RemoteInputListener.
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
    def onDisconnected(self, ):
        """public abstract void com.badlogic.gdx.input.RemoteInput$RemoteInputListener.onDisconnected()"""
        pass

    @abstractmethod
    def onConnected(self, ):
        """public abstract void com.badlogic.gdx.input.RemoteInput$RemoteInputListener.onConnected()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.input.GestureDetector$GestureListener
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.input.GestureDetector as __GestureDetector_GestureListener
__GestureListener = __GestureDetector_GestureListener.GestureListener
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

 
class GestureListener(ABC):
    """com.badlogic.gdx.input.GestureDetector.GestureListener"""
 
    @staticmethod
    def __wrap(java_value: __GestureListener) -> 'GestureListener':
        return GestureListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GestureListener):
        """
        Dynamic initializer for GestureListener.
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
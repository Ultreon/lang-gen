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
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.InputListener as _InputListener
_InputListener = _InputListener
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InputListener():
    """com.badlogic.gdx.scenes.scene2d.InputListener"""
 
    @staticmethod
    def _wrap(java_value: _InputListener) -> 'InputListener':
        return InputListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InputListener):
        """
        Dynamic initializer for InputListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InputListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InputListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.InputListener()"""
        val = _InputListener()
        self.__wrapper = val

    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_InputListener, self).touchDragged(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.InputListener()"""
        val = _InputListener()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_InputListener, self).keyUp(arg0, _int.valueOf(arg1)))

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool._wrap(super(_InputListener, self).touchDown(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_InputListener, self).handle(arg0))

    @overload
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_InputListener, self).exit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_InputListener, self).enter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_InputListener, self).touchUp(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_InputListener, self).keyDown(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool._wrap(super(_InputListener, self).mouseMoved(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool._wrap(super(_InputListener, self).scrolled(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool._wrap(super(_InputListener, self).keyTyped(arg0, _char.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.InputListener
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
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.InputListener as _InputListener
_InputListener = _InputListener
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InputListener():
    """com.badlogic.gdx.scenes.scene2d.InputListener"""
 
    @staticmethod
    def _wrap(java_value: _InputListener) -> 'InputListener':
        return InputListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InputListener):
        """
        Dynamic initializer for InputListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InputListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InputListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.InputListener()"""
        val = _InputListener()
        self.__wrapper = val

    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_InputListener, self).touchDragged(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.InputListener()"""
        val = _InputListener()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_InputListener, self).keyUp(arg0, _int.valueOf(arg1)))

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool._wrap(super(_InputListener, self).touchDown(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_InputListener, self).handle(arg0))

    @overload
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_InputListener, self).exit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_InputListener, self).enter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_InputListener, self).touchUp(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_InputListener, self).keyDown(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool._wrap(super(_InputListener, self).mouseMoved(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool._wrap(super(_InputListener, self).scrolled(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool._wrap(super(_InputListener, self).keyTyped(arg0, _char.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.InputListener 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.InputEvent$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.InputEvent as _InputEvent_Type
_Type = _InputEvent_Type.Type
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
 
class Type():
    """com.badlogic.gdx.scenes.scene2d.InputEvent.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.gdx.scenes.scene2d.InputEvent$Type com.badlogic.gdx.scenes.scene2d.InputEvent$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

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
    def values() -> List['Type']:
        """public static com.badlogic.gdx.scenes.scene2d.InputEvent$Type[] com.badlogic.gdx.scenes.scene2d.InputEvent$Type.values()"""
        return List[Type]._wrap(_Type.values()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Actor
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.scenes.scene2d.Touchable as _Touchable
_Touchable = _Touchable
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Stage as _Stage
_Stage = _Stage
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.scenes.scene2d.Group as _Group
_Group = _Group
import java.lang.String as _string
import com.badlogic.gdx.utils.DelayedRemovalArray as _DelayedRemovalArray
_DelayedRemovalArray = _DelayedRemovalArray
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Actor():
    """com.badlogic.gdx.scenes.scene2d.Actor"""
 
    @staticmethod
    def _wrap(java_value: _Actor) -> 'Actor':
        return Actor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Actor):
        """
        Dynamic initializer for Actor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Actor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Actor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def hasActions(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasActions()"""
        return bool._wrap(super(Actor, self).hasActions())

    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setVisible(boolean)"""
        super(_Actor, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def getTop(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getTop()"""
        return float._wrap(super(Actor, self).getTop())

    @overload
    def fire(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.fire(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_Actor, self).fire(arg0))

    @overload
    def localToScreenCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToScreenCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToScreenCoordinates(arg0))

    @overload
    def removeListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Actor, self).removeListener(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def screenToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.screenToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).screenToLocalCoordinates(arg0))

    @overload
    def clipEnd(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clipEnd()"""
        super(Actor, self).clipEnd()

    @overload
    def getY(self, arg0: int) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getY(int)"""
        return float._wrap(super(_Actor, self).getY(_int.valueOf(arg0)))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getRotation()"""
        return float._wrap(super(Actor, self).getRotation())

    @overload
    def firstAscendant(self, arg0: 'Class') -> 'Actor':
        """public <T extends com.badlogic.gdx.scenes.scene2d.Actor> T com.badlogic.gdx.scenes.scene2d.Actor.firstAscendant(java.lang.Class<T>)"""
        return 'Actor'._wrap(super(_Actor, self).firstAscendant(arg0))

    @overload
    def ancestorsVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.ancestorsVisible()"""
        return bool._wrap(super(Actor, self).ancestorsVisible())

    @overload
    def isDescendantOf(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isDescendantOf(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool._wrap(super(_Actor, self).isDescendantOf(arg0))

    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setBounds(float,float,float,float)"""
        super(_Actor, self).setBounds(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getX()"""
        return float._wrap(super(Actor, self).getX())

    @overload
    def sizeBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.sizeBy(float)"""
        super(_Actor, self).sizeBy(_float.valueOf(arg0))

    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isVisible()"""
        return bool._wrap(super(Actor, self).isVisible())

    @overload
    def remove(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.remove()"""
        return bool._wrap(super(Actor, self).remove())

    @overload
    def isTouchFocusTarget(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchFocusTarget()"""
        return bool._wrap(super(Actor, self).isTouchFocusTarget())

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

    @overload
    def getListeners(self) -> 'utils.DelayedRemovalArray':
        """public com.badlogic.gdx.utils.DelayedRemovalArray<com.badlogic.gdx.scenes.scene2d.EventListener> com.badlogic.gdx.scenes.scene2d.Actor.getListeners()"""
        return 'utils.DelayedRemovalArray'._wrap(super(Actor, self).getListeners())

    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScaleY(float)"""
        super(_Actor, self).setScaleY(_float.valueOf(arg0))

    @overload
    def drawDebug(self, arg0: 'ShapeRenderer'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.drawDebug(com.badlogic.gdx.graphics.glutils.ShapeRenderer)"""
        super(_Actor, self).drawDebug(arg0)

    @overload
    def setY(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setY(float,int)"""
        super(_Actor, self).setY(_float.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setPosition(float,float)"""
        super(_Actor, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setRotation(float)"""
        super(_Actor, self).setRotation(_float.valueOf(arg0))

    @overload
    def parentToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.parentToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).parentToLocalCoordinates(arg0))

    @overload
    def scaleBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.scaleBy(float)"""
        super(_Actor, self).scaleBy(_float.valueOf(arg0))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getHeight()"""
        return float._wrap(super(Actor, self).getHeight())

    @overload
    def getRight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getRight()"""
        return float._wrap(super(Actor, self).getRight())

    @overload
    def setDebug(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setDebug(boolean)"""
        super(_Actor, self).setDebug(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Actor()"""
        val = _Actor()
        self.__wrapper = val

    @overload
    def setWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setWidth(float)"""
        super(_Actor, self).setWidth(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Actor, self).setColor(arg0)

    @overload
    def isAscendantOf(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isAscendantOf(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool._wrap(super(_Actor, self).isAscendantOf(arg0))

    @overload
    def setOrigin(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOrigin(int)"""
        super(_Actor, self).setOrigin(_int.valueOf(arg0))

    @overload
    def hasScrollFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasScrollFocus()"""
        return bool._wrap(super(Actor, self).hasScrollFocus())

    @overload
    def scaleBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.scaleBy(float,float)"""
        super(_Actor, self).scaleBy(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Actor.toString()"""
        return str._wrap(super(Actor, self).toString())

    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOriginX(float)"""
        super(_Actor, self).setOriginX(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setZIndex(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.setZIndex(int)"""
        return bool._wrap(super(_Actor, self).setZIndex(_int.valueOf(arg0)))

    @overload
    def localToStageCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToStageCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToStageCoordinates(arg0))

    @overload
    def toBack(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.toBack()"""
        super(Actor, self).toBack()

    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_Actor, self).addAction(arg0)

    @overload
    def setHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setHeight(float)"""
        super(_Actor, self).setHeight(_float.valueOf(arg0))

    @overload
    def removeAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.removeAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_Actor, self).removeAction(arg0)

    @overload
    def clipBegin(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.clipBegin()"""
        return bool._wrap(super(Actor, self).clipBegin())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Actor()"""
        val = _Actor()
        self.__wrapper = val

    @overload
    def toFront(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.toFront()"""
        super(Actor, self).toFront()

    @overload
    def stageToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.stageToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).stageToLocalCoordinates(arg0))

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
    def getTouchable(self) -> 'Touchable':
        """public com.badlogic.gdx.scenes.scene2d.Touchable com.badlogic.gdx.scenes.scene2d.Actor.getTouchable()"""
        return 'Touchable'._wrap(super(Actor, self).getTouchable())

    @overload
    def getCaptureListeners(self) -> 'utils.DelayedRemovalArray':
        """public com.badlogic.gdx.utils.DelayedRemovalArray<com.badlogic.gdx.scenes.scene2d.EventListener> com.badlogic.gdx.scenes.scene2d.Actor.getCaptureListeners()"""
        return 'utils.DelayedRemovalArray'._wrap(super(Actor, self).getCaptureListeners())

    @overload
    def getX(self, arg0: int) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getX(int)"""
        return float._wrap(super(_Actor, self).getX(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setName(java.lang.String)"""
        super(_Actor, self).setName(arg0)

    @overload
    def addListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.addListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Actor, self).addListener(arg0))

    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clearListeners()"""
        super(Actor, self).clearListeners()

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(_Actor, self).draw(arg0, _float.valueOf(arg1))

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScale(float)"""
        super(_Actor, self).setScale(_float.valueOf(arg0))

    @overload
    def setUserObject(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setUserObject(java.lang.Object)"""
        super(_Actor, self).setUserObject(arg0)

    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setSize(float,float)"""
        super(_Actor, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def sizeBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.sizeBy(float,float)"""
        super(_Actor, self).sizeBy(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setY(float)"""
        super(_Actor, self).setY(_float.valueOf(arg0))

    @overload
    def clearActions(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clearActions()"""
        super(Actor, self).clearActions()

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Actor.getName()"""
        return str._wrap(super(Actor, self).getName())

    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScaleX(float)"""
        super(_Actor, self).setScaleX(_float.valueOf(arg0))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getWidth()"""
        return float._wrap(super(Actor, self).getWidth())

    @overload
    def hasParent(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasParent()"""
        return bool._wrap(super(Actor, self).hasParent())

    @overload
    def rotateBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.rotateBy(float)"""
        super(_Actor, self).rotateBy(_float.valueOf(arg0))

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOrigin(float,float)"""
        super(_Actor, self).setOrigin(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def moveBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.moveBy(float,float)"""
        super(_Actor, self).moveBy(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def notify(self, arg0: 'Event', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.notify(com.badlogic.gdx.scenes.scene2d.Event,boolean)"""
        return bool._wrap(super(_Actor, self).notify(arg0, _boolean.valueOf(arg1)))

    @overload
    def debug(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Actor.debug()"""
        return 'Actor'._wrap(super(Actor, self).debug())

    @overload
    def hasKeyboardFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasKeyboardFocus()"""
        return bool._wrap(super(Actor, self).hasKeyboardFocus())

    @overload
    def isTouchFocusListener(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchFocusListener()"""
        return bool._wrap(super(Actor, self).isTouchFocusListener())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clear()"""
        super(Actor, self).clear()

    @overload
    def getDebug(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.getDebug()"""
        return bool._wrap(super(Actor, self).getDebug())

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setX(float)"""
        super(_Actor, self).setX(_float.valueOf(arg0))

    @overload
    def getUserObject(self) -> object:
        """public java.lang.Object com.badlogic.gdx.scenes.scene2d.Actor.getUserObject()"""
        return object._wrap(super(Actor, self).getUserObject())

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getOriginX()"""
        return float._wrap(super(Actor, self).getOriginX())

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getScaleY()"""
        return float._wrap(super(Actor, self).getScaleY())

    @overload
    def act(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.act(float)"""
        super(_Actor, self).act(_float.valueOf(arg0))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getY()"""
        return float._wrap(super(Actor, self).getY())

    @overload
    def getParent(self) -> 'Group':
        """public com.badlogic.gdx.scenes.scene2d.Group com.badlogic.gdx.scenes.scene2d.Actor.getParent()"""
        return 'Group'._wrap(super(Actor, self).getParent())

    @overload
    def hit(self, arg0: float, arg1: float, arg2: bool) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Actor.hit(float,float,boolean)"""
        return 'Actor'._wrap(super(_Actor, self).hit(_float.valueOf(arg0), _float.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def getStage(self) -> 'Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Actor.getStage()"""
        return 'Stage'._wrap(super(Actor, self).getStage())

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setPosition(float,float,int)"""
        super(_Actor, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def removeCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.removeCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Actor, self).removeCaptureListener(arg0))

    @overload
    def getActions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Action> com.badlogic.gdx.scenes.scene2d.Actor.getActions()"""
        return 'utils.Array'._wrap(super(Actor, self).getActions())

    @overload
    def clipBegin(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.clipBegin(float,float,float,float)"""
        return bool._wrap(super(_Actor, self).clipBegin(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setColor(float,float,float,float)"""
        super(_Actor, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.Actor.getColor()"""
        return 'graphics.Color'._wrap(super(Actor, self).getColor())

    @overload
    def addCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.addCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Actor, self).addCaptureListener(arg0))

    @overload
    def ascendantsVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.ascendantsVisible()"""
        return bool._wrap(super(Actor, self).ascendantsVisible())

    @overload
    def localToActorCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToActorCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToActorCoordinates(arg0, arg1))

    @overload
    def localToParentCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToParentCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToParentCoordinates(arg0))

    @overload
    def localToAscendantCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToAscendantCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToAscendantCoordinates(arg0, arg1))

    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOriginY(float)"""
        super(_Actor, self).setOriginY(_float.valueOf(arg0))

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getScaleX()"""
        return float._wrap(super(Actor, self).getScaleX())

    @overload
    def isTouchable(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchable()"""
        return bool._wrap(super(Actor, self).isTouchable())

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScale(float,float)"""
        super(_Actor, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getOriginY()"""
        return float._wrap(super(Actor, self).getOriginY())

    @overload
    def setX(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setX(float,int)"""
        super(_Actor, self).setX(_float.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getZIndex(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.Actor.getZIndex()"""
        return int._wrap(super(Actor, self).getZIndex())

    @overload
    def setTouchable(self, arg0: 'Touchable'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setTouchable(com.badlogic.gdx.scenes.scene2d.Touchable)"""
        super(_Actor, self).setTouchable(arg0) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Stage
from pyquantum_helper import import_once as _import_once
import java.lang.Character as _char
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.scenes.scene2d.Stage as _Stage
_Stage = _Stage
import com.badlogic.gdx.utils.viewport.Viewport as _Viewport
_Viewport = _Viewport
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.scenes.scene2d.Group as _Group
_Group = _Group
import java.lang.Boolean as _boolean
try:
    from pygdx.utils import viewport
except ImportError:
    viewport = _import_once("pygdx.utils.viewport")

try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx.scenes.scene2d import ui
except ImportError:
    ui = _import_once("pygdx.scenes.scene2d.ui")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Stage():
    """com.badlogic.gdx.scenes.scene2d.Stage"""
 
    @staticmethod
    def _wrap(java_value: _Stage) -> 'Stage':
        return Stage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Stage):
        """
        Dynamic initializer for Stage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Stage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Stage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setDebugParentUnderMouse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugParentUnderMouse(boolean)"""
        super(_Stage, self).setDebugParentUnderMouse(_boolean.valueOf(arg0))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Stage.getHeight()"""
        return float._wrap(super(Stage, self).getHeight())

    @overload
    def setDebugUnderMouse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugUnderMouse(boolean)"""
        super(_Stage, self).setDebugUnderMouse(_boolean.valueOf(arg0))

    @overload
    def act(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.act(float)"""
        super(_Stage, self).act(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.keyDown(int)"""
        return bool._wrap(super(_Stage, self).keyDown(_int.valueOf(arg0)))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.clear()"""
        super(Stage, self).clear()

    @overload
    def hit(self, arg0: float, arg1: float, arg2: bool) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Stage.hit(float,float,boolean)"""
        return 'Actor'._wrap(super(_Stage, self).hit(_float.valueOf(arg0), _float.valueOf(arg1), _boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setActionsRequestRendering(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setActionsRequestRendering(boolean)"""
        super(_Stage, self).setActionsRequestRendering(_boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Stage()"""
        val = _Stage()
        self.__wrapper = val

    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_Stage, self).addAction(arg0)

    @overload
    def setDebugInvisible(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugInvisible(boolean)"""
        super(_Stage, self).setDebugInvisible(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Viewport', arg1: 'Batch'):
        """public com.badlogic.gdx.scenes.scene2d.Stage(com.badlogic.gdx.utils.viewport.Viewport,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _Stage(arg0, arg1)
        self.__wrapper = val

    @overload
    def unfocusAll(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.unfocusAll()"""
        super(Stage, self).unfocusAll()

    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.scenes.scene2d.Stage.getBatch()"""
        return 'g2d.Batch'._wrap(super(Stage, self).getBatch())

    @overload
    def getRoot(self) -> 'Group':
        """public com.badlogic.gdx.scenes.scene2d.Group com.badlogic.gdx.scenes.scene2d.Stage.getRoot()"""
        return 'Group'._wrap(super(Stage, self).getRoot())

    @overload
    def addCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.addCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Stage, self).addCaptureListener(arg0))

    @overload
    def addTouchFocus(self, arg0: 'EventListener', arg1: 'Actor', arg2: 'Actor', arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.addTouchFocus(com.badlogic.gdx.scenes.scene2d.EventListener,com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor,int,int)"""
        super(_Stage, self).addTouchFocus(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def setRoot(self, arg0: 'Group'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setRoot(com.badlogic.gdx.scenes.scene2d.Group)"""
        super(_Stage, self).setRoot(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Viewport'):
        """public com.badlogic.gdx.scenes.scene2d.Stage(com.badlogic.gdx.utils.viewport.Viewport)"""
        val = _Stage(arg0)
        self.__wrapper = val

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.keyTyped(char)"""
        return bool._wrap(super(_Stage, self).keyTyped(_char.valueOf(arg0)))

    @overload
    def isDebugAll(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.isDebugAll()"""
        return bool._wrap(super(Stage, self).isDebugAll())

    @overload
    def getViewport(self) -> 'viewport.Viewport':
        """public com.badlogic.gdx.utils.viewport.Viewport com.badlogic.gdx.scenes.scene2d.Stage.getViewport()"""
        return 'viewport.Viewport'._wrap(super(Stage, self).getViewport())

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.touchUp(int,int,int,int)"""
        return bool._wrap(super(_Stage, self).touchUp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.touchCancelled(int,int,int,int)"""
        return bool._wrap(super(_Stage, self).touchCancelled(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def getActionsRequestRendering(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.getActionsRequestRendering()"""
        return bool._wrap(super(Stage, self).getActionsRequestRendering())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Stage()"""
        val = _Stage()
        self.__wrapper = val

    @overload
    def removeListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Stage, self).removeListener(arg0))

    @overload
    def removeTouchFocus(self, arg0: 'EventListener', arg1: 'Actor', arg2: 'Actor', arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.removeTouchFocus(com.badlogic.gdx.scenes.scene2d.EventListener,com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor,int,int)"""
        super(_Stage, self).removeTouchFocus(arg0, arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.scrolled(float,float)"""
        return bool._wrap(super(_Stage, self).scrolled(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def cancelTouchFocus(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.cancelTouchFocus(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Stage, self).cancelTouchFocus(arg0)

    @overload
    def cancelTouchFocusExcept(self, arg0: 'EventListener', arg1: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.cancelTouchFocusExcept(com.badlogic.gdx.scenes.scene2d.EventListener,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Stage, self).cancelTouchFocusExcept(arg0, arg1)

    @overload
    def screenToStageCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Stage.screenToStageCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Stage, self).screenToStageCoordinates(arg0))

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.keyUp(int)"""
        return bool._wrap(super(_Stage, self).keyUp(_int.valueOf(arg0)))

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.mouseMoved(int,int)"""
        return bool._wrap(super(_Stage, self).mouseMoved(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def calculateScissors(self, arg0: 'Rectangle', arg1: 'Rectangle'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.calculateScissors(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(_Stage, self).calculateScissors(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getActors(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Actor> com.badlogic.gdx.scenes.scene2d.Stage.getActors()"""
        return 'utils.Array'._wrap(super(Stage, self).getActors())

    @overload
    def setViewport(self, arg0: 'Viewport'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setViewport(com.badlogic.gdx.utils.viewport.Viewport)"""
        super(_Stage, self).setViewport(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def stageToScreenCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Stage.stageToScreenCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Stage, self).stageToScreenCoordinates(arg0))

    @overload
    def setDebugTableUnderMouse(self, arg0: 'Debug'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugTableUnderMouse(com.badlogic.gdx.scenes.scene2d.ui.Table$Debug)"""
        super(_Stage, self).setDebugTableUnderMouse(arg0)

    @overload
    def addActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.addActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Stage, self).addActor(arg0)

    @overload
    def removeCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.removeCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Stage, self).removeCaptureListener(arg0))

    @overload
    def act(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.act()"""
        super(Stage, self).act()

    @overload
    def cancelTouchFocus(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.cancelTouchFocus()"""
        super(Stage, self).cancelTouchFocus()

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Stage.getWidth()"""
        return float._wrap(super(Stage, self).getWidth())

    @overload
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Stage.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'._wrap(super(_Stage, self).toScreenCoordinates(arg0, arg1))

    @overload
    def draw(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.draw()"""
        super(Stage, self).draw()

    @overload
    def setDebugTableUnderMouse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugTableUnderMouse(boolean)"""
        super(_Stage, self).setDebugTableUnderMouse(_boolean.valueOf(arg0))

    @overload
    def setScrollFocus(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.setScrollFocus(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool._wrap(super(_Stage, self).setScrollFocus(arg0))

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.scenes.scene2d.Stage.getCamera()"""
        return 'graphics.Camera'._wrap(super(Stage, self).getCamera())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.dispose()"""
        super(Stage, self).dispose()

    @overload
    def getKeyboardFocus(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Stage.getKeyboardFocus()"""
        return 'Actor'._wrap(super(Stage, self).getKeyboardFocus())

    @overload
    def getScrollFocus(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Stage.getScrollFocus()"""
        return 'Actor'._wrap(super(Stage, self).getScrollFocus())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def unfocus(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.unfocus(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Stage, self).unfocus(arg0)

    @overload
    def setDebugAll(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugAll(boolean)"""
        super(_Stage, self).setDebugAll(_boolean.valueOf(arg0))

    @overload
    def addListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.addListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Stage, self).addListener(arg0))

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.touchDown(int,int,int,int)"""
        return bool._wrap(super(_Stage, self).touchDown(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def getDebugColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.Stage.getDebugColor()"""
        return 'graphics.Color'._wrap(super(Stage, self).getDebugColor())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.touchDragged(int,int,int)"""
        return bool._wrap(super(_Stage, self).touchDragged(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def setKeyboardFocus(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.setKeyboardFocus(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool._wrap(super(_Stage, self).setKeyboardFocus(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.EventListener
import com.badlogic.gdx.scenes.scene2d.EventListener as _EventListener
_EventListener = _EventListener
from abc import abstractmethod, ABC
 
class EventListener():
    """com.badlogic.gdx.scenes.scene2d.EventListener"""
 
    @staticmethod
    def _wrap(java_value: _EventListener) -> 'EventListener':
        return EventListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventListener):
        """
        Dynamic initializer for EventListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def handle(self, arg0: 'Event'):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.EventListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.InputEvent
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.scenes.scene2d.Stage as _Stage
_Stage = _Stage
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.InputEvent as _InputEvent_Type
_Type = _InputEvent_Type.Type
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.Event as _Event
_Event = _Event
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.scenes.scene2d.InputEvent as _InputEvent
_InputEvent = _InputEvent
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InputEvent():
    """com.badlogic.gdx.scenes.scene2d.InputEvent"""
 
    @staticmethod
    def _wrap(java_value: _InputEvent) -> 'InputEvent':
        return InputEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InputEvent):
        """
        Dynamic initializer for InputEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InputEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InputEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setScrollAmountY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setScrollAmountY(float)"""
        super(_InputEvent, self).setScrollAmountY(_float.valueOf(arg0))

    @overload
    def getCharacter(self) -> str:
        """public char com.badlogic.gdx.scenes.scene2d.InputEvent.getCharacter()"""
        return str._wrap(super(InputEvent, self).getCharacter())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.InputEvent.toString()"""
        return str._wrap(super(InputEvent, self).toString())

    @override
    @overload
    def setListenerActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setListenerActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Event, self).setListenerActor(arg0)

    @overload
    def getScrollAmountY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.InputEvent.getScrollAmountY()"""
        return float._wrap(super(InputEvent, self).getScrollAmountY())

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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Event, self).setTarget(arg0)

    @overload
    def setPointer(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setPointer(int)"""
        super(_InputEvent, self).setPointer(_int.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.InputEvent()"""
        val = _InputEvent()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getPointer(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.InputEvent.getPointer()"""
        return int._wrap(super(InputEvent, self).getPointer())

    @overload
    def getButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.InputEvent.getButton()"""
        return int._wrap(super(InputEvent, self).getButton())

    @overload
    def getStageX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.InputEvent.getStageX()"""
        return float._wrap(super(InputEvent, self).getStageX())

    @override
    @overload
    def getBubbles(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.getBubbles()"""
        return bool._wrap(super(Event, self).getBubbles())

    @override
    @overload
    def isHandled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isHandled()"""
        return bool._wrap(super(Event, self).isHandled())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.InputEvent()"""
        val = _InputEvent()
        self.__wrapper = val

    @overload
    def setRelatedActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setRelatedActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_InputEvent, self).setRelatedActor(arg0)

    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setButton(int)"""
        super(_InputEvent, self).setButton(_int.valueOf(arg0))

    @overload
    def setStageX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setStageX(float)"""
        super(_InputEvent, self).setStageX(_float.valueOf(arg0))

    @overload
    def getScrollAmountX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.InputEvent.getScrollAmountX()"""
        return float._wrap(super(InputEvent, self).getScrollAmountX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setType(self, arg0: 'Type'):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setType(com.badlogic.gdx.scenes.scene2d.InputEvent$Type)"""
        super(_InputEvent, self).setType(arg0)

    @override
    @overload
    def getTarget(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getTarget()"""
        return 'Actor'._wrap(super(Event, self).getTarget())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def setBubbles(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setBubbles(boolean)"""
        super(_Event, self).setBubbles(_boolean.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.reset()"""
        super(InputEvent, self).reset()

    @override
    @overload
    def getStage(self) -> 'Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Event.getStage()"""
        return 'Stage'._wrap(super(Event, self).getStage())

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCancelled()"""
        return bool._wrap(super(Event, self).isCancelled())

    @override
    @overload
    def isCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCapture()"""
        return bool._wrap(super(Event, self).isCapture())

    @overload
    def getKeyCode(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.InputEvent.getKeyCode()"""
        return int._wrap(super(InputEvent, self).getKeyCode())

    @overload
    def setStageY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setStageY(float)"""
        super(_InputEvent, self).setStageY(_float.valueOf(arg0))

    @overload
    def getStageY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.InputEvent.getStageY()"""
        return float._wrap(super(InputEvent, self).getStageY())

    @override
    @overload
    def setStage(self, arg0: 'Stage'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setStage(com.badlogic.gdx.scenes.scene2d.Stage)"""
        super(_Event, self).setStage(arg0)

    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.scenes.scene2d.InputEvent$Type com.badlogic.gdx.scenes.scene2d.InputEvent.getType()"""
        return 'Type'._wrap(super(InputEvent, self).getType())

    @overload
    def setScrollAmountX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setScrollAmountX(float)"""
        super(_InputEvent, self).setScrollAmountX(_float.valueOf(arg0))

    @overload
    def toCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.InputEvent.toCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_InputEvent, self).toCoordinates(arg0, arg1))

    @overload
    def getRelatedActor(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.InputEvent.getRelatedActor()"""
        return 'Actor'._wrap(super(InputEvent, self).getRelatedActor())

    @override
    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.cancel()"""
        super(Event, self).cancel()

    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.stop()"""
        super(Event, self).stop()

    @override
    @overload
    def handle(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.handle()"""
        super(Event, self).handle()

    @overload
    def setKeyCode(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setKeyCode(int)"""
        super(_InputEvent, self).setKeyCode(_int.valueOf(arg0))

    @overload
    def getTouchFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputEvent.getTouchFocus()"""
        return bool._wrap(super(InputEvent, self).getTouchFocus())

    @overload
    def isTouchFocusCancel(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputEvent.isTouchFocusCancel()"""
        return bool._wrap(super(InputEvent, self).isTouchFocusCancel())

    @override
    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setCapture(boolean)"""
        super(_Event, self).setCapture(_boolean.valueOf(arg0))

    @overload
    def setTouchFocus(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setTouchFocus(boolean)"""
        super(_InputEvent, self).setTouchFocus(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setCharacter(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setCharacter(char)"""
        super(_InputEvent, self).setCharacter(_char.valueOf(arg0))

    @override
    @overload
    def getListenerActor(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getListenerActor()"""
        return 'Actor'._wrap(super(Event, self).getListenerActor())

    @override
    @overload
    def isStopped(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isStopped()"""
        return bool._wrap(super(Event, self).isStopped())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Action
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Action():
    """com.badlogic.gdx.scenes.scene2d.Action"""
 
    @staticmethod
    def _wrap(java_value: _Action) -> 'Action':
        return Action(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Action):
        """
        Dynamic initializer for Action.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Action__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Action__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Action()"""
        val = _Action()
        self.__wrapper = val

    @abstractmethod
    def act(self, arg0: float):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.Action.act(float)"""
        pass

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
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(Action, self).getPool())

    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Action, self).setActor(arg0)

    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(Action, self).restart()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Action, self).setTarget(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_Action, self).setPool(arg0)

    @overload
    def getActor(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'Actor'._wrap(super(Action, self).getActor())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(Action, self).reset()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(Action, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Action()"""
        val = _Action()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTarget(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'Actor'._wrap(super(Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Group
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.scenes.scene2d.Touchable as _Touchable
_Touchable = _Touchable
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Stage as _Stage
_Stage = _Stage
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.scenes.scene2d.Group as _Group
_Group = _Group
import java.lang.String as _string
import com.badlogic.gdx.utils.DelayedRemovalArray as _DelayedRemovalArray
_DelayedRemovalArray = _DelayedRemovalArray
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.Vector2 as _Vector2
_Vector2 = _Vector2
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

import com.badlogic.gdx.utils.SnapshotArray as _SnapshotArray
_SnapshotArray = _SnapshotArray
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Group():
    """com.badlogic.gdx.scenes.scene2d.Group"""
 
    @staticmethod
    def _wrap(java_value: _Group) -> 'Group':
        return Group(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Group):
        """
        Dynamic initializer for Group.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Group__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Group__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTouchable(self) -> 'Touchable':
        """public com.badlogic.gdx.scenes.scene2d.Touchable com.badlogic.gdx.scenes.scene2d.Actor.getTouchable()"""
        return 'Touchable'._wrap(super(Actor, self).getTouchable())

    @override
    @overload
    def drawDebug(self, arg0: 'ShapeRenderer'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.drawDebug(com.badlogic.gdx.graphics.glutils.ShapeRenderer)"""
        super(_Group, self).drawDebug(arg0)

    @override
    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOriginX(float)"""
        super(_Actor, self).setOriginX(_float.valueOf(arg0))

    @overload
    def fire(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.fire(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_Actor, self).fire(arg0))

    @overload
    def localToScreenCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToScreenCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToScreenCoordinates(arg0))

    @overload
    def removeListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Actor, self).removeListener(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_Actor, self).addAction(arg0)

    @overload
    def screenToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.screenToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).screenToLocalCoordinates(arg0))

    @overload
    def getY(self, arg0: int) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getY(int)"""
        return float._wrap(super(_Actor, self).getY(_int.valueOf(arg0)))

    @overload
    def swapActor(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.swapActor(int,int)"""
        return bool._wrap(super(_Group, self).swapActor(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def firstAscendant(self, arg0: 'Class') -> 'Actor':
        """public <T extends com.badlogic.gdx.scenes.scene2d.Actor> T com.badlogic.gdx.scenes.scene2d.Actor.firstAscendant(java.lang.Class<T>)"""
        return 'Actor'._wrap(super(_Actor, self).firstAscendant(arg0))

    @override
    @overload
    def isTouchable(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchable()"""
        return bool._wrap(super(Actor, self).isTouchable())

    @override
    @overload
    def sizeBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.sizeBy(float,float)"""
        super(_Actor, self).sizeBy(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.Group.clear()"""
        super(Group, self).clear()

    @overload
    def isDescendantOf(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isDescendantOf(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool._wrap(super(_Actor, self).isDescendantOf(arg0))

    @override
    @overload
    def debug(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Actor.debug()"""
        return 'Actor'._wrap(super(Actor, self).debug())

    @override
    @overload
    def hasActions(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasActions()"""
        return bool._wrap(super(Actor, self).hasActions())

    @override
    @overload
    def rotateBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.rotateBy(float)"""
        super(_Actor, self).rotateBy(_float.valueOf(arg0))

    @overload
    def removeActorAt(self, arg0: int, arg1: bool) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Group.removeActorAt(int,boolean)"""
        return 'Actor'._wrap(super(_Group, self).removeActorAt(_int.valueOf(arg0), _boolean.valueOf(arg1)))

    @override
    @overload
    def setDebug(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setDebug(boolean)"""
        super(_Actor, self).setDebug(_boolean.valueOf(arg0))

    @override
    @overload
    def isTouchFocusTarget(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchFocusTarget()"""
        return bool._wrap(super(Actor, self).isTouchFocusTarget())

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getOriginY()"""
        return float._wrap(super(Actor, self).getOriginY())

    @overload
    def removeActor(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.removeActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool._wrap(super(_Group, self).removeActor(arg0))

    @override
    @overload
    def getParent(self) -> 'Group':
        """public com.badlogic.gdx.scenes.scene2d.Group com.badlogic.gdx.scenes.scene2d.Actor.getParent()"""
        return 'Group'._wrap(super(Actor, self).getParent())

    @override
    @overload
    def hasScrollFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasScrollFocus()"""
        return bool._wrap(super(Actor, self).hasScrollFocus())

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getScaleX()"""
        return float._wrap(super(Actor, self).getScaleX())

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setRotation(float)"""
        super(_Actor, self).setRotation(_float.valueOf(arg0))

    @override
    @overload
    def scaleBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.scaleBy(float)"""
        super(_Actor, self).scaleBy(_float.valueOf(arg0))

    @override
    @overload
    def hasKeyboardFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasKeyboardFocus()"""
        return bool._wrap(super(Actor, self).hasKeyboardFocus())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setVisible(boolean)"""
        super(_Actor, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def addActorBefore(self, arg0: 'Actor', arg1: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.addActorBefore(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Group, self).addActorBefore(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setPosition(float,float)"""
        super(_Actor, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getStage(self) -> 'Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Actor.getStage()"""
        return 'Stage'._wrap(super(Actor, self).getStage())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Group.toString()"""
        return str._wrap(super(Group, self).toString())

    @override
    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setY(float)"""
        super(_Actor, self).setY(_float.valueOf(arg0))

    @override
    @overload
    def ascendantsVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.ascendantsVisible()"""
        return bool._wrap(super(Actor, self).ascendantsVisible())

    @override
    @overload
    def isTouchFocusListener(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchFocusListener()"""
        return bool._wrap(super(Actor, self).isTouchFocusListener())

    @overload
    def findActor(self, arg0: str) -> 'Actor':
        """public <T extends com.badlogic.gdx.scenes.scene2d.Actor> T com.badlogic.gdx.scenes.scene2d.Group.findActor(java.lang.String)"""
        return 'Actor'._wrap(super(_Group, self).findActor(arg0))

    @overload
    def hit(self, arg0: float, arg1: float, arg2: bool) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Group.hit(float,float,boolean)"""
        return 'Actor'._wrap(super(_Group, self).hit(_float.valueOf(arg0), _float.valueOf(arg1), _boolean.valueOf(arg2)))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Actor, self).setColor(arg0)

    @overload
    def parentToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.parentToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).parentToLocalCoordinates(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Group()"""
        val = _Group()
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Actor.getName()"""
        return str._wrap(super(Actor, self).getName())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isVisible()"""
        return bool._wrap(super(Actor, self).isVisible())

    @override
    @overload
    def sizeBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.sizeBy(float)"""
        super(_Actor, self).sizeBy(_float.valueOf(arg0))

    @overload
    def getChildren(self) -> 'utils.SnapshotArray':
        """public com.badlogic.gdx.utils.SnapshotArray<com.badlogic.gdx.scenes.scene2d.Actor> com.badlogic.gdx.scenes.scene2d.Group.getChildren()"""
        return 'utils.SnapshotArray'._wrap(super(Group, self).getChildren())

    @overload
    def removeActor(self, arg0: 'Actor', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.removeActor(com.badlogic.gdx.scenes.scene2d.Actor,boolean)"""
        return bool._wrap(super(_Group, self).removeActor(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScale(float,float)"""
        super(_Actor, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def localToDescendantCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Group.localToDescendantCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Group, self).localToDescendantCoordinates(arg0, arg1))

    @override
    @overload
    def getListeners(self) -> 'utils.DelayedRemovalArray':
        """public com.badlogic.gdx.utils.DelayedRemovalArray<com.badlogic.gdx.scenes.scene2d.EventListener> com.badlogic.gdx.scenes.scene2d.Actor.getListeners()"""
        return 'utils.DelayedRemovalArray'._wrap(super(Actor, self).getListeners())

    @overload
    def isAscendantOf(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isAscendantOf(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool._wrap(super(_Actor, self).isAscendantOf(arg0))

    @override
    @overload
    def getDebug(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.getDebug()"""
        return bool._wrap(super(Actor, self).getDebug())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setName(java.lang.String)"""
        super(_Actor, self).setName(arg0)

    @override
    @overload
    def getUserObject(self) -> object:
        """public java.lang.Object com.badlogic.gdx.scenes.scene2d.Actor.getUserObject()"""
        return object._wrap(super(Actor, self).getUserObject())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setPosition(float,float,int)"""
        super(_Actor, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def setY(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setY(float,int)"""
        super(_Actor, self).setY(_float.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setZIndex(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.setZIndex(int)"""
        return bool._wrap(super(_Actor, self).setZIndex(_int.valueOf(arg0)))

    @overload
    def addActorAt(self, arg0: int, arg1: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.addActorAt(int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Group, self).addActorAt(_int.valueOf(arg0), arg1)

    @override
    @overload
    def setHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setHeight(float)"""
        super(_Actor, self).setHeight(_float.valueOf(arg0))

    @overload
    def localToStageCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToStageCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToStageCoordinates(arg0))

    @override
    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getHeight()"""
        return float._wrap(super(Actor, self).getHeight())

    @override
    @overload
    def scaleBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.scaleBy(float,float)"""
        super(_Actor, self).scaleBy(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def swapActor(self, arg0: 'Actor', arg1: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.swapActor(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool._wrap(super(_Group, self).swapActor(arg0, arg1))

    @override
    @overload
    def act(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Group.act(float)"""
        super(_Group, self).act(_float.valueOf(arg0))

    @override
    @overload
    def setTouchable(self, arg0: 'Touchable'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setTouchable(com.badlogic.gdx.scenes.scene2d.Touchable)"""
        super(_Actor, self).setTouchable(arg0)

    @overload
    def addActorAfter(self, arg0: 'Actor', arg1: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.addActorAfter(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Group, self).addActorAfter(arg0, arg1)

    @override
    @overload
    def setWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setWidth(float)"""
        super(_Actor, self).setWidth(_float.valueOf(arg0))

    @overload
    def stageToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.stageToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).stageToLocalCoordinates(arg0))

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
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getWidth()"""
        return float._wrap(super(Actor, self).getWidth())

    @override
    @overload
    def getTop(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getTop()"""
        return float._wrap(super(Actor, self).getTop())

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getScaleY()"""
        return float._wrap(super(Actor, self).getScaleY())

    @overload
    def getX(self, arg0: int) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getX(int)"""
        return float._wrap(super(_Actor, self).getX(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def toFront(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.toFront()"""
        super(Actor, self).toFront()

    @overload
    def addListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.addListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Actor, self).addListener(arg0))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.Actor.getColor()"""
        return 'graphics.Color'._wrap(super(Actor, self).getColor())

    @override
    @overload
    def getCaptureListeners(self) -> 'utils.DelayedRemovalArray':
        """public com.badlogic.gdx.utils.DelayedRemovalArray<com.badlogic.gdx.scenes.scene2d.EventListener> com.badlogic.gdx.scenes.scene2d.Actor.getCaptureListeners()"""
        return 'utils.DelayedRemovalArray'._wrap(super(Actor, self).getCaptureListeners())

    @override
    @overload
    def removeAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.removeAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_Actor, self).removeAction(arg0)

    @overload
    def addActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.addActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Group, self).addActor(arg0)

    @overload
    def clearChildren(self):
        """public void com.badlogic.gdx.scenes.scene2d.Group.clearChildren()"""
        super(Group, self).clearChildren()

    @overload
    def clear(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Group.clear(boolean)"""
        super(_Group, self).clear(_boolean.valueOf(arg0))

    @override
    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getRotation()"""
        return float._wrap(super(Actor, self).getRotation())

    @override
    @overload
    def remove(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.remove()"""
        return bool._wrap(super(Actor, self).remove())

    @override
    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScaleX(float)"""
        super(_Actor, self).setScaleX(_float.valueOf(arg0))

    @override
    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOriginY(float)"""
        super(_Actor, self).setOriginY(_float.valueOf(arg0))

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getY()"""
        return float._wrap(super(Actor, self).getY())

    @overload
    def hasChildren(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.hasChildren()"""
        return bool._wrap(super(Group, self).hasChildren())

    @override
    @overload
    def hasParent(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasParent()"""
        return bool._wrap(super(Actor, self).hasParent())

    @override
    @overload
    def ancestorsVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.ancestorsVisible()"""
        return bool._wrap(super(Actor, self).ancestorsVisible())

    @override
    @overload
    def toBack(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.toBack()"""
        super(Actor, self).toBack()

    @override
    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScaleY(float)"""
        super(_Actor, self).setScaleY(_float.valueOf(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getX()"""
        return float._wrap(super(Actor, self).getX())

    @override
    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOrigin(float,float)"""
        super(_Actor, self).setOrigin(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setUserObject(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setUserObject(java.lang.Object)"""
        super(_Actor, self).setUserObject(arg0)

    @override
    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setBounds(float,float,float,float)"""
        super(_Actor, self).setBounds(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setSize(float,float)"""
        super(_Actor, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def clipBegin(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.clipBegin()"""
        return bool._wrap(super(Actor, self).clipBegin())

    @overload
    def notify(self, arg0: 'Event', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.notify(com.badlogic.gdx.scenes.scene2d.Event,boolean)"""
        return bool._wrap(super(_Actor, self).notify(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScale(float)"""
        super(_Actor, self).setScale(_float.valueOf(arg0))

    @override
    @overload
    def getZIndex(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.Actor.getZIndex()"""
        return int._wrap(super(Actor, self).getZIndex())

    @override
    @overload
    def setOrigin(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOrigin(int)"""
        super(_Actor, self).setOrigin(_int.valueOf(arg0))

    @override
    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getOriginX()"""
        return float._wrap(super(Actor, self).getOriginX())

    @overload
    def debugAll(self) -> 'Group':
        """public com.badlogic.gdx.scenes.scene2d.Group com.badlogic.gdx.scenes.scene2d.Group.debugAll()"""
        return 'Group'._wrap(super(Group, self).debugAll())

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Group.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(_Group, self).draw(arg0, _float.valueOf(arg1))

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setColor(float,float,float,float)"""
        super(_Actor, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clearListeners()"""
        super(Actor, self).clearListeners()

    @overload
    def getChild(self, arg0: int) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Group.getChild(int)"""
        return 'Actor'._wrap(super(_Group, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setX(float)"""
        super(_Actor, self).setX(_float.valueOf(arg0))

    @overload
    def removeCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.removeCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Actor, self).removeCaptureListener(arg0))

    @override
    @overload
    def clearActions(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clearActions()"""
        super(Actor, self).clearActions()

    @override
    @overload
    def moveBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.moveBy(float,float)"""
        super(_Actor, self).moveBy(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setDebug(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Group.setDebug(boolean,boolean)"""
        super(_Group, self).setDebug(_boolean.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def getActions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Action> com.badlogic.gdx.scenes.scene2d.Actor.getActions()"""
        return 'utils.Array'._wrap(super(Actor, self).getActions())

    @overload
    def clipBegin(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.clipBegin(float,float,float,float)"""
        return bool._wrap(super(_Actor, self).clipBegin(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Group()"""
        val = _Group()
        self.__wrapper = val

    @overload
    def addCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.addCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool._wrap(super(_Actor, self).addCaptureListener(arg0))

    @overload
    def localToActorCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToActorCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToActorCoordinates(arg0, arg1))

    @override
    @overload
    def setX(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setX(float,int)"""
        super(_Actor, self).setX(_float.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def localToParentCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToParentCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToParentCoordinates(arg0))

    @overload
    def localToAscendantCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToAscendantCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'._wrap(super(_Actor, self).localToAscendantCoordinates(arg0, arg1))

    @override
    @overload
    def clipEnd(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clipEnd()"""
        super(Actor, self).clipEnd()

    @overload
    def setTransform(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Group.setTransform(boolean)"""
        super(_Group, self).setTransform(_boolean.valueOf(arg0))

    @override
    @overload
    def setCullingArea(self, arg0: 'Rectangle'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.setCullingArea(com.badlogic.gdx.math.Rectangle)"""
        super(_Group, self).setCullingArea(arg0)

    @overload
    def getCullingArea(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.scenes.scene2d.Group.getCullingArea()"""
        return 'math.Rectangle'._wrap(super(Group, self).getCullingArea())

    @overload
    def isTransform(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.isTransform()"""
        return bool._wrap(super(Group, self).isTransform())

    @override
    @overload
    def getRight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getRight()"""
        return float._wrap(super(Actor, self).getRight())

    @overload
    def clearChildren(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Group.clearChildren(boolean)"""
        super(_Group, self).clearChildren(_boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Touchable
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Touchable as _Touchable
_Touchable = _Touchable
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
 
class Touchable():
    """com.badlogic.gdx.scenes.scene2d.Touchable"""
 
    @staticmethod
    def _wrap(java_value: _Touchable) -> 'Touchable':
        return Touchable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Touchable):
        """
        Dynamic initializer for Touchable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Touchable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Touchable__wrapper":
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
    def valueOf(arg0: str) -> 'Touchable':
        """public static com.badlogic.gdx.scenes.scene2d.Touchable com.badlogic.gdx.scenes.scene2d.Touchable.valueOf(java.lang.String)"""
        return Touchable._wrap(_Touchable.valueOf(arg0))

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
    def values() -> List['Touchable']:
        """public static com.badlogic.gdx.scenes.scene2d.Touchable[] com.badlogic.gdx.scenes.scene2d.Touchable.values()"""
        return List[Touchable]._wrap(_Touchable.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Event
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Stage as _Stage
_Stage = _Stage
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.Event as _Event
_Event = _Event
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Event():
    """com.badlogic.gdx.scenes.scene2d.Event"""
 
    @staticmethod
    def _wrap(java_value: _Event) -> 'Event':
        return Event(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Event):
        """
        Dynamic initializer for Event.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Event__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Event__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getStage(self) -> 'Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Event.getStage()"""
        return 'Stage'._wrap(super(Event, self).getStage())

    @overload
    def setListenerActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setListenerActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Event, self).setListenerActor(arg0)

    @overload
    def handle(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.handle()"""
        super(Event, self).handle()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getBubbles(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.getBubbles()"""
        return bool._wrap(super(Event, self).getBubbles())

    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Event, self).setTarget(arg0)

    @overload
    def setBubbles(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setBubbles(boolean)"""
        super(_Event, self).setBubbles(_boolean.valueOf(arg0))

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
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.reset()"""
        super(Event, self).reset()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Event()"""
        val = _Event()
        self.__wrapper = val

    @overload
    def stop(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.stop()"""
        super(Event, self).stop()

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.cancel()"""
        super(Event, self).cancel()

    @overload
    def isCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCapture()"""
        return bool._wrap(super(Event, self).isCapture())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isHandled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isHandled()"""
        return bool._wrap(super(Event, self).isHandled())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getTarget(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getTarget()"""
        return 'Actor'._wrap(super(Event, self).getTarget())

    @overload
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCancelled()"""
        return bool._wrap(super(Event, self).isCancelled())

    @overload
    def isStopped(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isStopped()"""
        return bool._wrap(super(Event, self).isStopped())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Event()"""
        val = _Event()
        self.__wrapper = val

    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setCapture(boolean)"""
        super(_Event, self).setCapture(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setStage(self, arg0: 'Stage'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setStage(com.badlogic.gdx.scenes.scene2d.Stage)"""
        super(_Event, self).setStage(arg0)

    @overload
    def getListenerActor(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getListenerActor()"""
        return 'Actor'._wrap(super(Event, self).getListenerActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Stage$TouchFocus
import com.badlogic.gdx.scenes.scene2d.Stage as _Stage_TouchFocus
_TouchFocus = _Stage_TouchFocus.TouchFocus
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
 
class TouchFocus():
    """com.badlogic.gdx.scenes.scene2d.Stage.TouchFocus"""
 
    @staticmethod
    def _wrap(java_value: _TouchFocus) -> 'TouchFocus':
        return TouchFocus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TouchFocus):
        """
        Dynamic initializer for TouchFocus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TouchFocus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TouchFocus__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Stage$TouchFocus()"""
        val = _TouchFocus()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage$TouchFocus.reset()"""
        super(TouchFocus, self).reset()

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
        """public com.badlogic.gdx.scenes.scene2d.Stage$TouchFocus()"""
        val = _TouchFocus()
        self.__wrapper = val
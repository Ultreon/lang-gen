from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener as _ClickListener
_ClickListener = _ClickListener
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.InputListener as _InputListener
_InputListener = _InputListener
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClickListener():
    """com.badlogic.gdx.scenes.scene2d.utils.ClickListener"""
 
    @staticmethod
    def _wrap(java_value: _ClickListener) -> 'ClickListener':
        return ClickListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClickListener):
        """
        Dynamic initializer for ClickListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClickListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClickListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def inTapSquare(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.inTapSquare(float,float)"""
        return bool._wrap(super(_ClickListener, self).inTapSquare(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def getTapCount(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTapCount()"""
        return int._wrap(super(ClickListener, self).getTapCount())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.scenes.scene2d.utils.ClickListener(int)"""
        val = _ClickListener(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def getPressedPointer(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getPressedPointer()"""
        return int._wrap(super(ClickListener, self).getPressedPointer())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def inTapSquare(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.inTapSquare()"""
        return bool._wrap(super(ClickListener, self).inTapSquare())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isOver(self, arg0: 'Actor', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isOver(com.badlogic.gdx.scenes.scene2d.Actor,float,float)"""
        return bool._wrap(super(_ClickListener, self).isOver(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getButton()"""
        return int._wrap(super(ClickListener, self).getButton())

    @overload
    def setTapCountInterval(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setTapCountInterval(float)"""
        super(_ClickListener, self).setTapCountInterval(_float.valueOf(arg0))

    @override
    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_ClickListener, self).touchUp(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setButton(int)"""
        super(_ClickListener, self).setButton(_int.valueOf(arg0))

    @overload
    def invalidateTapSquare(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.invalidateTapSquare()"""
        super(ClickListener, self).invalidateTapSquare()

    @overload
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool._wrap(super(_scene2d.InputListener, self).scrolled(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool._wrap(super(_scene2d.InputListener, self).mouseMoved(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setVisualPressed(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setVisualPressed(boolean)"""
        super(_ClickListener, self).setVisualPressed(_boolean.valueOf(arg0))

    @overload
    def getTapSquareSize(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTapSquareSize()"""
        return float._wrap(super(ClickListener, self).getTapSquareSize())

    @overload
    def isOver(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isOver()"""
        return bool._wrap(super(ClickListener, self).isOver())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyUp(arg0, _int.valueOf(arg1)))

    @overload
    def setTapCount(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setTapCount(int)"""
        super(_ClickListener, self).setTapCount(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_ClickListener, self).enter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ClickListener()"""
        val = _ClickListener()
        self.__wrapper = val

    @override
    @overload
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_ClickListener, self).exit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.ClickListener()"""
        val = _ClickListener()
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_scene2d.InputListener, self).handle(arg0))

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyDown(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isVisualPressed(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isVisualPressed()"""
        return bool._wrap(super(ClickListener, self).isVisualPressed())

    @override
    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_ClickListener, self).touchDragged(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def clicked(self, arg0: 'InputEvent', arg1: float, arg2: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.clicked(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        super(_ClickListener, self).clicked(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTouchDownX()"""
        return float._wrap(super(ClickListener, self).getTouchDownX())

    @overload
    def isPressed(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isPressed()"""
        return bool._wrap(super(ClickListener, self).isPressed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.cancel()"""
        super(ClickListener, self).cancel()

    @overload
    def getTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTouchDownY()"""
        return float._wrap(super(ClickListener, self).getTouchDownY())

    @overload
    def getPressedButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getPressedButton()"""
        return int._wrap(super(ClickListener, self).getPressedButton())

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setTapSquareSize(float)"""
        super(_ClickListener, self).setTapSquareSize(_float.valueOf(arg0))

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool._wrap(super(_ClickListener, self).touchDown(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyTyped(arg0, _char.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ClickListener
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener as _ClickListener
_ClickListener = _ClickListener
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.InputListener as _InputListener
_InputListener = _InputListener
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClickListener():
    """com.badlogic.gdx.scenes.scene2d.utils.ClickListener"""
 
    @staticmethod
    def _wrap(java_value: _ClickListener) -> 'ClickListener':
        return ClickListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClickListener):
        """
        Dynamic initializer for ClickListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClickListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClickListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def inTapSquare(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.inTapSquare(float,float)"""
        return bool._wrap(super(_ClickListener, self).inTapSquare(_float.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def getTapCount(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTapCount()"""
        return int._wrap(super(ClickListener, self).getTapCount())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.scenes.scene2d.utils.ClickListener(int)"""
        val = _ClickListener(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def getPressedPointer(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getPressedPointer()"""
        return int._wrap(super(ClickListener, self).getPressedPointer())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def inTapSquare(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.inTapSquare()"""
        return bool._wrap(super(ClickListener, self).inTapSquare())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isOver(self, arg0: 'Actor', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isOver(com.badlogic.gdx.scenes.scene2d.Actor,float,float)"""
        return bool._wrap(super(_ClickListener, self).isOver(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getButton()"""
        return int._wrap(super(ClickListener, self).getButton())

    @overload
    def setTapCountInterval(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setTapCountInterval(float)"""
        super(_ClickListener, self).setTapCountInterval(_float.valueOf(arg0))

    @override
    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_ClickListener, self).touchUp(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setButton(int)"""
        super(_ClickListener, self).setButton(_int.valueOf(arg0))

    @overload
    def invalidateTapSquare(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.invalidateTapSquare()"""
        super(ClickListener, self).invalidateTapSquare()

    @overload
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool._wrap(super(_scene2d.InputListener, self).scrolled(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool._wrap(super(_scene2d.InputListener, self).mouseMoved(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setVisualPressed(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setVisualPressed(boolean)"""
        super(_ClickListener, self).setVisualPressed(_boolean.valueOf(arg0))

    @overload
    def getTapSquareSize(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTapSquareSize()"""
        return float._wrap(super(ClickListener, self).getTapSquareSize())

    @overload
    def isOver(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isOver()"""
        return bool._wrap(super(ClickListener, self).isOver())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyUp(arg0, _int.valueOf(arg1)))

    @overload
    def setTapCount(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setTapCount(int)"""
        super(_ClickListener, self).setTapCount(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_ClickListener, self).enter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ClickListener()"""
        val = _ClickListener()
        self.__wrapper = val

    @override
    @overload
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_ClickListener, self).exit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.ClickListener()"""
        val = _ClickListener()
        self.__wrapper = val

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_scene2d.InputListener, self).handle(arg0))

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyDown(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isVisualPressed(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isVisualPressed()"""
        return bool._wrap(super(ClickListener, self).isVisualPressed())

    @override
    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_ClickListener, self).touchDragged(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def clicked(self, arg0: 'InputEvent', arg1: float, arg2: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.clicked(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        super(_ClickListener, self).clicked(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTouchDownX()"""
        return float._wrap(super(ClickListener, self).getTouchDownX())

    @overload
    def isPressed(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isPressed()"""
        return bool._wrap(super(ClickListener, self).isPressed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.cancel()"""
        super(ClickListener, self).cancel()

    @overload
    def getTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTouchDownY()"""
        return float._wrap(super(ClickListener, self).getTouchDownY())

    @overload
    def getPressedButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getPressedButton()"""
        return int._wrap(super(ClickListener, self).getPressedButton())

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setTapSquareSize(float)"""
        super(_ClickListener, self).setTapSquareSize(_float.valueOf(arg0))

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool._wrap(super(_ClickListener, self).touchDown(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyTyped(arg0, _char.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ClickListener 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Drawable
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import com.badlogic.gdx.scenes.scene2d.utils.Drawable as _Drawable
_Drawable = _Drawable
from abc import abstractmethod, ABC
 
class Drawable():
    """com.badlogic.gdx.scenes.scene2d.utils.Drawable"""
 
    @staticmethod
    def _wrap(java_value: _Drawable) -> 'Drawable':
        return Drawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Drawable):
        """
        Dynamic initializer for Drawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Drawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Drawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setLeftWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setLeftWidth(float)"""
        pass

    @abstractmethod
    def setMinWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setMinWidth(float)"""
        pass

    @abstractmethod
    def setMinHeight(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setMinHeight(float)"""
        pass

    @abstractmethod
    def getMinWidth(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getMinWidth()"""
        pass

    @abstractmethod
    def getRightWidth(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getRightWidth()"""
        pass

    @abstractmethod
    def getMinHeight(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getMinHeight()"""
        pass

    @abstractmethod
    def getLeftWidth(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getLeftWidth()"""
        pass

    @abstractmethod
    def setRightWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setRightWidth(float)"""
        pass

    @abstractmethod
    def getTopHeight(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getTopHeight()"""
        pass

    @abstractmethod
    def setBottomHeight(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setBottomHeight(float)"""
        pass

    @abstractmethod
    def setTopHeight(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setTopHeight(float)"""
        pass

    @abstractmethod
    def getBottomHeight(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getBottomHeight()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener as _DragScrollListener
_DragScrollListener = _DragScrollListener
try:
    from pygdx.scenes.scene2d import ui
except ImportError:
    ui = _import_once("pygdx.scenes.scene2d.ui")

import com.badlogic.gdx.scenes.scene2d.utils.DragListener as _DragListener
_DragListener = _DragListener
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.InputListener as _InputListener
_InputListener = _InputListener
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DragScrollListener():
    """com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener"""
 
    @staticmethod
    def _wrap(java_value: _DragScrollListener) -> 'DragScrollListener':
        return DragScrollListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DragScrollListener):
        """
        Dynamic initializer for DragScrollListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DragScrollListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DragScrollListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setButton(int)"""
        super(_DragListener, self).setButton(_int.valueOf(arg0))

    @override
    @overload
    def dragStart(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.dragStart(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_DragListener, self).dragStart(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.InputListener, self).exit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool._wrap(super(_DragListener, self).touchDown(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getStageTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getStageTouchDownY()"""
        return float._wrap(super(DragListener, self).getStageTouchDownY())

    @override
    @overload
    def getDragY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragY()"""
        return float._wrap(super(DragListener, self).getDragY())

    @override
    @overload
    def setDragStartX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setDragStartX(float)"""
        super(_DragListener, self).setDragStartX(_float.valueOf(arg0))

    @override
    @overload
    def getTapSquareSize(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTapSquareSize()"""
        return float._wrap(super(DragListener, self).getTapSquareSize())

    @override
    @overload
    def getDragStartY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragStartY()"""
        return float._wrap(super(DragListener, self).getDragStartY())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeltaY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDeltaY()"""
        return float._wrap(super(DragListener, self).getDeltaY())

    @overload
    def __init__(self, arg0: 'ScrollPane'):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener(com.badlogic.gdx.scenes.scene2d.ui.ScrollPane)"""
        val = _DragScrollListener(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.cancel()"""
        super(DragListener, self).cancel()

    @override
    @overload
    def getDragX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragX()"""
        return float._wrap(super(DragListener, self).getDragX())

    @overload
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool._wrap(super(_scene2d.InputListener, self).scrolled(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @override
    @overload
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.InputListener, self).enter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool._wrap(super(_scene2d.InputListener, self).mouseMoved(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setTapSquareSize(float)"""
        super(_DragListener, self).setTapSquareSize(_float.valueOf(arg0))

    @override
    @overload
    def isDragging(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragListener.isDragging()"""
        return bool._wrap(super(DragListener, self).isDragging())

    @overload
    def setPadding(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener.setPadding(float,float)"""
        super(_DragScrollListener, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_DragListener, self).touchUp(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyUp(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def getButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.DragListener.getButton()"""
        return int._wrap(super(DragListener, self).getButton())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTouchDownX()"""
        return float._wrap(super(DragListener, self).getTouchDownX())

    @override
    @overload
    def getDragStartX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragStartX()"""
        return float._wrap(super(DragListener, self).getDragStartX())

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_scene2d.InputListener, self).handle(arg0))

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyDown(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getDeltaX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDeltaX()"""
        return float._wrap(super(DragListener, self).getDeltaX())

    @override
    @overload
    def getTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTouchDownY()"""
        return float._wrap(super(DragListener, self).getTouchDownY())

    @overload
    def setup(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener.setup(float,float,float,float)"""
        super(_DragScrollListener, self).setup(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_DragListener, self).touchDragged(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def getDragDistance(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragDistance()"""
        return float._wrap(super(DragListener, self).getDragDistance())

    @override
    @overload
    def setDragStartY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setDragStartY(float)"""
        super(_DragListener, self).setDragStartY(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def dragStop(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener.dragStop(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_DragScrollListener, self).dragStop(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getStageTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getStageTouchDownX()"""
        return float._wrap(super(DragListener, self).getStageTouchDownX())

    @override
    @overload
    def drag(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener.drag(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_DragScrollListener, self).drag(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyTyped(arg0, _char.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.UIUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.utils.UIUtils as _UIUtils
_UIUtils = _UIUtils
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UIUtils():
    """com.badlogic.gdx.scenes.scene2d.utils.UIUtils"""
 
    @staticmethod
    def _wrap(java_value: _UIUtils) -> 'UIUtils':
        return UIUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UIUtils):
        """
        Dynamic initializer for UIUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UIUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UIUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def shift(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.shift(int)"""
        return bool._wrap(_UIUtils.shift(_int.valueOf(arg0)))

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

    @staticmethod
    @overload
    def left(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.left(int)"""
        return bool._wrap(_UIUtils.left(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def middle(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.middle(int)"""
        return bool._wrap(_UIUtils.middle(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ctrl(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.ctrl(int)"""
        return bool._wrap(_UIUtils.ctrl(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def right(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.right(int)"""
        return bool._wrap(_UIUtils.right(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def middle() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.middle()"""
        return bool._wrap(_UIUtils.middle())

    @staticmethod
    @overload
    def ctrl() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.ctrl()"""
        return bool._wrap(_UIUtils.ctrl())

    @staticmethod
    @overload
    def shift() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.shift()"""
        return bool._wrap(_UIUtils.shift())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def left() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.left()"""
        return bool._wrap(_UIUtils.left())

    @staticmethod
    @overload
    def alt(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.alt(int)"""
        return bool._wrap(_UIUtils.alt(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def alt() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.alt()"""
        return bool._wrap(_UIUtils.alt())

    @staticmethod
    @overload
    def right() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.right()"""
        return bool._wrap(_UIUtils.right())

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener as _ActorGestureListener
_ActorGestureListener = _ActorGestureListener
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import com.badlogic.gdx.input.GestureDetector as _GestureDetector
_GestureDetector = _GestureDetector
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import input
except ImportError:
    input = _import_once("pygdx.input")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ActorGestureListener():
    """com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener"""
 
    @staticmethod
    def _wrap(java_value: _ActorGestureListener) -> 'ActorGestureListener':
        return ActorGestureListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ActorGestureListener):
        """
        Dynamic initializer for ActorGestureListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ActorGestureListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ActorGestureListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def fling(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.fling(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_ActorGestureListener, self).fling(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getTouchDownTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.getTouchDownTarget()"""
        return 'scene2d.Actor'._wrap(super(ActorGestureListener, self).getTouchDownTarget())

    @overload
    def zoom(self, arg0: 'InputEvent', arg1: float, arg2: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.zoom(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        super(_ActorGestureListener, self).zoom(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def panStop(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.panStop(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_ActorGestureListener, self).panStop(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_ActorGestureListener, self).handle(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener()"""
        val = _ActorGestureListener()
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

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_ActorGestureListener, self).touchDown(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def tap(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.tap(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_ActorGestureListener, self).tap(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def pinch(self, arg0: 'InputEvent', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.pinch(com.badlogic.gdx.scenes.scene2d.InputEvent,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_ActorGestureListener, self).pinch(arg0, arg1, arg2, arg3, arg4)

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
        """public com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener()"""
        val = _ActorGestureListener()
        self.__wrapper = val

    @overload
    def longPress(self, arg0: 'Actor', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.longPress(com.badlogic.gdx.scenes.scene2d.Actor,float,float)"""
        return bool._wrap(super(_ActorGestureListener, self).longPress(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_ActorGestureListener, self).touchUp(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def pan(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.pan(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        super(_ActorGestureListener, self).pan(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getGestureDetector(self) -> 'input.GestureDetector':
        """public com.badlogic.gdx.input.GestureDetector com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.getGestureDetector()"""
        return 'input.GestureDetector'._wrap(super(ActorGestureListener, self).getGestureDetector())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener(float,float,float,float)"""
        val = _ActorGestureListener(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ChangeListener$ChangeEvent
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener as _ChangeListener_ChangeEvent
_ChangeEvent = _ChangeListener_ChangeEvent.ChangeEvent
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChangeEvent():
    """com.badlogic.gdx.scenes.scene2d.utils.ChangeListener.ChangeEvent"""
 
    @staticmethod
    def _wrap(java_value: _ChangeEvent) -> 'ChangeEvent':
        return ChangeEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChangeEvent):
        """
        Dynamic initializer for ChangeEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChangeEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChangeEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setCapture(boolean)"""
        super(_scene2d.Event, self).setCapture(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setStage(self, arg0: 'Stage'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setStage(com.badlogic.gdx.scenes.scene2d.Stage)"""
        super(_scene2d.Event, self).setStage(arg0)

    @override
    @overload
    def getBubbles(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.getBubbles()"""
        return bool._wrap(super(scene2d.Event, self).getBubbles())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isHandled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isHandled()"""
        return bool._wrap(super(scene2d.Event, self).isHandled())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.reset()"""
        super(scene2d.Event, self).reset()

    @override
    @overload
    def isCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCapture()"""
        return bool._wrap(super(scene2d.Event, self).isCapture())

    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.stop()"""
        super(scene2d.Event, self).stop()

    @override
    @overload
    def setListenerActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setListenerActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Event, self).setListenerActor(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCancelled()"""
        return bool._wrap(super(scene2d.Event, self).isCancelled())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Event, self).getTarget())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Event, self).setTarget(arg0)

    @override
    @overload
    def isStopped(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isStopped()"""
        return bool._wrap(super(scene2d.Event, self).isStopped())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStage(self) -> 'scene2d.Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Event.getStage()"""
        return 'scene2d.Stage'._wrap(super(scene2d.Event, self).getStage())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.cancel()"""
        super(scene2d.Event, self).cancel()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ChangeListener$ChangeEvent()"""
        val = _ChangeEvent()
        self.__wrapper = val

    @override
    @overload
    def getListenerActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getListenerActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Event, self).getListenerActor())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setBubbles(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setBubbles(boolean)"""
        super(_scene2d.Event, self).setBubbles(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.ChangeListener$ChangeEvent()"""
        val = _ChangeEvent()
        self.__wrapper = val

    @override
    @overload
    def handle(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.handle()"""
        super(scene2d.Event, self).handle()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.TransformDrawable
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import com.badlogic.gdx.scenes.scene2d.utils.Drawable as _Drawable
_Drawable = _Drawable
import com.badlogic.gdx.scenes.scene2d.utils.TransformDrawable as _TransformDrawable
_TransformDrawable = _TransformDrawable
from abc import abstractmethod, ABC
 
class TransformDrawable():
    """com.badlogic.gdx.scenes.scene2d.utils.TransformDrawable"""
 
    @staticmethod
    def _wrap(java_value: _TransformDrawable) -> 'TransformDrawable':
        return TransformDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TransformDrawable):
        """
        Dynamic initializer for TransformDrawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TransformDrawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TransformDrawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setLeftWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setLeftWidth(float)"""
        pass

    @abstractmethod
    def setMinWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setMinWidth(float)"""
        pass

    @abstractmethod
    def setMinHeight(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setMinHeight(float)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.TransformDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def getMinWidth(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getMinWidth()"""
        pass

    @abstractmethod
    def getRightWidth(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getRightWidth()"""
        pass

    @abstractmethod
    def getMinHeight(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getMinHeight()"""
        pass

    @abstractmethod
    def getLeftWidth(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getLeftWidth()"""
        pass

    @abstractmethod
    def setRightWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setRightWidth(float)"""
        pass

    @abstractmethod
    def getTopHeight(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getTopHeight()"""
        pass

    @abstractmethod
    def setBottomHeight(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setBottomHeight(float)"""
        pass

    @abstractmethod
    def setTopHeight(self, arg0: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.setTopHeight(float)"""
        pass

    @abstractmethod
    def getBottomHeight(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Drawable.getBottomHeight()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Drawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as _BaseDrawable
_BaseDrawable = _BaseDrawable
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.utils.Drawable as _Drawable
_Drawable = _Drawable
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable as _TextureRegionDrawable
_TextureRegionDrawable = _TextureRegionDrawable
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureRegionDrawable():
    """com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable"""
 
    @staticmethod
    def _wrap(java_value: _TextureRegionDrawable) -> 'TextureRegionDrawable':
        return TextureRegionDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureRegionDrawable):
        """
        Dynamic initializer for TextureRegionDrawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureRegionDrawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureRegionDrawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def tint(self, arg0: 'Color') -> 'Drawable':
        """public com.badlogic.gdx.scenes.scene2d.utils.Drawable com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.tint(com.badlogic.gdx.graphics.Color)"""
        return 'Drawable'._wrap(super(_TextureRegionDrawable, self).tint(arg0))

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float._wrap(super(BaseDrawable, self).getTopHeight())

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(_BaseDrawable, self).setRightWidth(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable()"""
        val = _TextureRegionDrawable()
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(_TextureRegionDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable(com.badlogic.gdx.graphics.Texture)"""
        val = _TextureRegionDrawable(arg0)
        self.__wrapper = val

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
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float._wrap(super(BaseDrawable, self).getBottomHeight())

    @overload
    def getRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.getRegion()"""
        return 'g2d.TextureRegion'._wrap(super(TextureRegionDrawable, self).getRegion())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(_BaseDrawable, self).setName(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable()"""
        val = _TextureRegionDrawable()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str._wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(_BaseDrawable, self).setMinHeight(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _TextureRegionDrawable(arg0)
        self.__wrapper = val

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(_BaseDrawable, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float._wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(_TextureRegionDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(_BaseDrawable, self).setMinWidth(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float._wrap(super(BaseDrawable, self).getRightWidth())

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float._wrap(super(BaseDrawable, self).getMinHeight())

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(_BaseDrawable, self).setMinSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(_BaseDrawable, self).setTopHeight(_float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float._wrap(super(BaseDrawable, self).getMinWidth())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(_BaseDrawable, self).setLeftWidth(_float.valueOf(arg0))

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(_BaseDrawable, self).setBottomHeight(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TextureRegionDrawable, self).setRegion(arg0)

    @overload
    def __init__(self, arg0: 'TextureRegionDrawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable(com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable)"""
        val = _TextureRegionDrawable(arg0)
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str._wrap(super(BaseDrawable, self).getName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as _BaseDrawable
_BaseDrawable = _BaseDrawable
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable as _SpriteDrawable
_SpriteDrawable = _SpriteDrawable
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.graphics.g2d.Sprite as _Sprite
_Sprite = _Sprite
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpriteDrawable():
    """com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable"""
 
    @staticmethod
    def _wrap(java_value: _SpriteDrawable) -> 'SpriteDrawable':
        return SpriteDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpriteDrawable):
        """
        Dynamic initializer for SpriteDrawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpriteDrawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpriteDrawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float._wrap(super(BaseDrawable, self).getTopHeight())

    @overload
    def tint(self, arg0: 'Color') -> 'SpriteDrawable':
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.tint(com.badlogic.gdx.graphics.Color)"""
        return 'SpriteDrawable'._wrap(super(_SpriteDrawable, self).tint(arg0))

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(_BaseDrawable, self).setRightWidth(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(_SpriteDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @overload
    def __init__(self, arg0: 'SpriteDrawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable(com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable)"""
        val = _SpriteDrawable(arg0)
        self.__wrapper = val

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
    def setSprite(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.setSprite(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(_SpriteDrawable, self).setSprite(arg0)

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float._wrap(super(BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(_BaseDrawable, self).setName(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str._wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(_BaseDrawable, self).setMinHeight(_float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(_SpriteDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(_BaseDrawable, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float._wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(_BaseDrawable, self).setMinWidth(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float._wrap(super(BaseDrawable, self).getRightWidth())

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float._wrap(super(BaseDrawable, self).getMinHeight())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable()"""
        val = _SpriteDrawable()
        self.__wrapper = val

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(_BaseDrawable, self).setMinSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(_BaseDrawable, self).setTopHeight(_float.valueOf(arg0))

    @overload
    def getSprite(self) -> 'g2d.Sprite':
        """public com.badlogic.gdx.graphics.g2d.Sprite com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.getSprite()"""
        return 'g2d.Sprite'._wrap(super(SpriteDrawable, self).getSprite())

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float._wrap(super(BaseDrawable, self).getMinWidth())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(_BaseDrawable, self).setLeftWidth(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Sprite'):
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable(com.badlogic.gdx.graphics.g2d.Sprite)"""
        val = _SpriteDrawable(arg0)
        self.__wrapper = val

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(_BaseDrawable, self).setBottomHeight(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable()"""
        val = _SpriteDrawable()
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str._wrap(super(BaseDrawable, self).getName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Selection
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import com.badlogic.gdx.scenes.scene2d.utils.Selection as _Selection
_Selection = _Selection
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import com.badlogic.gdx.utils.OrderedSet as _OrderedSet
_OrderedSet = _OrderedSet
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Selection():
    """com.badlogic.gdx.scenes.scene2d.utils.Selection"""
 
    @staticmethod
    def _wrap(java_value: _Selection) -> 'Selection':
        return Selection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Selection):
        """
        Dynamic initializer for Selection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Selection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Selection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setDisabled(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setDisabled(boolean)"""
        super(_Selection, self).setDisabled(_boolean.valueOf(arg0))

    @overload
    def setProgrammaticChangeEvents(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setProgrammaticChangeEvents(boolean)"""
        super(_Selection, self).setProgrammaticChangeEvents(_boolean.valueOf(arg0))

    @overload
    def set(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.set(T)"""
        super(_Selection, self).set(arg0)

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.Selection.size()"""
        return int._wrap(super(Selection, self).size())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.Selection.toString()"""
        return str._wrap(super(Selection, self).toString())

    @overload
    def setAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_Selection, self).setAll(arg0)

    @overload
    def fireChangeEvent(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.fireChangeEvent()"""
        return bool._wrap(super(Selection, self).fireChangeEvent())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.notEmpty()"""
        return bool._wrap(super(Selection, self).notEmpty())

    @overload
    def toArray(self, arg0: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.toArray(com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'._wrap(super(_Selection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.contains(T)"""
        return bool._wrap(super(_Selection, self).contains(arg0))

    @overload
    def getRequired(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getRequired()"""
        return bool._wrap(super(Selection, self).getRequired())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @overload
    def remove(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.remove(T)"""
        super(_Selection, self).remove(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.iterator()"""
        return 'Iterator'._wrap(super(Selection, self).iterator())

    @overload
    def getToggle(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getToggle()"""
        return bool._wrap(super(Selection, self).getToggle())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Selection, self).setActor(arg0)

    @overload
    def setMultiple(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setMultiple(boolean)"""
        super(_Selection, self).setMultiple(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setToggle(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setToggle(boolean)"""
        super(_Selection, self).setToggle(_boolean.valueOf(arg0))

    @overload
    def getLastSelected(self) -> object:
        """public T com.badlogic.gdx.scenes.scene2d.utils.Selection.getLastSelected()"""
        return object._wrap(super(Selection, self).getLastSelected())

    @overload
    def getMultiple(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getMultiple()"""
        return bool._wrap(super(Selection, self).getMultiple())

    @overload
    def hasItems(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.hasItems()"""
        return bool._wrap(super(Selection, self).hasItems())

    @overload
    def toArray(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.toArray()"""
        return 'utils.Array'._wrap(super(Selection, self).toArray())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.clear()"""
        super(Selection, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def items(self) -> 'utils.OrderedSet':
        """public com.badlogic.gdx.utils.OrderedSet<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.items()"""
        return 'utils.OrderedSet'._wrap(super(Selection, self).items())

    @overload
    def setRequired(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setRequired(boolean)"""
        super(_Selection, self).setRequired(_boolean.valueOf(arg0))

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.isEmpty()"""
        return bool._wrap(super(Selection, self).isEmpty())

    @overload
    def addAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.addAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_Selection, self).addAll(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.Selection()"""
        val = _Selection()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def choose(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.choose(T)"""
        super(_Selection, self).choose(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.Selection()"""
        val = _Selection()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.scenes.scene2d.utils.Selection.first()"""
        return object._wrap(super(Selection, self).first())

    @override
    @overload
    def isDisabled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.isDisabled()"""
        return bool._wrap(super(Selection, self).isDisabled())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def removeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.removeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_Selection, self).removeAll(arg0)

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.add(T)"""
        super(_Selection, self).add(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener as _FocusListener_FocusEvent_Type
_Type = _FocusListener_FocusEvent_Type.FocusEvent.Type
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener as _FocusListener_FocusEvent
_FocusEvent = _FocusListener_FocusEvent.FocusEvent
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FocusEvent():
    """com.badlogic.gdx.scenes.scene2d.utils.FocusListener.FocusEvent"""
 
    @staticmethod
    def _wrap(java_value: _FocusEvent) -> 'FocusEvent':
        return FocusEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FocusEvent):
        """
        Dynamic initializer for FocusEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FocusEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FocusEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setCapture(boolean)"""
        super(_scene2d.Event, self).setCapture(_boolean.valueOf(arg0))

    @overload
    def setType(self, arg0: 'Type'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.setType(com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type)"""
        super(_FocusEvent, self).setType(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.getType()"""
        return 'Type'._wrap(super(FocusEvent, self).getType())

    @override
    @overload
    def setStage(self, arg0: 'Stage'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setStage(com.badlogic.gdx.scenes.scene2d.Stage)"""
        super(_scene2d.Event, self).setStage(arg0)

    @override
    @overload
    def getBubbles(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.getBubbles()"""
        return bool._wrap(super(scene2d.Event, self).getBubbles())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isHandled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isHandled()"""
        return bool._wrap(super(scene2d.Event, self).isHandled())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCapture()"""
        return bool._wrap(super(scene2d.Event, self).isCapture())

    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.stop()"""
        super(scene2d.Event, self).stop()

    @override
    @overload
    def setListenerActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setListenerActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Event, self).setListenerActor(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCancelled()"""
        return bool._wrap(super(scene2d.Event, self).isCancelled())

    @overload
    def setFocused(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.setFocused(boolean)"""
        super(_FocusEvent, self).setFocused(_boolean.valueOf(arg0))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Event, self).getTarget())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.reset()"""
        super(FocusEvent, self).reset()

    @overload
    def getRelatedActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.getRelatedActor()"""
        return 'scene2d.Actor'._wrap(super(FocusEvent, self).getRelatedActor())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Event, self).setTarget(arg0)

    @override
    @overload
    def isStopped(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isStopped()"""
        return bool._wrap(super(scene2d.Event, self).isStopped())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStage(self) -> 'scene2d.Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Event.getStage()"""
        return 'scene2d.Stage'._wrap(super(scene2d.Event, self).getStage())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setRelatedActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.setRelatedActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_FocusEvent, self).setRelatedActor(arg0)

    @override
    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.cancel()"""
        super(scene2d.Event, self).cancel()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent()"""
        val = _FocusEvent()
        self.__wrapper = val

    @override
    @overload
    def getListenerActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getListenerActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Event, self).getListenerActor())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setBubbles(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setBubbles(boolean)"""
        super(_scene2d.Event, self).setBubbles(_boolean.valueOf(arg0))

    @overload
    def isFocused(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.isFocused()"""
        return bool._wrap(super(FocusEvent, self).isFocused())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent()"""
        val = _FocusEvent()
        self.__wrapper = val

    @override
    @overload
    def handle(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.handle()"""
        super(scene2d.Event, self).handle()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragListener
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.utils.DragListener as _DragListener
_DragListener = _DragListener
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.InputListener as _InputListener
_InputListener = _InputListener
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DragListener():
    """com.badlogic.gdx.scenes.scene2d.utils.DragListener"""
 
    @staticmethod
    def _wrap(java_value: _DragListener) -> 'DragListener':
        return DragListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DragListener):
        """
        Dynamic initializer for DragListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DragListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DragListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.InputListener, self).exit(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool._wrap(super(_DragListener, self).touchDown(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.DragListener.getButton()"""
        return int._wrap(super(DragListener, self).getButton())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragListener()"""
        val = _DragListener()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragListener()"""
        val = _DragListener()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def dragStop(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.dragStop(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_DragListener, self).dragStop(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getDragX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragX()"""
        return float._wrap(super(DragListener, self).getDragX())

    @overload
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool._wrap(super(_scene2d.InputListener, self).scrolled(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @override
    @overload
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.InputListener, self).enter(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4)

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool._wrap(super(_scene2d.InputListener, self).mouseMoved(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setTapSquareSize(float)"""
        super(_DragListener, self).setTapSquareSize(_float.valueOf(arg0))

    @overload
    def getTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTouchDownX()"""
        return float._wrap(super(DragListener, self).getTouchDownX())

    @overload
    def getDeltaY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDeltaY()"""
        return float._wrap(super(DragListener, self).getDeltaY())

    @override
    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(_DragListener, self).touchUp(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getStageTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getStageTouchDownX()"""
        return float._wrap(super(DragListener, self).getStageTouchDownX())

    @overload
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyUp(arg0, _int.valueOf(arg1)))

    @overload
    def dragStart(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.dragStart(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_DragListener, self).dragStart(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def getDragDistance(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragDistance()"""
        return float._wrap(super(DragListener, self).getDragDistance())

    @overload
    def getTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTouchDownY()"""
        return float._wrap(super(DragListener, self).getTouchDownY())

    @overload
    def getStageTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getStageTouchDownY()"""
        return float._wrap(super(DragListener, self).getStageTouchDownY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setDragStartY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setDragStartY(float)"""
        super(_DragListener, self).setDragStartY(_float.valueOf(arg0))

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_scene2d.InputListener, self).handle(arg0))

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyDown(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isDragging(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragListener.isDragging()"""
        return bool._wrap(super(DragListener, self).isDragging())

    @override
    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_DragListener, self).touchDragged(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def drag(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.drag(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_DragListener, self).drag(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.cancel()"""
        super(DragListener, self).cancel()

    @overload
    def getDeltaX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDeltaX()"""
        return float._wrap(super(DragListener, self).getDeltaX())

    @overload
    def getDragStartX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragStartX()"""
        return float._wrap(super(DragListener, self).getDragStartX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTapSquareSize(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTapSquareSize()"""
        return float._wrap(super(DragListener, self).getTapSquareSize())

    @overload
    def getDragStartY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragStartY()"""
        return float._wrap(super(DragListener, self).getDragStartY())

    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setButton(int)"""
        super(_DragListener, self).setButton(_int.valueOf(arg0))

    @overload
    def getDragY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragY()"""
        return float._wrap(super(DragListener, self).getDragY())

    @overload
    def setDragStartX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setDragStartX(float)"""
        super(_DragListener, self).setDragStartX(_float.valueOf(arg0))

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool._wrap(super(_scene2d.InputListener, self).keyTyped(arg0, _char.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Layout
import com.badlogic.gdx.scenes.scene2d.utils.Layout as _Layout
_Layout = _Layout
from abc import abstractmethod, ABC
 
class Layout():
    """com.badlogic.gdx.scenes.scene2d.utils.Layout"""
 
    @staticmethod
    def _wrap(java_value: _Layout) -> 'Layout':
        return Layout(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Layout):
        """
        Dynamic initializer for Layout.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Layout__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Layout__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getMaxWidth(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Layout.getMaxWidth()"""
        pass

    @abstractmethod
    def layout(self, ):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Layout.layout()"""
        pass

    @abstractmethod
    def pack(self, ):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Layout.pack()"""
        pass

    @abstractmethod
    def invalidate(self, ):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Layout.invalidate()"""
        pass

    @abstractmethod
    def getPrefHeight(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Layout.getPrefHeight()"""
        pass

    @abstractmethod
    def getPrefWidth(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Layout.getPrefWidth()"""
        pass

    @abstractmethod
    def getMaxHeight(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Layout.getMaxHeight()"""
        pass

    @abstractmethod
    def getMinHeight(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Layout.getMinHeight()"""
        pass

    @abstractmethod
    def invalidateHierarchy(self, ):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Layout.invalidateHierarchy()"""
        pass

    @abstractmethod
    def validate(self, ):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Layout.validate()"""
        pass

    @abstractmethod
    def getMinWidth(self, ):
        """public abstract float com.badlogic.gdx.scenes.scene2d.utils.Layout.getMinWidth()"""
        pass

    @abstractmethod
    def setFillParent(self, arg0: bool):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Layout.setFillParent(boolean)"""
        pass

    @abstractmethod
    def setLayoutEnabled(self, arg0: bool):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Layout.setLayoutEnabled(boolean)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.FocusListener
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener as _FocusListener
_FocusListener = _FocusListener
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FocusListener():
    """com.badlogic.gdx.scenes.scene2d.utils.FocusListener"""
 
    @staticmethod
    def _wrap(java_value: _FocusListener) -> 'FocusListener':
        return FocusListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FocusListener):
        """
        Dynamic initializer for FocusListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FocusListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FocusListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.FocusListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_FocusListener, self).handle(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener()"""
        val = _FocusListener()
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

    @overload
    def keyboardFocusChanged(self, arg0: 'FocusEvent', arg1: 'Actor', arg2: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener.keyboardFocusChanged(com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent,com.badlogic.gdx.scenes.scene2d.Actor,boolean)"""
        super(_FocusListener, self).keyboardFocusChanged(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener()"""
        val = _FocusListener()
        self.__wrapper = val

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
    def scrollFocusChanged(self, arg0: 'FocusEvent', arg1: 'Actor', arg2: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener.scrollFocusChanged(com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent,com.badlogic.gdx.scenes.scene2d.Actor,boolean)"""
        super(_FocusListener, self).scrollFocusChanged(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type
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
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener as _FocusListener_FocusEvent_Type
_Type = _FocusListener_FocusEvent_Type.FocusEvent.Type
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """com.badlogic.gdx.scenes.scene2d.utils.FocusListener.FocusEvent.Type"""
 
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

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
    def values() -> List['Type']:
        """public static com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type[] com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type.values()"""
        return List[Type]._wrap(_Type.values())

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as _BaseDrawable
_BaseDrawable = _BaseDrawable
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BaseDrawable():
    """com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable"""
 
    @staticmethod
    def _wrap(java_value: _BaseDrawable) -> 'BaseDrawable':
        return BaseDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BaseDrawable):
        """
        Dynamic initializer for BaseDrawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BaseDrawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BaseDrawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float._wrap(super(BaseDrawable, self).getTopHeight())

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(_BaseDrawable, self).setRightWidth(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(_BaseDrawable, self).setName(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable()"""
        val = _BaseDrawable()
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str._wrap(super(BaseDrawable, self).getName())

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
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float._wrap(super(BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str._wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(_BaseDrawable, self).setMinHeight(_float.valueOf(arg0))

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float._wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(_BaseDrawable, self).setMinWidth(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float._wrap(super(BaseDrawable, self).getRightWidth())

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float._wrap(super(BaseDrawable, self).getMinHeight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Drawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable(com.badlogic.gdx.scenes.scene2d.utils.Drawable)"""
        val = _BaseDrawable(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable()"""
        val = _BaseDrawable()
        self.__wrapper = val

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(_BaseDrawable, self).setTopHeight(_float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(_BaseDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float._wrap(super(BaseDrawable, self).getMinWidth())

    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(_BaseDrawable, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(_BaseDrawable, self).setMinSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(_BaseDrawable, self).setLeftWidth(_float.valueOf(arg0))

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(_BaseDrawable, self).setBottomHeight(_float.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as _DragAndDrop_Target
_Target = _DragAndDrop_Target.Target
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
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
 
class Target():
    """com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.Target"""
 
    @staticmethod
    def _wrap(java_value: _Target) -> 'Target':
        return Target(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Target):
        """
        Dynamic initializer for Target.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Target__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Target__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def drop(self, arg0: 'Source', arg1: 'Payload', arg2: float, arg3: float, arg4: int):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target.drop(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload,float,float,int)"""
        pass

    @abstractmethod
    def drag(self, arg0: 'Source', arg1: 'Payload', arg2: float, arg3: float, arg4: int):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target.drag(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload,float,float,int)"""
        pass

    @overload
    def reset(self, arg0: 'Source', arg1: 'Payload'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target.reset(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload)"""
        super(_Target, self).reset(arg0, arg1)

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target.getActor()"""
        return 'scene2d.Actor'._wrap(super(Target, self).getActor())

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
    def __init__(self, arg0: 'Actor'):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target(com.badlogic.gdx.scenes.scene2d.Actor)"""
        val = _Target(arg0)
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Cullable
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from abc import abstractmethod, ABC
import com.badlogic.gdx.scenes.scene2d.utils.Cullable as _Cullable
_Cullable = _Cullable
 
class Cullable():
    """com.badlogic.gdx.scenes.scene2d.utils.Cullable"""
 
    @staticmethod
    def _wrap(java_value: _Cullable) -> 'Cullable':
        return Cullable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Cullable):
        """
        Dynamic initializer for Cullable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Cullable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Cullable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setCullingArea(self, arg0: 'Rectangle'):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Cullable.setCullingArea(com.badlogic.gdx.math.Rectangle)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Disableable
from abc import abstractmethod, ABC
import com.badlogic.gdx.scenes.scene2d.utils.Disableable as _Disableable
_Disableable = _Disableable
 
class Disableable():
    """com.badlogic.gdx.scenes.scene2d.utils.Disableable"""
 
    @staticmethod
    def _wrap(java_value: _Disableable) -> 'Disableable':
        return Disableable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Disableable):
        """
        Dynamic initializer for Disableable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Disableable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Disableable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setDisabled(self, arg0: bool):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Disableable.setDisabled(boolean)"""
        pass

    @abstractmethod
    def isDisabled(self, ):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.utils.Disableable.isDisabled()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as _BaseDrawable
_BaseDrawable = _BaseDrawable
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable as _NinePatchDrawable
_NinePatchDrawable = _NinePatchDrawable
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.graphics.g2d.NinePatch as _NinePatch
_NinePatch = _NinePatch
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NinePatchDrawable():
    """com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable"""
 
    @staticmethod
    def _wrap(java_value: _NinePatchDrawable) -> 'NinePatchDrawable':
        return NinePatchDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NinePatchDrawable):
        """
        Dynamic initializer for NinePatchDrawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NinePatchDrawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NinePatchDrawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float._wrap(super(BaseDrawable, self).getTopHeight())

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(_BaseDrawable, self).setRightWidth(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'NinePatch'):
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable(com.badlogic.gdx.graphics.g2d.NinePatch)"""
        val = _NinePatchDrawable(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable()"""
        val = _NinePatchDrawable()
        self.__wrapper = val

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
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float._wrap(super(BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(_BaseDrawable, self).setName(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str._wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(_BaseDrawable, self).setMinHeight(_float.valueOf(arg0))

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(_BaseDrawable, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float._wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(_BaseDrawable, self).setMinWidth(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float._wrap(super(BaseDrawable, self).getRightWidth())

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float._wrap(super(BaseDrawable, self).getMinHeight())

    @overload
    def setPatch(self, arg0: 'NinePatch'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.setPatch(com.badlogic.gdx.graphics.g2d.NinePatch)"""
        super(_NinePatchDrawable, self).setPatch(arg0)

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(_BaseDrawable, self).setMinSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable()"""
        val = _NinePatchDrawable()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'NinePatchDrawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable(com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable)"""
        val = _NinePatchDrawable(arg0)
        self.__wrapper = val

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(_BaseDrawable, self).setTopHeight(_float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float._wrap(super(BaseDrawable, self).getMinWidth())

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(_NinePatchDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(_NinePatchDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(_BaseDrawable, self).setLeftWidth(_float.valueOf(arg0))

    @overload
    def getPatch(self) -> 'g2d.NinePatch':
        """public com.badlogic.gdx.graphics.g2d.NinePatch com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.getPatch()"""
        return 'g2d.NinePatch'._wrap(super(NinePatchDrawable, self).getPatch())

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(_BaseDrawable, self).setBottomHeight(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def tint(self, arg0: 'Color') -> 'NinePatchDrawable':
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.tint(com.badlogic.gdx.graphics.Color)"""
        return 'NinePatchDrawable'._wrap(super(_NinePatchDrawable, self).tint(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str._wrap(super(BaseDrawable, self).getName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ArraySelection
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import com.badlogic.gdx.utils.OrderedSet as _OrderedSet
_OrderedSet = _OrderedSet
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import com.badlogic.gdx.scenes.scene2d.utils.ArraySelection as _ArraySelection
_ArraySelection = _ArraySelection
import java.lang.String as _String
_String = _String
from builtins import object
import com.badlogic.gdx.scenes.scene2d.utils.Selection as _Selection
_Selection = _Selection
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArraySelection():
    """com.badlogic.gdx.scenes.scene2d.utils.ArraySelection"""
 
    @staticmethod
    def _wrap(java_value: _ArraySelection) -> 'ArraySelection':
        return ArraySelection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArraySelection):
        """
        Dynamic initializer for ArraySelection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArraySelection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArraySelection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def validate(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ArraySelection.validate()"""
        super(ArraySelection, self).validate()

    @override
    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.add(T)"""
        super(_Selection, self).add(arg0)

    @override
    @overload
    def setProgrammaticChangeEvents(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setProgrammaticChangeEvents(boolean)"""
        super(_Selection, self).setProgrammaticChangeEvents(_boolean.valueOf(arg0))

    @override
    @overload
    def setDisabled(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setDisabled(boolean)"""
        super(_Selection, self).setDisabled(_boolean.valueOf(arg0))

    @override
    @overload
    def choose(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ArraySelection.choose(T)"""
        super(_ArraySelection, self).choose(arg0)

    @override
    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.Selection.size()"""
        return int._wrap(super(Selection, self).size())

    @override
    @overload
    def addAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.addAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_Selection, self).addAll(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.Selection.toString()"""
        return str._wrap(super(Selection, self).toString())

    @override
    @overload
    def getRequired(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getRequired()"""
        return bool._wrap(super(Selection, self).getRequired())

    @override
    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.notEmpty()"""
        return bool._wrap(super(Selection, self).notEmpty())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setMultiple(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setMultiple(boolean)"""
        super(_Selection, self).setMultiple(_boolean.valueOf(arg0))

    @override
    @overload
    def getToggle(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getToggle()"""
        return bool._wrap(super(Selection, self).getToggle())

    @overload
    def toArray(self, arg0: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.toArray(com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'._wrap(super(_Selection, self).toArray(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.contains(T)"""
        return bool._wrap(super(_Selection, self).contains(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.scenes.scene2d.utils.ArraySelection(com.badlogic.gdx.utils.Array<T>)"""
        val = _ArraySelection(arg0)
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.clear()"""
        super(Selection, self).clear()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.iterator()"""
        return 'Iterator'._wrap(super(Selection, self).iterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getRangeSelect(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ArraySelection.getRangeSelect()"""
        return bool._wrap(super(ArraySelection, self).getRangeSelect())

    @override
    @overload
    def fireChangeEvent(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.fireChangeEvent()"""
        return bool._wrap(super(Selection, self).fireChangeEvent())

    @override
    @overload
    def hasItems(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.hasItems()"""
        return bool._wrap(super(Selection, self).hasItems())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setRangeSelect(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ArraySelection.setRangeSelect(boolean)"""
        super(_ArraySelection, self).setRangeSelect(_boolean.valueOf(arg0))

    @override
    @overload
    def getMultiple(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getMultiple()"""
        return bool._wrap(super(Selection, self).getMultiple())

    @override
    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.scenes.scene2d.utils.Selection.first()"""
        return object._wrap(super(Selection, self).first())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setToggle(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setToggle(boolean)"""
        super(_Selection, self).setToggle(_boolean.valueOf(arg0))

    @override
    @overload
    def items(self) -> 'utils.OrderedSet':
        """public com.badlogic.gdx.utils.OrderedSet<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.items()"""
        return 'utils.OrderedSet'._wrap(super(Selection, self).items())

    @override
    @overload
    def setAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_Selection, self).setAll(arg0)

    @override
    @overload
    def set(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.set(T)"""
        super(_Selection, self).set(arg0)

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Selection, self).setActor(arg0)

    @override
    @overload
    def getLastSelected(self) -> object:
        """public T com.badlogic.gdx.scenes.scene2d.utils.Selection.getLastSelected()"""
        return object._wrap(super(Selection, self).getLastSelected())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setRequired(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setRequired(boolean)"""
        super(_Selection, self).setRequired(_boolean.valueOf(arg0))

    @override
    @overload
    def toArray(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.toArray()"""
        return 'utils.Array'._wrap(super(Selection, self).toArray())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isDisabled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.isDisabled()"""
        return bool._wrap(super(Selection, self).isDisabled())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.isEmpty()"""
        return bool._wrap(super(Selection, self).isEmpty())

    @override
    @overload
    def removeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.removeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_Selection, self).removeAll(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def remove(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.remove(T)"""
        super(_Selection, self).remove(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ScissorStack
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.math.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.lang.Long as _long
import com.badlogic.gdx.scenes.scene2d.utils.ScissorStack as _ScissorStack
_ScissorStack = _ScissorStack
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScissorStack():
    """com.badlogic.gdx.scenes.scene2d.utils.ScissorStack"""
 
    @staticmethod
    def _wrap(java_value: _ScissorStack) -> 'ScissorStack':
        return ScissorStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScissorStack):
        """
        Dynamic initializer for ScissorStack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScissorStack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScissorStack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def calculateScissors(arg0: 'Camera', arg1: 'Matrix4', arg2: 'Rectangle', arg3: 'Rectangle'):
        """public static void com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.calculateScissors(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        _ScissorStack.calculateScissors(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def getViewport() -> 'math.Rectangle':
        """public static com.badlogic.gdx.math.Rectangle com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.getViewport()"""
        return math.Rectangle._wrap(_ScissorStack.getViewport())

    @staticmethod
    @overload
    def pushScissors(arg0: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.pushScissors(com.badlogic.gdx.math.Rectangle)"""
        return bool._wrap(_ScissorStack.pushScissors(arg0))

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

    @staticmethod
    @overload
    def popScissors() -> 'math.Rectangle':
        """public static com.badlogic.gdx.math.Rectangle com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.popScissors()"""
        return math.Rectangle._wrap(_ScissorStack.popScissors())

    @staticmethod
    @overload
    def peekScissors() -> 'math.Rectangle':
        """public static com.badlogic.gdx.math.Rectangle com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.peekScissors()"""
        return math.Rectangle._wrap(_ScissorStack.peekScissors())

    @staticmethod
    @overload
    def calculateScissors(arg0: 'Camera', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Matrix4', arg6: 'Rectangle', arg7: 'Rectangle'):
        """public static void com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.calculateScissors(com.badlogic.gdx.graphics.Camera,float,float,float,float,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        _ScissorStack.calculateScissors(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6, arg7)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.ScissorStack()"""
        val = _ScissorStack()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ScissorStack()"""
        val = _ScissorStack()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as _DragAndDrop_Payload
_Payload = _DragAndDrop_Payload.Payload
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Payload():
    """com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.Payload"""
 
    @staticmethod
    def _wrap(java_value: _Payload) -> 'Payload':
        return Payload(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Payload):
        """
        Dynamic initializer for Payload.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Payload__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Payload__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setDragActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.setDragActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Payload, self).setDragActor(arg0)

    @overload
    def getObject(self) -> object:
        """public java.lang.Object com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.getObject()"""
        return object._wrap(super(Payload, self).getObject())

    @overload
    def getDragActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.getDragActor()"""
        return 'scene2d.Actor'._wrap(super(Payload, self).getDragActor())

    @overload
    def setInvalidDragActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.setInvalidDragActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Payload, self).setInvalidDragActor(arg0)

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

    @overload
    def getValidDragActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.getValidDragActor()"""
        return 'scene2d.Actor'._wrap(super(Payload, self).getValidDragActor())

    @overload
    def setValidDragActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.setValidDragActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_Payload, self).setValidDragActor(arg0)

    @overload
    def setObject(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.setObject(java.lang.Object)"""
        super(_Payload, self).setObject(arg0)

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
    def getInvalidDragActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.getInvalidDragActor()"""
        return 'scene2d.Actor'._wrap(super(Payload, self).getInvalidDragActor())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload()"""
        val = _Payload()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload()"""
        val = _Payload()
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as _DragAndDrop
_DragAndDrop = _DragAndDrop
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as _DragAndDrop_Payload
_Payload = _DragAndDrop_Payload.Payload
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as _DragAndDrop_Source
_Source = _DragAndDrop_Source.Source
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DragAndDrop():
    """com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop"""
 
    @staticmethod
    def _wrap(java_value: _DragAndDrop) -> 'DragAndDrop':
        return DragAndDrop(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DragAndDrop):
        """
        Dynamic initializer for DragAndDrop.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DragAndDrop__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DragAndDrop__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setButton(int)"""
        super(_DragAndDrop, self).setButton(_int.valueOf(arg0))

    @overload
    def getDragActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.getDragActor()"""
        return 'scene2d.Actor'._wrap(super(DragAndDrop, self).getDragActor())

    @overload
    def isDragValid(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.isDragValid()"""
        return bool._wrap(super(DragAndDrop, self).isDragValid())

    @overload
    def removeTarget(self, arg0: 'Target'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.removeTarget(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target)"""
        super(_DragAndDrop, self).removeTarget(arg0)

    @overload
    def getDragTime(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.getDragTime()"""
        return int._wrap(super(DragAndDrop, self).getDragTime())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isDragging(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.isDragging()"""
        return bool._wrap(super(DragAndDrop, self).isDragging())

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
    def setTouchOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setTouchOffset(float,float)"""
        super(_DragAndDrop, self).setTouchOffset(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def removeSource(self, arg0: 'Source'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.removeSource(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source)"""
        super(_DragAndDrop, self).removeSource(arg0)

    @overload
    def getDragPayload(self) -> 'Payload':
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.getDragPayload()"""
        return 'Payload'._wrap(super(DragAndDrop, self).getDragPayload())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop()"""
        val = _DragAndDrop()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setKeepWithinStage(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setKeepWithinStage(boolean)"""
        super(_DragAndDrop, self).setKeepWithinStage(_boolean.valueOf(arg0))

    @overload
    def getDragSource(self) -> 'Source':
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.getDragSource()"""
        return 'Source'._wrap(super(DragAndDrop, self).getDragSource())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.clear()"""
        super(DragAndDrop, self).clear()

    @overload
    def addSource(self, arg0: 'Source'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.addSource(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source)"""
        super(_DragAndDrop, self).addSource(arg0)

    @overload
    def setDragActorPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setDragActorPosition(float,float)"""
        super(_DragAndDrop, self).setDragActorPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setTapSquareSize(float)"""
        super(_DragAndDrop, self).setTapSquareSize(_float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def cancelTouchFocusExcept(self, arg0: 'Source'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.cancelTouchFocusExcept(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source)"""
        super(_DragAndDrop, self).cancelTouchFocusExcept(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setCancelTouchFocus(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setCancelTouchFocus(boolean)"""
        super(_DragAndDrop, self).setCancelTouchFocus(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setDragTime(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setDragTime(int)"""
        super(_DragAndDrop, self).setDragTime(_int.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop()"""
        val = _DragAndDrop()
        self.__wrapper = val

    @overload
    def addTarget(self, arg0: 'Target'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.addTarget(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target)"""
        super(_DragAndDrop, self).addTarget(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as _DragAndDrop_Source
_Source = _DragAndDrop_Source.Source
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Source():
    """com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.Source"""
 
    @staticmethod
    def _wrap(java_value: _Source) -> 'Source':
        return Source(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Source):
        """
        Dynamic initializer for Source.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Source__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Source__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.getActor()"""
        return 'scene2d.Actor'._wrap(super(Source, self).getActor())

    @overload
    def dragStop(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Payload', arg5: 'Target'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.dragStop(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target)"""
        super(_Source, self).dragStop(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5)

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
    def __init__(self, arg0: 'Actor'):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source(com.badlogic.gdx.scenes.scene2d.Actor)"""
        val = _Source(arg0)
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def drag(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.drag(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(_Source, self).drag(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

    @abstractmethod
    def dragStart(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public abstract com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.dragStart(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        pass

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ChangeListener
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener as _ChangeListener
_ChangeListener = _ChangeListener
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChangeListener():
    """com.badlogic.gdx.scenes.scene2d.utils.ChangeListener"""
 
    @staticmethod
    def _wrap(java_value: _ChangeListener) -> 'ChangeListener':
        return ChangeListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChangeListener):
        """
        Dynamic initializer for ChangeListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChangeListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChangeListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public com.badlogic.gdx.scenes.scene2d.utils.ChangeListener()"""
        val = _ChangeListener()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def changed(self, arg0: 'ChangeEvent', arg1: 'Actor'):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.ChangeListener.changed(com.badlogic.gdx.scenes.scene2d.utils.ChangeListener$ChangeEvent,com.badlogic.gdx.scenes.scene2d.Actor)"""
        pass

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ChangeListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool._wrap(super(_ChangeListener, self).handle(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.ChangeListener()"""
        val = _ChangeListener()
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as _BaseDrawable
_BaseDrawable = _BaseDrawable
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable as _TiledDrawable
_TiledDrawable = _TiledDrawable
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable as _TextureRegionDrawable
_TextureRegionDrawable = _TextureRegionDrawable
import java.lang.Class as _Class
_Class = _Class
 
class TiledDrawable():
    """com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable"""
 
    @staticmethod
    def _wrap(java_value: _TiledDrawable) -> 'TiledDrawable':
        return TiledDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TiledDrawable):
        """
        Dynamic initializer for TiledDrawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TiledDrawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TiledDrawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float._wrap(super(BaseDrawable, self).getTopHeight())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable()"""
        val = _TiledDrawable()
        self.__wrapper = val

    @overload
    def getScale(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.getScale()"""
        return float._wrap(super(TiledDrawable, self).getScale())

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(_BaseDrawable, self).setRightWidth(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable()"""
        val = _TiledDrawable()
        self.__wrapper = val

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
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float._wrap(super(BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TextureRegionDrawable, self).setRegion(arg0)

    @overload
    def getAlign(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.getAlign()"""
        return int._wrap(super(TiledDrawable, self).getAlign())

    @staticmethod
    @overload
    def draw(arg0: 'Batch', arg1: 'TextureRegion', arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,int)"""
        _TiledDrawable.draw(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7))

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(_BaseDrawable, self).setName(arg0)

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _TiledDrawable(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str._wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(_BaseDrawable, self).setMinHeight(_float.valueOf(arg0))

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(_BaseDrawable, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float._wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(_BaseDrawable, self).setMinWidth(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float._wrap(super(BaseDrawable, self).getRightWidth())

    @overload
    def setAlign(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.setAlign(int)"""
        super(_TiledDrawable, self).setAlign(_int.valueOf(arg0))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float._wrap(super(BaseDrawable, self).getMinHeight())

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(_BaseDrawable, self).setMinSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.getRegion()"""
        return 'g2d.TextureRegion'._wrap(super(TextureRegionDrawable, self).getRegion())

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(_BaseDrawable, self).setTopHeight(_float.valueOf(arg0))

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.setScale(float)"""
        super(_TiledDrawable, self).setScale(_float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float._wrap(super(BaseDrawable, self).getMinWidth())

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.getColor()"""
        return 'graphics.Color'._wrap(super(TiledDrawable, self).getColor())

    @overload
    def __init__(self, arg0: 'TextureRegionDrawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable(com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable)"""
        val = _TiledDrawable(arg0)
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(_TiledDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(_BaseDrawable, self).setLeftWidth(_float.valueOf(arg0))

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(_BaseDrawable, self).setBottomHeight(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def tint(self, arg0: 'Color') -> 'TiledDrawable':
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.tint(com.badlogic.gdx.graphics.Color)"""
        return 'TiledDrawable'._wrap(super(_TiledDrawable, self).tint(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(_TiledDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str._wrap(super(BaseDrawable, self).getName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())
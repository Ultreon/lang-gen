from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.EventAction as _EventAction
_EventAction = _EventAction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventAction():
    """com.badlogic.gdx.scenes.scene2d.actions.EventAction"""
 
    @staticmethod
    def _wrap(java_value: _EventAction) -> 'EventAction':
        return EventAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventAction):
        """
        Dynamic initializer for EventAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self, arg0: 'Class'):
        """public com.badlogic.gdx.scenes.scene2d.actions.EventAction(java.lang.Class<? extends T>)"""
        val = _EventAction(arg0)
        self.__wrapper = val

    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setActive(boolean)"""
        super(_EventAction, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.act(float)"""
        return bool._wrap(super(_EventAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.restart()"""
        super(EventAction, self).restart()

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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.isActive()"""
        return bool._wrap(super(EventAction, self).isActive())

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_EventAction, self).setTarget(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

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

    @abstractmethod
    def handle(self, arg0: 'Event'):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.handle(T)"""
        pass

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

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

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.EventAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.EventAction as _EventAction
_EventAction = _EventAction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventAction():
    """com.badlogic.gdx.scenes.scene2d.actions.EventAction"""
 
    @staticmethod
    def _wrap(java_value: _EventAction) -> 'EventAction':
        return EventAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventAction):
        """
        Dynamic initializer for EventAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self, arg0: 'Class'):
        """public com.badlogic.gdx.scenes.scene2d.actions.EventAction(java.lang.Class<? extends T>)"""
        val = _EventAction(arg0)
        self.__wrapper = val

    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setActive(boolean)"""
        super(_EventAction, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.act(float)"""
        return bool._wrap(super(_EventAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.restart()"""
        super(EventAction, self).restart()

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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.isActive()"""
        return bool._wrap(super(EventAction, self).isActive())

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_EventAction, self).setTarget(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

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

    @abstractmethod
    def handle(self, arg0: 'Event'):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.handle(T)"""
        pass

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

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

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.EventAction 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.AfterAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import com.badlogic.gdx.scenes.scene2d.actions.AfterAction as _AfterAction
_AfterAction = _AfterAction
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as _DelegateAction
_DelegateAction = _DelegateAction
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AfterAction():
    """com.badlogic.gdx.scenes.scene2d.actions.AfterAction"""
 
    @staticmethod
    def _wrap(java_value: _AfterAction) -> 'AfterAction':
        return AfterAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AfterAction):
        """
        Dynamic initializer for AfterAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AfterAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AfterAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str._wrap(super(DelegateAction, self).toString())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.AfterAction()"""
        val = _AfterAction()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.AfterAction()"""
        val = _AfterAction()
        self.__wrapper = val

    @override
    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'._wrap(super(DelegateAction, self).getAction())

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_DelegateAction, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AfterAction.restart()"""
        super(AfterAction, self).restart()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool._wrap(super(_DelegateAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_DelegateAction, self).setAction(arg0)

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AfterAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_AfterAction, self).setTarget(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction as _ScaleByAction
_ScaleByAction = _ScaleByAction
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScaleByAction():
    """com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction"""
 
    @staticmethod
    def _wrap(java_value: _ScaleByAction) -> 'ScaleByAction':
        return ScaleByAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScaleByAction):
        """
        Dynamic initializer for ScaleByAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScaleByAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScaleByAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @overload
    def getAmountX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.getAmountX()"""
        return float._wrap(super(ScaleByAction, self).getAmountX())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction()"""
        val = _ScaleByAction()
        self.__wrapper = val

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def setAmount(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.setAmount(float,float)"""
        super(_ScaleByAction, self).setAmount(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @overload
    def setAmountX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.setAmountX(float)"""
        super(_ScaleByAction, self).setAmountX(_float.valueOf(arg0))

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def setAmountY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.setAmountY(float)"""
        super(_ScaleByAction, self).setAmountY(_float.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @overload
    def setAmount(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.setAmount(float)"""
        super(_ScaleByAction, self).setAmount(_float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getAmountY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.getAmountY()"""
        return float._wrap(super(ScaleByAction, self).getAmountY())

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction()"""
        val = _ScaleByAction()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.Actions
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction as _ScaleToAction
_ScaleToAction = _ScaleToAction
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.LayoutAction as _LayoutAction
_LayoutAction = _LayoutAction
import com.badlogic.gdx.scenes.scene2d.actions.SizeByAction as _SizeByAction
_SizeByAction = _SizeByAction
import com.badlogic.gdx.scenes.scene2d.actions.DelayAction as _DelayAction
_DelayAction = _DelayAction
import com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction as _TimeScaleAction
_TimeScaleAction = _TimeScaleAction
import java.lang.Boolean as _boolean
import com.badlogic.gdx.scenes.scene2d.actions.RemoveAction as _RemoveAction
_RemoveAction = _RemoveAction
import com.badlogic.gdx.scenes.scene2d.actions.SequenceAction as _SequenceAction
_SequenceAction = _SequenceAction
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.scenes.scene2d.actions.VisibleAction as _VisibleAction
_VisibleAction = _VisibleAction
import com.badlogic.gdx.scenes.scene2d.actions.MoveByAction as _MoveByAction
_MoveByAction = _MoveByAction
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
import com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction as _RemoveActorAction
_RemoveActorAction = _RemoveActorAction
from builtins import str
import com.badlogic.gdx.scenes.scene2d.actions.SizeToAction as _SizeToAction
_SizeToAction = _SizeToAction
from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.AlphaAction as _AlphaAction
_AlphaAction = _AlphaAction
import com.badlogic.gdx.scenes.scene2d.actions.TouchableAction as _TouchableAction
_TouchableAction = _TouchableAction
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import com.badlogic.gdx.scenes.scene2d.actions.AfterAction as _AfterAction
_AfterAction = _AfterAction
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.actions.ColorAction as _ColorAction
_ColorAction = _ColorAction
import com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction as _RemoveListenerAction
_RemoveListenerAction = _RemoveListenerAction
import com.badlogic.gdx.scenes.scene2d.actions.ParallelAction as _ParallelAction
_ParallelAction = _ParallelAction
import java.lang.Float as _float
import com.badlogic.gdx.scenes.scene2d.actions.AddAction as _AddAction
_AddAction = _AddAction
import com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction as _AddListenerAction
_AddListenerAction = _AddListenerAction
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.RepeatAction as _RepeatAction
_RepeatAction = _RepeatAction
import com.badlogic.gdx.scenes.scene2d.actions.MoveToAction as _MoveToAction
_MoveToAction = _MoveToAction
import com.badlogic.gdx.scenes.scene2d.actions.RotateByAction as _RotateByAction
_RotateByAction = _RotateByAction
import com.badlogic.gdx.scenes.scene2d.actions.RunnableAction as _RunnableAction
_RunnableAction = _RunnableAction
import com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction as _ScaleByAction
_ScaleByAction = _ScaleByAction
import com.badlogic.gdx.scenes.scene2d.actions.RotateToAction as _RotateToAction
_RotateToAction = _RotateToAction
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
import com.badlogic.gdx.scenes.scene2d.actions.Actions as _Actions
_Actions = _Actions
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Actions():
    """com.badlogic.gdx.scenes.scene2d.actions.Actions"""
 
    @staticmethod
    def _wrap(java_value: _Actions) -> 'Actions':
        return Actions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Actions):
        """
        Dynamic initializer for Actions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Actions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Actions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def rotateTo(arg0: float, arg1: float, arg2: 'Interpolation') -> 'RotateToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateTo(float,float,com.badlogic.gdx.math.Interpolation)"""
        return RotateToAction._wrap(_Actions.rotateTo(_float.valueOf(arg0), _float.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def targeting(arg0: 'Actor', arg1: 'Action') -> 'scene2d.Action':
        """public static com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.Actions.targeting(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Action)"""
        return scene2d.Action._wrap(_Actions.targeting(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def addAction(arg0: 'Action', arg1: 'Actor') -> 'AddAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AddAction com.badlogic.gdx.scenes.scene2d.actions.Actions.addAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return AddAction._wrap(_Actions.addAction(arg0, arg1))

    @staticmethod
    @overload
    def moveTo(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveTo(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return MoveToAction._wrap(_Actions.moveTo(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def sizeBy(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'SizeByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeBy(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return SizeByAction._wrap(_Actions.sizeBy(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def parallel(arg0: 'Action', arg1: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction._wrap(_Actions.parallel(arg0, arg1))

    @staticmethod
    @overload
    def sequence(arg0: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction._wrap(_Actions.sequence(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def rotateBy(arg0: float) -> 'RotateByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateBy(float)"""
        return RotateByAction._wrap(_Actions.rotateBy(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def sequence(arg0: 'Action', arg1: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction._wrap(_Actions.sequence(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def alpha(arg0: float, arg1: float) -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.alpha(float,float)"""
        return AlphaAction._wrap(_Actions.alpha(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def after(arg0: 'Action') -> 'AfterAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AfterAction com.badlogic.gdx.scenes.scene2d.actions.Actions.after(com.badlogic.gdx.scenes.scene2d.Action)"""
        return AfterAction._wrap(_Actions.after(arg0))

    @staticmethod
    @overload
    def removeAction(arg0: 'Action', arg1: 'Actor') -> 'RemoveAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return RemoveAction._wrap(_Actions.removeAction(arg0, arg1))

    @staticmethod
    @overload
    def sequence(*arg0: 'scene2d.Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action...)"""
        return SequenceAction._wrap(_Actions.sequence(arg0))

    @staticmethod
    @overload
    def fadeOut(arg0: float) -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.fadeOut(float)"""
        return AlphaAction._wrap(_Actions.fadeOut(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def layout(arg0: bool) -> 'LayoutAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.LayoutAction com.badlogic.gdx.scenes.scene2d.actions.Actions.layout(boolean)"""
        return LayoutAction._wrap(_Actions.layout(_boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def run(arg0: 'Runnable') -> 'RunnableAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RunnableAction com.badlogic.gdx.scenes.scene2d.actions.Actions.run(java.lang.Runnable)"""
        return RunnableAction._wrap(_Actions.run(arg0))

    @staticmethod
    @overload
    def removeActor() -> 'RemoveActorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeActor()"""
        return RemoveActorAction._wrap(_Actions.removeActor())

    @staticmethod
    @overload
    def color(arg0: 'Color', arg1: float) -> 'ColorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ColorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.color(com.badlogic.gdx.graphics.Color,float)"""
        return ColorAction._wrap(_Actions.color(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def moveToAligned(arg0: float, arg1: float, arg2: int, arg3: float, arg4: 'Interpolation') -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveToAligned(float,float,int,float,com.badlogic.gdx.math.Interpolation)"""
        return MoveToAction._wrap(_Actions.moveToAligned(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def scaleTo(arg0: float, arg1: float) -> 'ScaleToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleTo(float,float)"""
        return ScaleToAction._wrap(_Actions.scaleTo(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def rotateTo(arg0: float) -> 'RotateToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateTo(float)"""
        return RotateToAction._wrap(_Actions.rotateTo(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def sequence(arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action', arg4: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction._wrap(_Actions.sequence(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def moveToAligned(arg0: float, arg1: float, arg2: int) -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveToAligned(float,float,int)"""
        return MoveToAction._wrap(_Actions.moveToAligned(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def fadeOut(arg0: float, arg1: 'Interpolation') -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.fadeOut(float,com.badlogic.gdx.math.Interpolation)"""
        return AlphaAction._wrap(_Actions.fadeOut(_float.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def sizeTo(arg0: float, arg1: float) -> 'SizeToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeTo(float,float)"""
        return SizeToAction._wrap(_Actions.sizeTo(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def scaleTo(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'ScaleToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleTo(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return ScaleToAction._wrap(_Actions.scaleTo(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def alpha(arg0: float, arg1: float, arg2: 'Interpolation') -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.alpha(float,float,com.badlogic.gdx.math.Interpolation)"""
        return AlphaAction._wrap(_Actions.alpha(_float.valueOf(arg0), _float.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def addListener(arg0: 'EventListener', arg1: bool) -> 'AddListenerAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction com.badlogic.gdx.scenes.scene2d.actions.Actions.addListener(com.badlogic.gdx.scenes.scene2d.EventListener,boolean)"""
        return AddListenerAction._wrap(_Actions.addListener(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def scaleBy(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'ScaleByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleBy(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return ScaleByAction._wrap(_Actions.scaleBy(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def color(arg0: 'Color') -> 'ColorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ColorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.color(com.badlogic.gdx.graphics.Color)"""
        return ColorAction._wrap(_Actions.color(arg0))

    @staticmethod
    @overload
    def sizeTo(arg0: float, arg1: float, arg2: float) -> 'SizeToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeTo(float,float,float)"""
        return SizeToAction._wrap(_Actions.sizeTo(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.Actions()"""
        val = _Actions()
        self.__wrapper = val

    @staticmethod
    @overload
    def rotateTo(arg0: float, arg1: float) -> 'RotateToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateTo(float,float)"""
        return RotateToAction._wrap(_Actions.rotateTo(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def timeScale(arg0: float, arg1: 'Action') -> 'TimeScaleAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction com.badlogic.gdx.scenes.scene2d.actions.Actions.timeScale(float,com.badlogic.gdx.scenes.scene2d.Action)"""
        return TimeScaleAction._wrap(_Actions.timeScale(_float.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def sizeBy(arg0: float, arg1: float, arg2: float) -> 'SizeByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeBy(float,float,float)"""
        return SizeByAction._wrap(_Actions.sizeBy(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def parallel(arg0: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction._wrap(_Actions.parallel(arg0))

    @staticmethod
    @overload
    def repeat(arg0: int, arg1: 'Action') -> 'RepeatAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RepeatAction com.badlogic.gdx.scenes.scene2d.actions.Actions.repeat(int,com.badlogic.gdx.scenes.scene2d.Action)"""
        return RepeatAction._wrap(_Actions.repeat(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def parallel(arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction._wrap(_Actions.parallel(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.Actions()"""
        val = _Actions()
        self.__wrapper = val

    @staticmethod
    @overload
    def delay(arg0: float) -> 'DelayAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.DelayAction com.badlogic.gdx.scenes.scene2d.actions.Actions.delay(float)"""
        return DelayAction._wrap(_Actions.delay(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def hide() -> 'VisibleAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.VisibleAction com.badlogic.gdx.scenes.scene2d.actions.Actions.hide()"""
        return VisibleAction._wrap(_Actions.hide())

    @staticmethod
    @overload
    def addListener(arg0: 'EventListener', arg1: bool, arg2: 'Actor') -> 'AddListenerAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction com.badlogic.gdx.scenes.scene2d.actions.Actions.addListener(com.badlogic.gdx.scenes.scene2d.EventListener,boolean,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return AddListenerAction._wrap(_Actions.addListener(arg0, _boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def moveBy(arg0: float, arg1: float) -> 'MoveByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveBy(float,float)"""
        return MoveByAction._wrap(_Actions.moveBy(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def scaleBy(arg0: float, arg1: float, arg2: float) -> 'ScaleByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleBy(float,float,float)"""
        return ScaleByAction._wrap(_Actions.scaleBy(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def parallel(*arg0: 'scene2d.Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action...)"""
        return ParallelAction._wrap(_Actions.parallel(arg0))

    @staticmethod
    @overload
    def removeListener(arg0: 'EventListener', arg1: bool) -> 'RemoveListenerAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener,boolean)"""
        return RemoveListenerAction._wrap(_Actions.removeListener(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def moveBy(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'MoveByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveBy(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return MoveByAction._wrap(_Actions.moveBy(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def sizeBy(arg0: float, arg1: float) -> 'SizeByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeBy(float,float)"""
        return SizeByAction._wrap(_Actions.sizeBy(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def sizeTo(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'SizeToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeTo(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return SizeToAction._wrap(_Actions.sizeTo(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def moveToAligned(arg0: float, arg1: float, arg2: int, arg3: float) -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveToAligned(float,float,int,float)"""
        return MoveToAction._wrap(_Actions.moveToAligned(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def parallel() -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel()"""
        return ParallelAction._wrap(_Actions.parallel())

    @staticmethod
    @overload
    def show() -> 'VisibleAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.VisibleAction com.badlogic.gdx.scenes.scene2d.actions.Actions.show()"""
        return VisibleAction._wrap(_Actions.show())

    @staticmethod
    @overload
    def sequence(arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction._wrap(_Actions.sequence(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def moveTo(arg0: float, arg1: float) -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveTo(float,float)"""
        return MoveToAction._wrap(_Actions.moveTo(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def scaleTo(arg0: float, arg1: float, arg2: float) -> 'ScaleToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleTo(float,float,float)"""
        return ScaleToAction._wrap(_Actions.scaleTo(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def visible(arg0: bool) -> 'VisibleAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.VisibleAction com.badlogic.gdx.scenes.scene2d.actions.Actions.visible(boolean)"""
        return VisibleAction._wrap(_Actions.visible(_boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def action(arg0: 'Class') -> 'scene2d.Action':
        """public static <T extends com.badlogic.gdx.scenes.scene2d.Action> T com.badlogic.gdx.scenes.scene2d.actions.Actions.action(java.lang.Class<T>)"""
        return scene2d.Action._wrap(_Actions.action(arg0))

    @staticmethod
    @overload
    def removeListener(arg0: 'EventListener', arg1: bool, arg2: 'Actor') -> 'RemoveListenerAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener,boolean,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return RemoveListenerAction._wrap(_Actions.removeListener(arg0, _boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def rotateBy(arg0: float, arg1: float, arg2: 'Interpolation') -> 'RotateByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateBy(float,float,com.badlogic.gdx.math.Interpolation)"""
        return RotateByAction._wrap(_Actions.rotateBy(_float.valueOf(arg0), _float.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def forever(arg0: 'Action') -> 'RepeatAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RepeatAction com.badlogic.gdx.scenes.scene2d.actions.Actions.forever(com.badlogic.gdx.scenes.scene2d.Action)"""
        return RepeatAction._wrap(_Actions.forever(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def moveTo(arg0: float, arg1: float, arg2: float) -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveTo(float,float,float)"""
        return MoveToAction._wrap(_Actions.moveTo(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def delay(arg0: float, arg1: 'Action') -> 'DelayAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.DelayAction com.badlogic.gdx.scenes.scene2d.actions.Actions.delay(float,com.badlogic.gdx.scenes.scene2d.Action)"""
        return DelayAction._wrap(_Actions.delay(_float.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def addAction(arg0: 'Action') -> 'AddAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AddAction com.badlogic.gdx.scenes.scene2d.actions.Actions.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        return AddAction._wrap(_Actions.addAction(arg0))

    @staticmethod
    @overload
    def touchable(arg0: 'Touchable') -> 'TouchableAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.TouchableAction com.badlogic.gdx.scenes.scene2d.actions.Actions.touchable(com.badlogic.gdx.scenes.scene2d.Touchable)"""
        return TouchableAction._wrap(_Actions.touchable(arg0))

    @staticmethod
    @overload
    def removeActor(arg0: 'Actor') -> 'RemoveActorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return RemoveActorAction._wrap(_Actions.removeActor(arg0))

    @staticmethod
    @overload
    def parallel(arg0: 'Action', arg1: 'Action', arg2: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction._wrap(_Actions.parallel(arg0, arg1, arg2))

    @staticmethod
    @overload
    def removeAction(arg0: 'Action') -> 'RemoveAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        return RemoveAction._wrap(_Actions.removeAction(arg0))

    @staticmethod
    @overload
    def moveBy(arg0: float, arg1: float, arg2: float) -> 'MoveByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveBy(float,float,float)"""
        return MoveByAction._wrap(_Actions.moveBy(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def sequence() -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence()"""
        return SequenceAction._wrap(_Actions.sequence())

    @staticmethod
    @overload
    def fadeIn(arg0: float) -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.fadeIn(float)"""
        return AlphaAction._wrap(_Actions.fadeIn(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def sequence(arg0: 'Action', arg1: 'Action', arg2: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction._wrap(_Actions.sequence(arg0, arg1, arg2))

    @staticmethod
    @overload
    def fadeIn(arg0: float, arg1: 'Interpolation') -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.fadeIn(float,com.badlogic.gdx.math.Interpolation)"""
        return AlphaAction._wrap(_Actions.fadeIn(_float.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def scaleBy(arg0: float, arg1: float) -> 'ScaleByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleBy(float,float)"""
        return ScaleByAction._wrap(_Actions.scaleBy(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def color(arg0: 'Color', arg1: float, arg2: 'Interpolation') -> 'ColorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ColorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.color(com.badlogic.gdx.graphics.Color,float,com.badlogic.gdx.math.Interpolation)"""
        return ColorAction._wrap(_Actions.color(arg0, _float.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def rotateBy(arg0: float, arg1: float) -> 'RotateByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateBy(float,float)"""
        return RotateByAction._wrap(_Actions.rotateBy(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def alpha(arg0: float) -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.alpha(float)"""
        return AlphaAction._wrap(_Actions.alpha(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def parallel(arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action', arg4: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction._wrap(_Actions.parallel(arg0, arg1, arg2, arg3, arg4)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.TouchableAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.Touchable as _Touchable
_Touchable = _Touchable
import com.badlogic.gdx.scenes.scene2d.actions.TouchableAction as _TouchableAction
_TouchableAction = _TouchableAction
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TouchableAction():
    """com.badlogic.gdx.scenes.scene2d.actions.TouchableAction"""
 
    @staticmethod
    def _wrap(java_value: _TouchableAction) -> 'TouchableAction':
        return TouchableAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TouchableAction):
        """
        Dynamic initializer for TouchableAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TouchableAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TouchableAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @overload
    def getTouchable(self) -> 'scene2d.Touchable':
        """public com.badlogic.gdx.scenes.scene2d.Touchable com.badlogic.gdx.scenes.scene2d.actions.TouchableAction.getTouchable()"""
        return 'scene2d.Touchable'._wrap(super(TouchableAction, self).getTouchable())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.TouchableAction()"""
        val = _TouchableAction()
        self.__wrapper = val

    @overload
    def setTouchable(self, arg0: 'Touchable'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TouchableAction.setTouchable(com.badlogic.gdx.scenes.scene2d.Touchable)"""
        super(_TouchableAction, self).setTouchable(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.TouchableAction()"""
        val = _TouchableAction()
        self.__wrapper = val

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TouchableAction.act(float)"""
        return bool._wrap(super(_TouchableAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.SizeByAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import com.badlogic.gdx.scenes.scene2d.actions.SizeByAction as _SizeByAction
_SizeByAction = _SizeByAction
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
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
 
class SizeByAction():
    """com.badlogic.gdx.scenes.scene2d.actions.SizeByAction"""
 
    @staticmethod
    def _wrap(java_value: _SizeByAction) -> 'SizeByAction':
        return SizeByAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SizeByAction):
        """
        Dynamic initializer for SizeByAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SizeByAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SizeByAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.SizeByAction()"""
        val = _SizeByAction()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.SizeByAction()"""
        val = _SizeByAction()
        self.__wrapper = val

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @overload
    def getAmountHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.getAmountHeight()"""
        return float._wrap(super(SizeByAction, self).getAmountHeight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getAmountWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.getAmountWidth()"""
        return float._wrap(super(SizeByAction, self).getAmountWidth())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setAmountHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.setAmountHeight(float)"""
        super(_SizeByAction, self).setAmountHeight(_float.valueOf(arg0))

    @overload
    def setAmountWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.setAmountWidth(float)"""
        super(_SizeByAction, self).setAmountWidth(_float.valueOf(arg0))

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setAmount(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.setAmount(float,float)"""
        super(_SizeByAction, self).setAmount(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.LayoutAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import com.badlogic.gdx.scenes.scene2d.actions.LayoutAction as _LayoutAction
_LayoutAction = _LayoutAction
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LayoutAction():
    """com.badlogic.gdx.scenes.scene2d.actions.LayoutAction"""
 
    @staticmethod
    def _wrap(java_value: _LayoutAction) -> 'LayoutAction':
        return LayoutAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LayoutAction):
        """
        Dynamic initializer for LayoutAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LayoutAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LayoutAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.isEnabled()"""
        return bool._wrap(super(LayoutAction, self).isEnabled())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.act(float)"""
        return bool._wrap(super(_LayoutAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def setLayoutEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.setLayoutEnabled(boolean)"""
        super(_LayoutAction, self).setLayoutEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.LayoutAction()"""
        val = _LayoutAction()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_LayoutAction, self).setTarget(arg0)

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.LayoutAction()"""
        val = _LayoutAction()
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.AlphaAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.AlphaAction as _AlphaAction
_AlphaAction = _AlphaAction
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AlphaAction():
    """com.badlogic.gdx.scenes.scene2d.actions.AlphaAction"""
 
    @staticmethod
    def _wrap(java_value: _AlphaAction) -> 'AlphaAction':
        return AlphaAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AlphaAction):
        """
        Dynamic initializer for AlphaAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AlphaAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AlphaAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.AlphaAction()"""
        val = _AlphaAction()
        self.__wrapper = val

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.getColor()"""
        return 'graphics.Color'._wrap(super(AlphaAction, self).getColor())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setAlpha(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.setAlpha(float)"""
        super(_AlphaAction, self).setAlpha(_float.valueOf(arg0))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.AlphaAction()"""
        val = _AlphaAction()
        self.__wrapper = val

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_AlphaAction, self).setColor(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.reset()"""
        super(AlphaAction, self).reset()

    @overload
    def getAlpha(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.getAlpha()"""
        return float._wrap(super(AlphaAction, self).getAlpha())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.ColorAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.actions.ColorAction as _ColorAction
_ColorAction = _ColorAction
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ColorAction():
    """com.badlogic.gdx.scenes.scene2d.actions.ColorAction"""
 
    @staticmethod
    def _wrap(java_value: _ColorAction) -> 'ColorAction':
        return ColorAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorAction):
        """
        Dynamic initializer for ColorAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.ColorAction()"""
        val = _ColorAction()
        self.__wrapper = val

    @overload
    def setEndColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ColorAction.setEndColor(com.badlogic.gdx.graphics.Color)"""
        super(_ColorAction, self).setEndColor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.ColorAction()"""
        val = _ColorAction()
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.actions.ColorAction.getColor()"""
        return 'graphics.Color'._wrap(super(ColorAction, self).getColor())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ColorAction.reset()"""
        super(ColorAction, self).reset()

    @overload
    def getEndColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.actions.ColorAction.getEndColor()"""
        return 'graphics.Color'._wrap(super(ColorAction, self).getEndColor())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ColorAction.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_ColorAction, self).setColor(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.DelayAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
from builtins import float
import com.badlogic.gdx.scenes.scene2d.actions.DelayAction as _DelayAction
_DelayAction = _DelayAction
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as _DelegateAction
_DelegateAction = _DelegateAction
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DelayAction():
    """com.badlogic.gdx.scenes.scene2d.actions.DelayAction"""
 
    @staticmethod
    def _wrap(java_value: _DelayAction) -> 'DelayAction':
        return DelayAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DelayAction):
        """
        Dynamic initializer for DelayAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DelayAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DelayAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelayAction.setDuration(float)"""
        super(_DelayAction, self).setDuration(_float.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.DelayAction()"""
        val = _DelayAction()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.DelayAction(float)"""
        val = _DelayAction(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_DelegateAction, self).setActor(arg0)

    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.DelayAction.getDuration()"""
        return float._wrap(super(DelayAction, self).getDuration())

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

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
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool._wrap(super(_DelegateAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.DelayAction()"""
        val = _DelayAction()
        self.__wrapper = val

    @override
    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_DelegateAction, self).setAction(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str._wrap(super(DelegateAction, self).toString())

    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelayAction.setTime(float)"""
        super(_DelayAction, self).setTime(_float.valueOf(arg0))

    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.DelayAction.getTime()"""
        return float._wrap(super(DelayAction, self).getTime())

    @override
    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'._wrap(super(DelegateAction, self).getAction())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelayAction.finish()"""
        super(DelayAction, self).finish()

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_DelegateAction, self).setTarget(arg0)

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

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
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelayAction.restart()"""
        super(DelayAction, self).restart()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.AddAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import com.badlogic.gdx.scenes.scene2d.actions.AddAction as _AddAction
_AddAction = _AddAction
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AddAction():
    """com.badlogic.gdx.scenes.scene2d.actions.AddAction"""
 
    @staticmethod
    def _wrap(java_value: _AddAction) -> 'AddAction':
        return AddAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AddAction):
        """
        Dynamic initializer for AddAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AddAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AddAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.AddAction()"""
        val = _AddAction()
        self.__wrapper = val

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.AddAction.act(float)"""
        return bool._wrap(super(_AddAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

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
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.AddAction.getAction()"""
        return 'scene2d.Action'._wrap(super(AddAction, self).getAction())

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddAction.restart()"""
        super(AddAction, self).restart()

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_AddAction, self).setAction(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.AddAction()"""
        val = _AddAction()
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddAction.reset()"""
        super(AddAction, self).reset()

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.ParallelAction
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.scenes.scene2d.actions.ParallelAction as _ParallelAction
_ParallelAction = _ParallelAction
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParallelAction():
    """com.badlogic.gdx.scenes.scene2d.actions.ParallelAction"""
 
    @staticmethod
    def _wrap(java_value: _ParallelAction) -> 'ParallelAction':
        return ParallelAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParallelAction):
        """
        Dynamic initializer for ParallelAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParallelAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParallelAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_ParallelAction, self).setActor(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

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
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.reset()"""
        super(ParallelAction, self).reset()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.restart()"""
        super(ParallelAction, self).restart()

    @overload
    def getActions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Action> com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.getActions()"""
        return 'utils.Array'._wrap(super(ParallelAction, self).getActions())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction()"""
        val = _ParallelAction()
        self.__wrapper = val

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.act(float)"""
        return bool._wrap(super(_ParallelAction, self).act(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _ParallelAction(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def __init__(self, arg0: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _ParallelAction(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction()"""
        val = _ParallelAction()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.toString()"""
        return str._wrap(super(ParallelAction, self).toString())

    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_ParallelAction, self).addAction(arg0)

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _ParallelAction(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action', arg4: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _ParallelAction(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _ParallelAction(arg0, arg1, arg2)
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RepeatAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as _DelegateAction
_DelegateAction = _DelegateAction
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.RepeatAction as _RepeatAction
_RepeatAction = _RepeatAction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RepeatAction():
    """com.badlogic.gdx.scenes.scene2d.actions.RepeatAction"""
 
    @staticmethod
    def _wrap(java_value: _RepeatAction) -> 'RepeatAction':
        return RepeatAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RepeatAction):
        """
        Dynamic initializer for RepeatAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RepeatAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RepeatAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCount(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RepeatAction.setCount(int)"""
        super(_RepeatAction, self).setCount(_int.valueOf(arg0))

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_DelegateAction, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RepeatAction.restart()"""
        super(RepeatAction, self).restart()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool._wrap(super(_DelegateAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_DelegateAction, self).setAction(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str._wrap(super(DelegateAction, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RepeatAction()"""
        val = _RepeatAction()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RepeatAction()"""
        val = _RepeatAction()
        self.__wrapper = val

    @override
    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'._wrap(super(DelegateAction, self).getAction())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_DelegateAction, self).setTarget(arg0)

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def getCount(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.RepeatAction.getCount()"""
        return int._wrap(super(RepeatAction, self).getCount())

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
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RepeatAction.finish()"""
        super(RepeatAction, self).finish()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.TemporalAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
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
 
class TemporalAction():
    """com.badlogic.gdx.scenes.scene2d.actions.TemporalAction"""
 
    @staticmethod
    def _wrap(java_value: _TemporalAction) -> 'TemporalAction':
        return TemporalAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TemporalAction):
        """
        Dynamic initializer for TemporalAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TemporalAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TemporalAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.TemporalAction(float)"""
        val = _TemporalAction(_float.valueOf(arg0))
        self.__wrapper = val

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.TemporalAction()"""
        val = _TemporalAction()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.TemporalAction()"""
        val = _TemporalAction()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float, arg1: 'Interpolation'):
        """public com.badlogic.gdx.scenes.scene2d.actions.TemporalAction(float,com.badlogic.gdx.math.Interpolation)"""
        val = _TemporalAction(_float.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction as _RemoveListenerAction
_RemoveListenerAction = _RemoveListenerAction
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.EventListener as _EventListener
_EventListener = _EventListener
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemoveListenerAction():
    """com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction"""
 
    @staticmethod
    def _wrap(java_value: _RemoveListenerAction) -> 'RemoveListenerAction':
        return RemoveListenerAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemoveListenerAction):
        """
        Dynamic initializer for RemoveListenerAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemoveListenerAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemoveListenerAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def setListener(self, arg0: 'EventListener'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.setListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        super(_RemoveListenerAction, self).setListener(arg0)

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction()"""
        val = _RemoveListenerAction()
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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getListener(self) -> 'scene2d.EventListener':
        """public com.badlogic.gdx.scenes.scene2d.EventListener com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.getListener()"""
        return 'scene2d.EventListener'._wrap(super(RemoveListenerAction, self).getListener())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.act(float)"""
        return bool._wrap(super(_RemoveListenerAction, self).act(_float.valueOf(arg0)))

    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.setCapture(boolean)"""
        super(_RemoveListenerAction, self).setCapture(_boolean.valueOf(arg0))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.reset()"""
        super(RemoveListenerAction, self).reset()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction()"""
        val = _RemoveListenerAction()
        self.__wrapper = val

    @overload
    def getCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.getCapture()"""
        return bool._wrap(super(RemoveListenerAction, self).getCapture())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
from builtins import float
import com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction as _TimeScaleAction
_TimeScaleAction = _TimeScaleAction
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as _DelegateAction
_DelegateAction = _DelegateAction
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TimeScaleAction():
    """com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction"""
 
    @staticmethod
    def _wrap(java_value: _TimeScaleAction) -> 'TimeScaleAction':
        return TimeScaleAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TimeScaleAction):
        """
        Dynamic initializer for TimeScaleAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TimeScaleAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TimeScaleAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str._wrap(super(DelegateAction, self).toString())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @override
    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'._wrap(super(DelegateAction, self).getAction())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction()"""
        val = _TimeScaleAction()
        self.__wrapper = val

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_DelegateAction, self).setTarget(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.restart()"""
        super(DelegateAction, self).restart()

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction.setScale(float)"""
        super(_TimeScaleAction, self).setScale(_float.valueOf(arg0))

    @overload
    def getScale(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction.getScale()"""
        return float._wrap(super(TimeScaleAction, self).getScale())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_DelegateAction, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

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
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool._wrap(super(_DelegateAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_DelegateAction, self).setAction(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction()"""
        val = _TimeScaleAction()
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.VisibleAction
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.VisibleAction as _VisibleAction
_VisibleAction = _VisibleAction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VisibleAction():
    """com.badlogic.gdx.scenes.scene2d.actions.VisibleAction"""
 
    @staticmethod
    def _wrap(java_value: _VisibleAction) -> 'VisibleAction':
        return VisibleAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VisibleAction):
        """
        Dynamic initializer for VisibleAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VisibleAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VisibleAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.VisibleAction.act(float)"""
        return bool._wrap(super(_VisibleAction, self).act(_float.valueOf(arg0)))

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.VisibleAction.isVisible()"""
        return bool._wrap(super(VisibleAction, self).isVisible())

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.VisibleAction()"""
        val = _VisibleAction()
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.VisibleAction.setVisible(boolean)"""
        super(_VisibleAction, self).setVisible(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.VisibleAction()"""
        val = _VisibleAction()
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction as _AddListenerAction
_AddListenerAction = _AddListenerAction
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.EventListener as _EventListener
_EventListener = _EventListener
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AddListenerAction():
    """com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction"""
 
    @staticmethod
    def _wrap(java_value: _AddListenerAction) -> 'AddListenerAction':
        return AddListenerAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AddListenerAction):
        """
        Dynamic initializer for AddListenerAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AddListenerAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AddListenerAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.act(float)"""
        return bool._wrap(super(_AddListenerAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def setListener(self, arg0: 'EventListener'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.setListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        super(_AddListenerAction, self).setListener(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction()"""
        val = _AddListenerAction()
        self.__wrapper = val

    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.setCapture(boolean)"""
        super(_AddListenerAction, self).setCapture(_boolean.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getListener(self) -> 'scene2d.EventListener':
        """public com.badlogic.gdx.scenes.scene2d.EventListener com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.getListener()"""
        return 'scene2d.EventListener'._wrap(super(AddListenerAction, self).getListener())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction()"""
        val = _AddListenerAction()
        self.__wrapper = val

    @overload
    def getCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.getCapture()"""
        return bool._wrap(super(AddListenerAction, self).getCapture())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.reset()"""
        super(AddListenerAction, self).reset()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction as _ScaleToAction
_ScaleToAction = _ScaleToAction
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
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
 
class ScaleToAction():
    """com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction"""
 
    @staticmethod
    def _wrap(java_value: _ScaleToAction) -> 'ScaleToAction':
        return ScaleToAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScaleToAction):
        """
        Dynamic initializer for ScaleToAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScaleToAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScaleToAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction()"""
        val = _ScaleToAction()
        self.__wrapper = val

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.setX(float)"""
        super(_ScaleToAction, self).setX(_float.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.setScale(float,float)"""
        super(_ScaleToAction, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.setScale(float)"""
        super(_ScaleToAction, self).setScale(_float.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction()"""
        val = _ScaleToAction()
        self.__wrapper = val

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.setY(float)"""
        super(_ScaleToAction, self).setY(_float.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.getX()"""
        return float._wrap(super(ScaleToAction, self).getX())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.getY()"""
        return float._wrap(super(ScaleToAction, self).getY())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.MoveByAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.scenes.scene2d.actions.MoveByAction as _MoveByAction
_MoveByAction = _MoveByAction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MoveByAction():
    """com.badlogic.gdx.scenes.scene2d.actions.MoveByAction"""
 
    @staticmethod
    def _wrap(java_value: _MoveByAction) -> 'MoveByAction':
        return MoveByAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MoveByAction):
        """
        Dynamic initializer for MoveByAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MoveByAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MoveByAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @overload
    def getAmountY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.getAmountY()"""
        return float._wrap(super(MoveByAction, self).getAmountY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @overload
    def setAmountY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.setAmountY(float)"""
        super(_MoveByAction, self).setAmountY(_float.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.MoveByAction()"""
        val = _MoveByAction()
        self.__wrapper = val

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getAmountX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.getAmountX()"""
        return float._wrap(super(MoveByAction, self).getAmountX())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def setAmountX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.setAmountX(float)"""
        super(_MoveByAction, self).setAmountX(_float.valueOf(arg0))

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.MoveByAction()"""
        val = _MoveByAction()
        self.__wrapper = val

    @overload
    def setAmount(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.setAmount(float,float)"""
        super(_MoveByAction, self).setAmount(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction as _CountdownEventAction
_CountdownEventAction = _CountdownEventAction
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.EventAction as _EventAction
_EventAction = _EventAction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CountdownEventAction():
    """com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction"""
 
    @staticmethod
    def _wrap(java_value: _CountdownEventAction) -> 'CountdownEventAction':
        return CountdownEventAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CountdownEventAction):
        """
        Dynamic initializer for CountdownEventAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CountdownEventAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CountdownEventAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.act(float)"""
        return bool._wrap(super(_EventAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.restart()"""
        super(EventAction, self).restart()

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setActive(boolean)"""
        super(_EventAction, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_EventAction, self).setTarget(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

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
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction.handle(T)"""
        return bool._wrap(super(_CountdownEventAction, self).handle(arg0))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.isActive()"""
        return bool._wrap(super(EventAction, self).isActive())

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
    def __init__(self, arg0: 'Class', arg1: int):
        """public com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction(java.lang.Class<? extends T>,int)"""
        val = _CountdownEventAction(arg0, _int.valueOf(arg1))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction as _RemoveActorAction
_RemoveActorAction = _RemoveActorAction
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemoveActorAction():
    """com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction"""
 
    @staticmethod
    def _wrap(java_value: _RemoveActorAction) -> 'RemoveActorAction':
        return RemoveActorAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemoveActorAction):
        """
        Dynamic initializer for RemoveActorAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemoveActorAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemoveActorAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction.restart()"""
        super(RemoveActorAction, self).restart()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction.act(float)"""
        return bool._wrap(super(_RemoveActorAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

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
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction()"""
        val = _RemoveActorAction()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction()"""
        val = _RemoveActorAction()
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.IntAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.scenes.scene2d.actions.IntAction as _IntAction
_IntAction = _IntAction
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
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
 
class IntAction():
    """com.badlogic.gdx.scenes.scene2d.actions.IntAction"""
 
    @staticmethod
    def _wrap(java_value: _IntAction) -> 'IntAction':
        return IntAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntAction):
        """
        Dynamic initializer for IntAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def getEnd(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.IntAction.getEnd()"""
        return int._wrap(super(IntAction, self).getEnd())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @overload
    def setStart(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.IntAction.setStart(int)"""
        super(_IntAction, self).setStart(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @overload
    def getValue(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.IntAction.getValue()"""
        return int._wrap(super(IntAction, self).getValue())

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setEnd(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.IntAction.setEnd(int)"""
        super(_IntAction, self).setEnd(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction(int,int,float)"""
        val = _IntAction(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction(int,int)"""
        val = _IntAction(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction()"""
        val = _IntAction()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction()"""
        val = _IntAction()
        self.__wrapper = val

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float, arg3: 'Interpolation'):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction(int,int,float,com.badlogic.gdx.math.Interpolation)"""
        val = _IntAction(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), arg3)
        self.__wrapper = val

    @overload
    def setValue(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.IntAction.setValue(int)"""
        super(_IntAction, self).setValue(_int.valueOf(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def getStart(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.IntAction.getStart()"""
        return int._wrap(super(IntAction, self).getStart())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.DelegateAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as _DelegateAction
_DelegateAction = _DelegateAction
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DelegateAction():
    """com.badlogic.gdx.scenes.scene2d.actions.DelegateAction"""
 
    @staticmethod
    def _wrap(java_value: _DelegateAction) -> 'DelegateAction':
        return DelegateAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DelegateAction):
        """
        Dynamic initializer for DelegateAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DelegateAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DelegateAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str._wrap(super(DelegateAction, self).toString())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_DelegateAction, self).setAction(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_DelegateAction, self).setTarget(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.restart()"""
        super(DelegateAction, self).restart()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_DelegateAction, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.DelegateAction()"""
        val = _DelegateAction()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool._wrap(super(_DelegateAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.DelegateAction()"""
        val = _DelegateAction()
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'._wrap(super(DelegateAction, self).getAction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction as _RelativeTemporalAction
_RelativeTemporalAction = _RelativeTemporalAction
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
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
 
class RelativeTemporalAction():
    """com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction"""
 
    @staticmethod
    def _wrap(java_value: _RelativeTemporalAction) -> 'RelativeTemporalAction':
        return RelativeTemporalAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RelativeTemporalAction):
        """
        Dynamic initializer for RelativeTemporalAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RelativeTemporalAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RelativeTemporalAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction()"""
        val = _RelativeTemporalAction()
        self.__wrapper = val

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

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
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction()"""
        val = _RelativeTemporalAction()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RunnableAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import java.lang.Runnable as Runnable
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Integer as _int
import java.lang.Runnable as _Runnable
_Runnable = _Runnable
import com.badlogic.gdx.scenes.scene2d.actions.RunnableAction as _RunnableAction
_RunnableAction = _RunnableAction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RunnableAction():
    """com.badlogic.gdx.scenes.scene2d.actions.RunnableAction"""
 
    @staticmethod
    def _wrap(java_value: _RunnableAction) -> 'RunnableAction':
        return RunnableAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RunnableAction):
        """
        Dynamic initializer for RunnableAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RunnableAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RunnableAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RunnableAction()"""
        val = _RunnableAction()
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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.reset()"""
        super(RunnableAction, self).reset()

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getRunnable(self) -> 'Runnable':
        """public java.lang.Runnable com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.getRunnable()"""
        return 'Runnable'._wrap(super(RunnableAction, self).getRunnable())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RunnableAction()"""
        val = _RunnableAction()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def setRunnable(self, arg0: 'Runnable'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.setRunnable(java.lang.Runnable)"""
        super(_RunnableAction, self).setRunnable(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.act(float)"""
        return bool._wrap(super(_RunnableAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.restart()"""
        super(RunnableAction, self).restart()

    @overload
    def run(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.run()"""
        super(RunnableAction, self).run()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.SequenceAction
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.scenes.scene2d.actions.ParallelAction as _ParallelAction
_ParallelAction = _ParallelAction
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.SequenceAction as _SequenceAction
_SequenceAction = _SequenceAction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SequenceAction():
    """com.badlogic.gdx.scenes.scene2d.actions.SequenceAction"""
 
    @staticmethod
    def _wrap(java_value: _SequenceAction) -> 'SequenceAction':
        return SequenceAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SequenceAction):
        """
        Dynamic initializer for SequenceAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SequenceAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SequenceAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _SequenceAction(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_ParallelAction, self).setActor(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _SequenceAction(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_ParallelAction, self).addAction(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

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
    def __init__(self, arg0: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _SequenceAction(arg0)
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.reset()"""
        super(ParallelAction, self).reset()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _SequenceAction(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction()"""
        val = _SequenceAction()
        self.__wrapper = val

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SequenceAction.restart()"""
        super(SequenceAction, self).restart()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action', arg4: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = _SequenceAction(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction()"""
        val = _SequenceAction()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.toString()"""
        return str._wrap(super(ParallelAction, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.SequenceAction.act(float)"""
        return bool._wrap(super(_SequenceAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getActions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Action> com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.getActions()"""
        return 'utils.Array'._wrap(super(ParallelAction, self).getActions())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RotateByAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.RotateByAction as _RotateByAction
_RotateByAction = _RotateByAction
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RotateByAction():
    """com.badlogic.gdx.scenes.scene2d.actions.RotateByAction"""
 
    @staticmethod
    def _wrap(java_value: _RotateByAction) -> 'RotateByAction':
        return RotateByAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RotateByAction):
        """
        Dynamic initializer for RotateByAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RotateByAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RotateByAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @overload
    def setAmount(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RotateByAction.setAmount(float)"""
        super(_RotateByAction, self).setAmount(_float.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateByAction()"""
        val = _RotateByAction()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def getAmount(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.RotateByAction.getAmount()"""
        return float._wrap(super(RotateByAction, self).getAmount())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateByAction()"""
        val = _RotateByAction()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.FloatAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

import com.badlogic.gdx.scenes.scene2d.actions.FloatAction as _FloatAction
_FloatAction = _FloatAction
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
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
 
class FloatAction():
    """com.badlogic.gdx.scenes.scene2d.actions.FloatAction"""
 
    @staticmethod
    def _wrap(java_value: _FloatAction) -> 'FloatAction':
        return FloatAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatAction):
        """
        Dynamic initializer for FloatAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction()"""
        val = _FloatAction()
        self.__wrapper = val

    @overload
    def getValue(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.FloatAction.getValue()"""
        return float._wrap(super(FloatAction, self).getValue())

    @overload
    def getEnd(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.FloatAction.getEnd()"""
        return float._wrap(super(FloatAction, self).getEnd())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setValue(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.FloatAction.setValue(float)"""
        super(_FloatAction, self).setValue(_float.valueOf(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getStart(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.FloatAction.getStart()"""
        return float._wrap(super(FloatAction, self).getStart())

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: 'Interpolation'):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        val = _FloatAction(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction()"""
        val = _FloatAction()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction(float,float,float)"""
        val = _FloatAction(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction(float,float)"""
        val = _FloatAction(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setEnd(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.FloatAction.setEnd(float)"""
        super(_FloatAction, self).setEnd(_float.valueOf(arg0))

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setStart(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.FloatAction.setStart(float)"""
        super(_FloatAction, self).setStart(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.MoveToAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.MoveToAction as _MoveToAction
_MoveToAction = _MoveToAction
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MoveToAction():
    """com.badlogic.gdx.scenes.scene2d.actions.MoveToAction"""
 
    @staticmethod
    def _wrap(java_value: _MoveToAction) -> 'MoveToAction':
        return MoveToAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MoveToAction):
        """
        Dynamic initializer for MoveToAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MoveToAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MoveToAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setX(float)"""
        super(_MoveToAction, self).setX(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @overload
    def getStartY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getStartY()"""
        return float._wrap(super(MoveToAction, self).getStartY())

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setY(float)"""
        super(_MoveToAction, self).setY(_float.valueOf(arg0))

    @overload
    def getAlignment(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getAlignment()"""
        return int._wrap(super(MoveToAction, self).getAlignment())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.MoveToAction()"""
        val = _MoveToAction()
        self.__wrapper = val

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setPosition(float,float,int)"""
        super(_MoveToAction, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getX()"""
        return float._wrap(super(MoveToAction, self).getX())

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getY()"""
        return float._wrap(super(MoveToAction, self).getY())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @overload
    def getStartX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getStartX()"""
        return float._wrap(super(MoveToAction, self).getStartX())

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.reset()"""
        super(MoveToAction, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setPosition(float,float)"""
        super(_MoveToAction, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setAlignment(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setAlignment(int)"""
        super(_MoveToAction, self).setAlignment(_int.valueOf(arg0))

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @overload
    def setStartPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setStartPosition(float,float)"""
        super(_MoveToAction, self).setStartPosition(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.MoveToAction()"""
        val = _MoveToAction()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RotateToAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
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
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.RotateToAction as _RotateToAction
_RotateToAction = _RotateToAction
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RotateToAction():
    """com.badlogic.gdx.scenes.scene2d.actions.RotateToAction"""
 
    @staticmethod
    def _wrap(java_value: _RotateToAction) -> 'RotateToAction':
        return RotateToAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RotateToAction):
        """
        Dynamic initializer for RotateToAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RotateToAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RotateToAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RotateToAction.setRotation(float)"""
        super(_RotateToAction, self).setRotation(_float.valueOf(arg0))

    @overload
    def setUseShortestDirection(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RotateToAction.setUseShortestDirection(boolean)"""
        super(_RotateToAction, self).setUseShortestDirection(_boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @overload
    def isUseShortestDirection(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RotateToAction.isUseShortestDirection()"""
        return bool._wrap(super(RotateToAction, self).isUseShortestDirection())

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateToAction()"""
        val = _RotateToAction()
        self.__wrapper = val

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.RotateToAction.getRotation()"""
        return float._wrap(super(RotateToAction, self).getRotation())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateToAction()"""
        val = _RotateToAction()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateToAction(boolean)"""
        val = _RotateToAction(_boolean.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RemoveAction
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

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
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.scenes.scene2d.actions.RemoveAction as _RemoveAction
_RemoveAction = _RemoveAction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RemoveAction():
    """com.badlogic.gdx.scenes.scene2d.actions.RemoveAction"""
 
    @staticmethod
    def _wrap(java_value: _RemoveAction) -> 'RemoveAction':
        return RemoveAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RemoveAction):
        """
        Dynamic initializer for RemoveAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RemoveAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RemoveAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RemoveAction.act(float)"""
        return bool._wrap(super(_RemoveAction, self).act(_float.valueOf(arg0)))

    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(_RemoveAction, self).setAction(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.RemoveAction.getAction()"""
        return 'scene2d.Action'._wrap(super(RemoveAction, self).getAction())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveAction()"""
        val = _RemoveAction()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveAction()"""
        val = _RemoveAction()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveAction.reset()"""
        super(RemoveAction, self).reset()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.SizeToAction
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.scenes.scene2d.Action as _Action
_Action = _Action
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = _import_once("pygdx.scenes.scene2d")

import com.badlogic.gdx.scenes.scene2d.actions.SizeToAction as _SizeToAction
_SizeToAction = _SizeToAction
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as _TemporalAction
_TemporalAction = _TemporalAction
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.scenes.scene2d.Actor as _Actor
_Actor = _Actor
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Boolean as _boolean
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
 
class SizeToAction():
    """com.badlogic.gdx.scenes.scene2d.actions.SizeToAction"""
 
    @staticmethod
    def _wrap(java_value: _SizeToAction) -> 'SizeToAction':
        return SizeToAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SizeToAction):
        """
        Dynamic initializer for SizeToAction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SizeToAction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SizeToAction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float._wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'._wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool._wrap(super(TemporalAction, self).isReverse())

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.getWidth()"""
        return float._wrap(super(SizeToAction, self).getWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(_TemporalAction, self).setReverse(_boolean.valueOf(arg0))

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(_scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool._wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.setWidth(float)"""
        super(_SizeToAction, self).setWidth(_float.valueOf(arg0))

    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.setSize(float,float)"""
        super(_SizeToAction, self).setSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.SizeToAction()"""
        val = _SizeToAction()
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(_scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(_TemporalAction, self).setDuration(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'._wrap(super(scene2d.Action, self).getActor())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.SizeToAction()"""
        val = _SizeToAction()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str._wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool._wrap(super(_TemporalAction, self).act(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(_TemporalAction, self).setTime(_float.valueOf(arg0))

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float._wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.getHeight()"""
        return float._wrap(super(SizeToAction, self).getHeight())

    @overload
    def setHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.setHeight(float)"""
        super(_SizeToAction, self).setHeight(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())
from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.actions.LayoutAction as __LayoutAction
__LayoutAction = __LayoutAction
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LayoutAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.LayoutAction"""
 
    @staticmethod
    def __wrap(java_value: __LayoutAction) -> 'LayoutAction':
        return LayoutAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LayoutAction):
        """
        Dynamic initializer for LayoutAction.
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
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def setLayoutEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.setLayoutEnabled(boolean)"""
        super(__LayoutAction, self).setLayoutEnabled(__boolean.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.isEnabled()"""
        return bool.__wrap(super(LayoutAction, self).isEnabled())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__LayoutAction, self).setTarget(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.act(float)"""
        return bool.__wrap(super(__LayoutAction, self).act(__float.valueOf(arg0)))

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
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.LayoutAction()"""
        val = __LayoutAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.LayoutAction()"""
        val = __LayoutAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.LayoutAction
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.actions.LayoutAction as __LayoutAction
__LayoutAction = __LayoutAction
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LayoutAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.LayoutAction"""
 
    @staticmethod
    def __wrap(java_value: __LayoutAction) -> 'LayoutAction':
        return LayoutAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LayoutAction):
        """
        Dynamic initializer for LayoutAction.
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
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def setLayoutEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.setLayoutEnabled(boolean)"""
        super(__LayoutAction, self).setLayoutEnabled(__boolean.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.isEnabled()"""
        return bool.__wrap(super(LayoutAction, self).isEnabled())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__LayoutAction, self).setTarget(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.LayoutAction.act(float)"""
        return bool.__wrap(super(__LayoutAction, self).act(__float.valueOf(arg0)))

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
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.LayoutAction()"""
        val = __LayoutAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.LayoutAction()"""
        val = __LayoutAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.LayoutAction 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RotateToAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.actions.RotateToAction as __RotateToAction
__RotateToAction = __RotateToAction
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RotateToAction(__TemporalAction, TemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.RotateToAction"""
 
    @staticmethod
    def __wrap(java_value: __RotateToAction) -> 'RotateToAction':
        return RotateToAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RotateToAction):
        """
        Dynamic initializer for RotateToAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateToAction(boolean)"""
        val = __RotateToAction(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RotateToAction.setRotation(float)"""
        super(__RotateToAction, self).setRotation(__float.valueOf(arg0))

    @overload
    def setUseShortestDirection(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RotateToAction.setUseShortestDirection(boolean)"""
        super(__RotateToAction, self).setUseShortestDirection(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateToAction()"""
        val = __RotateToAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @overload
    def isUseShortestDirection(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RotateToAction.isUseShortestDirection()"""
        return bool.__wrap(super(RotateToAction, self).isUseShortestDirection())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.RotateToAction.getRotation()"""
        return float.__wrap(super(RotateToAction, self).getRotation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateToAction()"""
        val = __RotateToAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.SizeToAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import com.badlogic.gdx.scenes.scene2d.actions.SizeToAction as __SizeToAction
__SizeToAction = __SizeToAction
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SizeToAction(__TemporalAction, TemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.SizeToAction"""
 
    @staticmethod
    def __wrap(java_value: __SizeToAction) -> 'SizeToAction':
        return SizeToAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SizeToAction):
        """
        Dynamic initializer for SizeToAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.SizeToAction()"""
        val = __SizeToAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.setWidth(float)"""
        super(__SizeToAction, self).setWidth(__float.valueOf(arg0))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.setSize(float,float)"""
        super(__SizeToAction, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.getHeight()"""
        return float.__wrap(super(SizeToAction, self).getHeight())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.SizeToAction()"""
        val = __SizeToAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @overload
    def setHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.setHeight(float)"""
        super(__SizeToAction, self).setHeight(__float.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.SizeToAction.getWidth()"""
        return float.__wrap(super(SizeToAction, self).getWidth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.MoveToAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.actions.MoveToAction as __MoveToAction
__MoveToAction = __MoveToAction
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class MoveToAction(__TemporalAction, TemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.MoveToAction"""
 
    @staticmethod
    def __wrap(java_value: __MoveToAction) -> 'MoveToAction':
        return MoveToAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MoveToAction):
        """
        Dynamic initializer for MoveToAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAlignment(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getAlignment()"""
        return int.__wrap(super(MoveToAction, self).getAlignment())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getX()"""
        return float.__wrap(super(MoveToAction, self).getX())

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setY(float)"""
        super(__MoveToAction, self).setY(__float.valueOf(arg0))

    @overload
    def getStartY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getStartY()"""
        return float.__wrap(super(MoveToAction, self).getStartY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getStartX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getStartX()"""
        return float.__wrap(super(MoveToAction, self).getStartX())

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setX(float)"""
        super(__MoveToAction, self).setX(__float.valueOf(arg0))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def setAlignment(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setAlignment(int)"""
        super(__MoveToAction, self).setAlignment(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.reset()"""
        super(MoveToAction, self).reset()

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.MoveToAction()"""
        val = __MoveToAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setPosition(float,float,int)"""
        super(__MoveToAction, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.MoveToAction()"""
        val = __MoveToAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setStartPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setStartPosition(float,float)"""
        super(__MoveToAction, self).setStartPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.setPosition(float,float)"""
        super(__MoveToAction, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveToAction.getY()"""
        return float.__wrap(super(MoveToAction, self).getY()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.ParallelAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import com.badlogic.gdx.scenes.scene2d.actions.ParallelAction as __ParallelAction
__ParallelAction = __ParallelAction
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParallelAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.ParallelAction"""
 
    @staticmethod
    def __wrap(java_value: __ParallelAction) -> 'ParallelAction':
        return ParallelAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParallelAction):
        """
        Dynamic initializer for ParallelAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__ParallelAction, self).setActor(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __ParallelAction(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__ParallelAction, self).addAction(arg0)

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.reset()"""
        super(ParallelAction, self).reset()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.restart()"""
        super(ParallelAction, self).restart()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction()"""
        val = __ParallelAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.toString()"""
        return str.__wrap(super(ParallelAction, self).toString())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def getActions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Action> com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.getActions()"""
        return 'utils.Array'.__wrap(super(ParallelAction, self).getActions())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction()"""
        val = __ParallelAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __ParallelAction(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __ParallelAction(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.act(float)"""
        return bool.__wrap(super(__ParallelAction, self).act(__float.valueOf(arg0)))

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
    def __init__(self, arg0: 'Action', arg1: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __ParallelAction(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action', arg4: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.ParallelAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __ParallelAction(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction as __ScaleByAction
__ScaleByAction = __ScaleByAction
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ScaleByAction(__RelativeTemporalAction, RelativeTemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction"""
 
    @staticmethod
    def __wrap(java_value: __ScaleByAction) -> 'ScaleByAction':
        return ScaleByAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScaleByAction):
        """
        Dynamic initializer for ScaleByAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getAmountY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.getAmountY()"""
        return float.__wrap(super(ScaleByAction, self).getAmountY())

    @overload
    def setAmount(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.setAmount(float)"""
        super(__ScaleByAction, self).setAmount(__float.valueOf(arg0))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @overload
    def setAmountX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.setAmountX(float)"""
        super(__ScaleByAction, self).setAmountX(__float.valueOf(arg0))

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setAmount(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.setAmount(float,float)"""
        super(__ScaleByAction, self).setAmount(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def setAmountY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.setAmountY(float)"""
        super(__ScaleByAction, self).setAmountY(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction()"""
        val = __ScaleByAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @overload
    def getAmountX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction.getAmountX()"""
        return float.__wrap(super(ScaleByAction, self).getAmountX())

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction()"""
        val = __ScaleByAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.IntAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import com.badlogic.gdx.scenes.scene2d.actions.IntAction as __IntAction
__IntAction = __IntAction
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class IntAction(__TemporalAction, TemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.IntAction"""
 
    @staticmethod
    def __wrap(java_value: __IntAction) -> 'IntAction':
        return IntAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntAction):
        """
        Dynamic initializer for IntAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction()"""
        val = __IntAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getStart(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.IntAction.getStart()"""
        return int.__wrap(super(IntAction, self).getStart())

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setValue(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.IntAction.setValue(int)"""
        super(__IntAction, self).setValue(__int.valueOf(arg0))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction()"""
        val = __IntAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float, arg3: 'Interpolation'):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction(int,int,float,com.badlogic.gdx.math.Interpolation)"""
        val = __IntAction(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setEnd(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.IntAction.setEnd(int)"""
        super(__IntAction, self).setEnd(__int.valueOf(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def getValue(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.IntAction.getValue()"""
        return int.__wrap(super(IntAction, self).getValue())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction(int,int)"""
        val = __IntAction(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @overload
    def getEnd(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.IntAction.getEnd()"""
        return int.__wrap(super(IntAction, self).getEnd())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.IntAction(int,int,float)"""
        val = __IntAction(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @overload
    def setStart(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.IntAction.setStart(int)"""
        super(__IntAction, self).setStart(__int.valueOf(arg0))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.AfterAction
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as __DelegateAction
__DelegateAction = __DelegateAction
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import com.badlogic.gdx.scenes.scene2d.actions.AfterAction as __AfterAction
__AfterAction = __AfterAction
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AfterAction(__DelegateAction, DelegateAction):
    """com.badlogic.gdx.scenes.scene2d.actions.AfterAction"""
 
    @staticmethod
    def __wrap(java_value: __AfterAction) -> 'AfterAction':
        return AfterAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AfterAction):
        """
        Dynamic initializer for AfterAction.
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
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'.__wrap(super(DelegateAction, self).getAction())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.AfterAction()"""
        val = __AfterAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__DelegateAction, self).setActor(arg0)

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
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AfterAction.restart()"""
        super(AfterAction, self).restart()

    @overload
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool.__wrap(super(__DelegateAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__DelegateAction, self).setAction(arg0)

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.AfterAction()"""
        val = __AfterAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AfterAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__AfterAction, self).setTarget(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str.__wrap(super(DelegateAction, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.DelegateAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as __DelegateAction
__DelegateAction = __DelegateAction
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DelegateAction(ABC, scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.DelegateAction"""
 
    @staticmethod
    def __wrap(java_value: __DelegateAction) -> 'DelegateAction':
        return DelegateAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DelegateAction):
        """
        Dynamic initializer for DelegateAction.
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
        """public com.badlogic.gdx.scenes.scene2d.actions.DelegateAction()"""
        val = __DelegateAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.DelegateAction()"""
        val = __DelegateAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__DelegateAction, self).setTarget(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__DelegateAction, self).setActor(arg0)

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.restart()"""
        super(DelegateAction, self).restart()

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
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool.__wrap(super(__DelegateAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__DelegateAction, self).setAction(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'.__wrap(super(DelegateAction, self).getAction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str.__wrap(super(DelegateAction, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.AddAction
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.actions.AddAction as __AddAction
__AddAction = __AddAction
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AddAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.AddAction"""
 
    @staticmethod
    def __wrap(java_value: __AddAction) -> 'AddAction':
        return AddAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AddAction):
        """
        Dynamic initializer for AddAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__AddAction, self).setAction(arg0)

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddAction.restart()"""
        super(AddAction, self).restart()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.AddAction.act(float)"""
        return bool.__wrap(super(__AddAction, self).act(__float.valueOf(arg0)))

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

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
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.AddAction()"""
        val = __AddAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.AddAction()"""
        val = __AddAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.AddAction.getAction()"""
        return 'scene2d.Action'.__wrap(super(AddAction, self).getAction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RunnableAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.Runnable as __Runnable
__Runnable = __Runnable
import com.badlogic.gdx.scenes.scene2d.actions.RunnableAction as __RunnableAction
__RunnableAction = __RunnableAction
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RunnableAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.RunnableAction"""
 
    @staticmethod
    def __wrap(java_value: __RunnableAction) -> 'RunnableAction':
        return RunnableAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RunnableAction):
        """
        Dynamic initializer for RunnableAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RunnableAction()"""
        val = __RunnableAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RunnableAction()"""
        val = __RunnableAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.act(float)"""
        return bool.__wrap(super(__RunnableAction, self).act(__float.valueOf(arg0)))

    @overload
    def getRunnable(self) -> 'Runnable':
        """public java.lang.Runnable com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.getRunnable()"""
        return 'Runnable'.__wrap(super(RunnableAction, self).getRunnable())

    @overload
    def setRunnable(self, arg0: 'Runnable'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.setRunnable(java.lang.Runnable)"""
        super(__RunnableAction, self).setRunnable(arg0)

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RunnableAction.reset()"""
        super(RunnableAction, self).reset()

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.EventAction
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import com.badlogic.gdx.scenes.scene2d.actions.EventAction as __EventAction
__EventAction = __EventAction
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EventAction(ABC, scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.EventAction"""
 
    @staticmethod
    def __wrap(java_value: __EventAction) -> 'EventAction':
        return EventAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventAction):
        """
        Dynamic initializer for EventAction.
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
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.act(float)"""
        return bool.__wrap(super(__EventAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.restart()"""
        super(EventAction, self).restart()

    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setActive(boolean)"""
        super(__EventAction, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @abstractmethod
    def handle(self, arg0: 'Event'):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.handle(T)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__EventAction, self).setTarget(arg0)

    @overload
    def __init__(self, arg0: 'Class'):
        """public com.badlogic.gdx.scenes.scene2d.actions.EventAction(java.lang.Class<? extends T>)"""
        val = __EventAction(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.isActive()"""
        return bool.__wrap(super(EventAction, self).isActive())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction as __AddListenerAction
__AddListenerAction = __AddListenerAction
import com.badlogic.gdx.scenes.scene2d.EventListener as __EventListener
__EventListener = __EventListener
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AddListenerAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction"""
 
    @staticmethod
    def __wrap(java_value: __AddListenerAction) -> 'AddListenerAction':
        return AddListenerAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AddListenerAction):
        """
        Dynamic initializer for AddListenerAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.act(float)"""
        return bool.__wrap(super(__AddListenerAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getListener(self) -> 'scene2d.EventListener':
        """public com.badlogic.gdx.scenes.scene2d.EventListener com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.getListener()"""
        return 'scene2d.EventListener'.__wrap(super(AddListenerAction, self).getListener())

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
    def setListener(self, arg0: 'EventListener'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.setListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        super(__AddListenerAction, self).setListener(arg0)

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.setCapture(boolean)"""
        super(__AddListenerAction, self).setCapture(__boolean.valueOf(arg0))

    @overload
    def getCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction.getCapture()"""
        return bool.__wrap(super(AddListenerAction, self).getCapture())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction()"""
        val = __AddListenerAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction()"""
        val = __AddListenerAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RepeatAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.RepeatAction as __RepeatAction
__RepeatAction = __RepeatAction
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as __DelegateAction
__DelegateAction = __DelegateAction
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RepeatAction(__DelegateAction, DelegateAction):
    """com.badlogic.gdx.scenes.scene2d.actions.RepeatAction"""
 
    @staticmethod
    def __wrap(java_value: __RepeatAction) -> 'RepeatAction':
        return RepeatAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RepeatAction):
        """
        Dynamic initializer for RepeatAction.
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
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @override
    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'.__wrap(super(DelegateAction, self).getAction())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RepeatAction()"""
        val = __RepeatAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def getCount(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.actions.RepeatAction.getCount()"""
        return int.__wrap(super(RepeatAction, self).getCount())

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str.__wrap(super(DelegateAction, self).toString())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__DelegateAction, self).setTarget(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__DelegateAction, self).setActor(arg0)

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
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool.__wrap(super(__DelegateAction, self).act(__float.valueOf(arg0)))

    @overload
    def setCount(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RepeatAction.setCount(int)"""
        super(__RepeatAction, self).setCount(__int.valueOf(arg0))

    @override
    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__DelegateAction, self).setAction(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RepeatAction()"""
        val = __RepeatAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RepeatAction.finish()"""
        super(RepeatAction, self).finish() 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction as __RemoveActorAction
__RemoveActorAction = __RemoveActorAction
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RemoveActorAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction"""
 
    @staticmethod
    def __wrap(java_value: __RemoveActorAction) -> 'RemoveActorAction':
        return RemoveActorAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemoveActorAction):
        """
        Dynamic initializer for RemoveActorAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction.restart()"""
        super(RemoveActorAction, self).restart()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

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
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction()"""
        val = __RemoveActorAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction.act(float)"""
        return bool.__wrap(super(__RemoveActorAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction()"""
        val = __RemoveActorAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.EventListener as __EventListener
__EventListener = __EventListener
import com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction as __RemoveListenerAction
__RemoveListenerAction = __RemoveListenerAction
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RemoveListenerAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction"""
 
    @staticmethod
    def __wrap(java_value: __RemoveListenerAction) -> 'RemoveListenerAction':
        return RemoveListenerAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemoveListenerAction):
        """
        Dynamic initializer for RemoveListenerAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.setCapture(boolean)"""
        super(__RemoveListenerAction, self).setCapture(__boolean.valueOf(arg0))

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.act(float)"""
        return bool.__wrap(super(__RemoveListenerAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @overload
    def getCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.getCapture()"""
        return bool.__wrap(super(RemoveListenerAction, self).getCapture())

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
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction()"""
        val = __RemoveListenerAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction()"""
        val = __RemoveListenerAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

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
    def setListener(self, arg0: 'EventListener'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.setListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        super(__RemoveListenerAction, self).setListener(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getListener(self) -> 'scene2d.EventListener':
        """public com.badlogic.gdx.scenes.scene2d.EventListener com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction.getListener()"""
        return 'scene2d.EventListener'.__wrap(super(RemoveListenerAction, self).getListener()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction as __RelativeTemporalAction
__RelativeTemporalAction = __RelativeTemporalAction
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RelativeTemporalAction(ABC, __TemporalAction, TemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction"""
 
    @staticmethod
    def __wrap(java_value: __RelativeTemporalAction) -> 'RelativeTemporalAction':
        return RelativeTemporalAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RelativeTemporalAction):
        """
        Dynamic initializer for RelativeTemporalAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction()"""
        val = __RelativeTemporalAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RelativeTemporalAction()"""
        val = __RelativeTemporalAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.FloatAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import com.badlogic.gdx.scenes.scene2d.actions.FloatAction as __FloatAction
__FloatAction = __FloatAction
from builtins import bool
from builtins import int
 
class FloatAction(__TemporalAction, TemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.FloatAction"""
 
    @staticmethod
    def __wrap(java_value: __FloatAction) -> 'FloatAction':
        return FloatAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatAction):
        """
        Dynamic initializer for FloatAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setEnd(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.FloatAction.setEnd(float)"""
        super(__FloatAction, self).setEnd(__float.valueOf(arg0))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @overload
    def setValue(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.FloatAction.setValue(float)"""
        super(__FloatAction, self).setValue(__float.valueOf(arg0))

    @overload
    def setStart(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.FloatAction.setStart(float)"""
        super(__FloatAction, self).setStart(__float.valueOf(arg0))

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction()"""
        val = __FloatAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: 'Interpolation'):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        val = __FloatAction(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getEnd(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.FloatAction.getEnd()"""
        return float.__wrap(super(FloatAction, self).getEnd())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def getStart(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.FloatAction.getStart()"""
        return float.__wrap(super(FloatAction, self).getStart())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction(float,float)"""
        val = __FloatAction(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getValue(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.FloatAction.getValue()"""
        return float.__wrap(super(FloatAction, self).getValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction(float,float,float)"""
        val = __FloatAction(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.FloatAction()"""
        val = __FloatAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.TouchableAction
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.scenes.scene2d.Touchable as __Touchable
__Touchable = __Touchable
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import com.badlogic.gdx.scenes.scene2d.actions.TouchableAction as __TouchableAction
__TouchableAction = __TouchableAction
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TouchableAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.TouchableAction"""
 
    @staticmethod
    def __wrap(java_value: __TouchableAction) -> 'TouchableAction':
        return TouchableAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TouchableAction):
        """
        Dynamic initializer for TouchableAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def getTouchable(self) -> 'scene2d.Touchable':
        """public com.badlogic.gdx.scenes.scene2d.Touchable com.badlogic.gdx.scenes.scene2d.actions.TouchableAction.getTouchable()"""
        return 'scene2d.Touchable'.__wrap(super(TouchableAction, self).getTouchable())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.TouchableAction()"""
        val = __TouchableAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.TouchableAction()"""
        val = __TouchableAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTouchable(self, arg0: 'Touchable'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TouchableAction.setTouchable(com.badlogic.gdx.scenes.scene2d.Touchable)"""
        super(__TouchableAction, self).setTouchable(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

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
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(scene2d.Action, self).restart()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TouchableAction.act(float)"""
        return bool.__wrap(super(__TouchableAction, self).act(__float.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RotateByAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.RotateByAction as __RotateByAction
__RotateByAction = __RotateByAction
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RotateByAction(__RelativeTemporalAction, RelativeTemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.RotateByAction"""
 
    @staticmethod
    def __wrap(java_value: __RotateByAction) -> 'RotateByAction':
        return RotateByAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RotateByAction):
        """
        Dynamic initializer for RotateByAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateByAction()"""
        val = __RotateByAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def getAmount(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.RotateByAction.getAmount()"""
        return float.__wrap(super(RotateByAction, self).getAmount())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RotateByAction()"""
        val = __RotateByAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0))

    @overload
    def setAmount(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RotateByAction.setAmount(float)"""
        super(__RotateByAction, self).setAmount(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.DelayAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.DelayAction as __DelayAction
__DelayAction = __DelayAction
from builtins import float
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as __DelegateAction
__DelegateAction = __DelegateAction
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DelayAction(__DelegateAction, DelegateAction):
    """com.badlogic.gdx.scenes.scene2d.actions.DelayAction"""
 
    @staticmethod
    def __wrap(java_value: __DelayAction) -> 'DelayAction':
        return DelayAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DelayAction):
        """
        Dynamic initializer for DelayAction.
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
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @override
    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'.__wrap(super(DelegateAction, self).getAction())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.DelayAction()"""
        val = __DelayAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.DelayAction.getTime()"""
        return float.__wrap(super(DelayAction, self).getTime())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str.__wrap(super(DelegateAction, self).toString())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.DelayAction.getDuration()"""
        return float.__wrap(super(DelayAction, self).getDuration())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__DelegateAction, self).setTarget(arg0)

    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelayAction.finish()"""
        super(DelayAction, self).finish()

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__DelegateAction, self).setActor(arg0)

    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelayAction.setDuration(float)"""
        super(__DelayAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.DelayAction(float)"""
        val = __DelayAction(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool.__wrap(super(__DelegateAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__DelegateAction, self).setAction(arg0)

    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelayAction.setTime(float)"""
        super(__DelayAction, self).setTime(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.DelayAction()"""
        val = __DelayAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelayAction.restart()"""
        super(DelayAction, self).restart() 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.Actions
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

import com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction as __TimeScaleAction
__TimeScaleAction = __TimeScaleAction
import java.lang.Boolean as __boolean
import com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction as __RemoveActorAction
__RemoveActorAction = __RemoveActorAction
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.DelayAction as __DelayAction
__DelayAction = __DelayAction
import com.badlogic.gdx.scenes.scene2d.actions.SequenceAction as __SequenceAction
__SequenceAction = __SequenceAction
import com.badlogic.gdx.scenes.scene2d.actions.RotateByAction as __RotateByAction
__RotateByAction = __RotateByAction
import com.badlogic.gdx.scenes.scene2d.actions.RotateToAction as __RotateToAction
__RotateToAction = __RotateToAction
import com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction as __RemoveListenerAction
__RemoveListenerAction = __RemoveListenerAction
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import com.badlogic.gdx.scenes.scene2d.actions.TouchableAction as __TouchableAction
__TouchableAction = __TouchableAction
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.scenes.scene2d.actions.ParallelAction as __ParallelAction
__ParallelAction = __ParallelAction
import com.badlogic.gdx.scenes.scene2d.actions.LayoutAction as __LayoutAction
__LayoutAction = __LayoutAction
import com.badlogic.gdx.scenes.scene2d.actions.AddAction as __AddAction
__AddAction = __AddAction
import com.badlogic.gdx.scenes.scene2d.actions.MoveToAction as __MoveToAction
__MoveToAction = __MoveToAction
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import com.badlogic.gdx.scenes.scene2d.actions.AfterAction as __AfterAction
__AfterAction = __AfterAction
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.actions.SizeByAction as __SizeByAction
__SizeByAction = __SizeByAction
import com.badlogic.gdx.scenes.scene2d.actions.MoveByAction as __MoveByAction
__MoveByAction = __MoveByAction
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.scenes.scene2d.actions.SizeToAction as __SizeToAction
__SizeToAction = __SizeToAction
import java.lang.Runnable as Runnable
import com.badlogic.gdx.scenes.scene2d.actions.RepeatAction as __RepeatAction
__RepeatAction = __RepeatAction
import com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction as __AddListenerAction
__AddListenerAction = __AddListenerAction
import com.badlogic.gdx.scenes.scene2d.actions.RunnableAction as __RunnableAction
__RunnableAction = __RunnableAction
import com.badlogic.gdx.scenes.scene2d.actions.ColorAction as __ColorAction
__ColorAction = __ColorAction
import java.lang.Long as __long
import java.lang.Float as __float
import com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction as __ScaleByAction
__ScaleByAction = __ScaleByAction
import com.badlogic.gdx.scenes.scene2d.actions.Actions as __Actions
__Actions = __Actions
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.actions.VisibleAction as __VisibleAction
__VisibleAction = __VisibleAction
import com.badlogic.gdx.scenes.scene2d.actions.RemoveAction as __RemoveAction
__RemoveAction = __RemoveAction
import java.lang.Integer as __int
import com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction as __ScaleToAction
__ScaleToAction = __ScaleToAction
import com.badlogic.gdx.scenes.scene2d.actions.AlphaAction as __AlphaAction
__AlphaAction = __AlphaAction
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class Actions():
    """com.badlogic.gdx.scenes.scene2d.actions.Actions"""
 
    @staticmethod
    def __wrap(java_value: __Actions) -> 'Actions':
        return Actions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Actions):
        """
        Dynamic initializer for Actions.
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
 
    @staticmethod
    @overload
    def removeActor() -> 'RemoveActorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeActor()"""
        return RemoveActorAction.__wrap(__Actions.removeActor())

    @staticmethod
    @overload
    def rotateTo(arg0: float, arg1: float, arg2: 'Interpolation') -> 'RotateToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateTo(float,float,com.badlogic.gdx.math.Interpolation)"""
        return RotateToAction.__wrap(__Actions.rotateTo(__float.valueOf(arg0), __float.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def fadeIn(arg0: float, arg1: 'Interpolation') -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.fadeIn(float,com.badlogic.gdx.math.Interpolation)"""
        return AlphaAction.__wrap(__Actions.fadeIn(__float.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def sizeBy(arg0: float, arg1: float) -> 'SizeByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeBy(float,float)"""
        return SizeByAction.__wrap(__Actions.sizeBy(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def after(arg0: 'Action') -> 'AfterAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AfterAction com.badlogic.gdx.scenes.scene2d.actions.Actions.after(com.badlogic.gdx.scenes.scene2d.Action)"""
        return AfterAction.__wrap(__Actions.after(arg0))

    @staticmethod
    @overload
    def moveToAligned(arg0: float, arg1: float, arg2: int, arg3: float, arg4: 'Interpolation') -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveToAligned(float,float,int,float,com.badlogic.gdx.math.Interpolation)"""
        return MoveToAction.__wrap(__Actions.moveToAligned(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def removeActor(arg0: 'Actor') -> 'RemoveActorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveActorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return RemoveActorAction.__wrap(__Actions.removeActor(arg0))

    @staticmethod
    @overload
    def show() -> 'VisibleAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.VisibleAction com.badlogic.gdx.scenes.scene2d.actions.Actions.show()"""
        return VisibleAction.__wrap(__Actions.show())

    @staticmethod
    @overload
    def sizeBy(arg0: float, arg1: float, arg2: float) -> 'SizeByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeBy(float,float,float)"""
        return SizeByAction.__wrap(__Actions.sizeBy(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def sequence(arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction.__wrap(__Actions.sequence(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def parallel(arg0: 'Action', arg1: 'Action', arg2: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction.__wrap(__Actions.parallel(arg0, arg1, arg2))

    @staticmethod
    @overload
    def rotateTo(arg0: float, arg1: float) -> 'RotateToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateTo(float,float)"""
        return RotateToAction.__wrap(__Actions.rotateTo(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def moveTo(arg0: float, arg1: float, arg2: float) -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveTo(float,float,float)"""
        return MoveToAction.__wrap(__Actions.moveTo(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def rotateBy(arg0: float) -> 'RotateByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateBy(float)"""
        return RotateByAction.__wrap(__Actions.rotateBy(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def alpha(arg0: float, arg1: float) -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.alpha(float,float)"""
        return AlphaAction.__wrap(__Actions.alpha(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def touchable(arg0: 'Touchable') -> 'TouchableAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.TouchableAction com.badlogic.gdx.scenes.scene2d.actions.Actions.touchable(com.badlogic.gdx.scenes.scene2d.Touchable)"""
        return TouchableAction.__wrap(__Actions.touchable(arg0))

    @staticmethod
    @overload
    def moveToAligned(arg0: float, arg1: float, arg2: int, arg3: float) -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveToAligned(float,float,int,float)"""
        return MoveToAction.__wrap(__Actions.moveToAligned(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def color(arg0: 'Color') -> 'ColorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ColorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.color(com.badlogic.gdx.graphics.Color)"""
        return ColorAction.__wrap(__Actions.color(arg0))

    @staticmethod
    @overload
    def sizeTo(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'SizeToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeTo(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return SizeToAction.__wrap(__Actions.sizeTo(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def rotateBy(arg0: float, arg1: float) -> 'RotateByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateBy(float,float)"""
        return RotateByAction.__wrap(__Actions.rotateBy(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def moveTo(arg0: float, arg1: float) -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveTo(float,float)"""
        return MoveToAction.__wrap(__Actions.moveTo(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.Actions()"""
        val = __Actions()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def action(arg0: 'Class') -> 'scene2d.Action':
        """public static <T extends com.badlogic.gdx.scenes.scene2d.Action> T com.badlogic.gdx.scenes.scene2d.actions.Actions.action(java.lang.Class<T>)"""
        return scene2d.Action.__wrap(__Actions.action(arg0))

    @staticmethod
    @overload
    def sizeBy(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'SizeByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeBy(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return SizeByAction.__wrap(__Actions.sizeBy(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def rotateBy(arg0: float, arg1: float, arg2: 'Interpolation') -> 'RotateByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateBy(float,float,com.badlogic.gdx.math.Interpolation)"""
        return RotateByAction.__wrap(__Actions.rotateBy(__float.valueOf(arg0), __float.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def repeat(arg0: int, arg1: 'Action') -> 'RepeatAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RepeatAction com.badlogic.gdx.scenes.scene2d.actions.Actions.repeat(int,com.badlogic.gdx.scenes.scene2d.Action)"""
        return RepeatAction.__wrap(__Actions.repeat(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def addAction(arg0: 'Action', arg1: 'Actor') -> 'AddAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AddAction com.badlogic.gdx.scenes.scene2d.actions.Actions.addAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return AddAction.__wrap(__Actions.addAction(arg0, arg1))

    @staticmethod
    @overload
    def sequence(arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action', arg4: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction.__wrap(__Actions.sequence(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def removeAction(arg0: 'Action') -> 'RemoveAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        return RemoveAction.__wrap(__Actions.removeAction(arg0))

    @staticmethod
    @overload
    def fadeOut(arg0: float, arg1: 'Interpolation') -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.fadeOut(float,com.badlogic.gdx.math.Interpolation)"""
        return AlphaAction.__wrap(__Actions.fadeOut(__float.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def hide() -> 'VisibleAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.VisibleAction com.badlogic.gdx.scenes.scene2d.actions.Actions.hide()"""
        return VisibleAction.__wrap(__Actions.hide())

    @staticmethod
    @overload
    def parallel(arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction.__wrap(__Actions.parallel(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def run(arg0: 'Runnable') -> 'RunnableAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RunnableAction com.badlogic.gdx.scenes.scene2d.actions.Actions.run(java.lang.Runnable)"""
        return RunnableAction.__wrap(__Actions.run(arg0))

    @staticmethod
    @overload
    def layout(arg0: bool) -> 'LayoutAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.LayoutAction com.badlogic.gdx.scenes.scene2d.actions.Actions.layout(boolean)"""
        return LayoutAction.__wrap(__Actions.layout(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def sequence(arg0: 'Action', arg1: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction.__wrap(__Actions.sequence(arg0, arg1))

    @staticmethod
    @overload
    def addAction(arg0: 'Action') -> 'AddAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AddAction com.badlogic.gdx.scenes.scene2d.actions.Actions.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        return AddAction.__wrap(__Actions.addAction(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def sequence(arg0: 'Action', arg1: 'Action', arg2: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction.__wrap(__Actions.sequence(arg0, arg1, arg2))

    @staticmethod
    @overload
    def sequence(*arg0: 'scene2d.Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action...)"""
        return SequenceAction.__wrap(__Actions.sequence(arg0))

    @staticmethod
    @overload
    def moveBy(arg0: float, arg1: float, arg2: float) -> 'MoveByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveBy(float,float,float)"""
        return MoveByAction.__wrap(__Actions.moveBy(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def parallel(arg0: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction.__wrap(__Actions.parallel(arg0))

    @staticmethod
    @overload
    def scaleTo(arg0: float, arg1: float, arg2: float) -> 'ScaleToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleTo(float,float,float)"""
        return ScaleToAction.__wrap(__Actions.scaleTo(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def rotateTo(arg0: float) -> 'RotateToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RotateToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.rotateTo(float)"""
        return RotateToAction.__wrap(__Actions.rotateTo(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def color(arg0: 'Color', arg1: float, arg2: 'Interpolation') -> 'ColorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ColorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.color(com.badlogic.gdx.graphics.Color,float,com.badlogic.gdx.math.Interpolation)"""
        return ColorAction.__wrap(__Actions.color(arg0, __float.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def moveToAligned(arg0: float, arg1: float, arg2: int) -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveToAligned(float,float,int)"""
        return MoveToAction.__wrap(__Actions.moveToAligned(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def delay(arg0: float, arg1: 'Action') -> 'DelayAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.DelayAction com.badlogic.gdx.scenes.scene2d.actions.Actions.delay(float,com.badlogic.gdx.scenes.scene2d.Action)"""
        return DelayAction.__wrap(__Actions.delay(__float.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def sequence() -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence()"""
        return SequenceAction.__wrap(__Actions.sequence())

    @staticmethod
    @overload
    def fadeIn(arg0: float) -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.fadeIn(float)"""
        return AlphaAction.__wrap(__Actions.fadeIn(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def parallel() -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel()"""
        return ParallelAction.__wrap(__Actions.parallel())

    @staticmethod
    @overload
    def moveBy(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'MoveByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveBy(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return MoveByAction.__wrap(__Actions.moveBy(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def alpha(arg0: float) -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.alpha(float)"""
        return AlphaAction.__wrap(__Actions.alpha(__float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def moveTo(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'MoveToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveTo(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return MoveToAction.__wrap(__Actions.moveTo(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def removeAction(arg0: 'Action', arg1: 'Actor') -> 'RemoveAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return RemoveAction.__wrap(__Actions.removeAction(arg0, arg1))

    @staticmethod
    @overload
    def sizeTo(arg0: float, arg1: float) -> 'SizeToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeTo(float,float)"""
        return SizeToAction.__wrap(__Actions.sizeTo(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def visible(arg0: bool) -> 'VisibleAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.VisibleAction com.badlogic.gdx.scenes.scene2d.actions.Actions.visible(boolean)"""
        return VisibleAction.__wrap(__Actions.visible(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def scaleTo(arg0: float, arg1: float) -> 'ScaleToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleTo(float,float)"""
        return ScaleToAction.__wrap(__Actions.scaleTo(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def alpha(arg0: float, arg1: float, arg2: 'Interpolation') -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.alpha(float,float,com.badlogic.gdx.math.Interpolation)"""
        return AlphaAction.__wrap(__Actions.alpha(__float.valueOf(arg0), __float.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def parallel(arg0: 'Action', arg1: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction.__wrap(__Actions.parallel(arg0, arg1))

    @staticmethod
    @overload
    def sequence(arg0: 'Action') -> 'SequenceAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SequenceAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sequence(com.badlogic.gdx.scenes.scene2d.Action)"""
        return SequenceAction.__wrap(__Actions.sequence(arg0))

    @staticmethod
    @overload
    def moveBy(arg0: float, arg1: float) -> 'MoveByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.MoveByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.moveBy(float,float)"""
        return MoveByAction.__wrap(__Actions.moveBy(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.Actions()"""
        val = __Actions()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def timeScale(arg0: float, arg1: 'Action') -> 'TimeScaleAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction com.badlogic.gdx.scenes.scene2d.actions.Actions.timeScale(float,com.badlogic.gdx.scenes.scene2d.Action)"""
        return TimeScaleAction.__wrap(__Actions.timeScale(__float.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def color(arg0: 'Color', arg1: float) -> 'ColorAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ColorAction com.badlogic.gdx.scenes.scene2d.actions.Actions.color(com.badlogic.gdx.graphics.Color,float)"""
        return ColorAction.__wrap(__Actions.color(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def scaleBy(arg0: float, arg1: float, arg2: float) -> 'ScaleByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleBy(float,float,float)"""
        return ScaleByAction.__wrap(__Actions.scaleBy(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def fadeOut(arg0: float) -> 'AlphaAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AlphaAction com.badlogic.gdx.scenes.scene2d.actions.Actions.fadeOut(float)"""
        return AlphaAction.__wrap(__Actions.fadeOut(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def scaleTo(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'ScaleToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleTo(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return ScaleToAction.__wrap(__Actions.scaleTo(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def addListener(arg0: 'EventListener', arg1: bool, arg2: 'Actor') -> 'AddListenerAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction com.badlogic.gdx.scenes.scene2d.actions.Actions.addListener(com.badlogic.gdx.scenes.scene2d.EventListener,boolean,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return AddListenerAction.__wrap(__Actions.addListener(arg0, __boolean.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def removeListener(arg0: 'EventListener', arg1: bool) -> 'RemoveListenerAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener,boolean)"""
        return RemoveListenerAction.__wrap(__Actions.removeListener(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def scaleBy(arg0: float, arg1: float, arg2: float, arg3: 'Interpolation') -> 'ScaleByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleBy(float,float,float,com.badlogic.gdx.math.Interpolation)"""
        return ScaleByAction.__wrap(__Actions.scaleBy(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def scaleBy(arg0: float, arg1: float) -> 'ScaleByAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ScaleByAction com.badlogic.gdx.scenes.scene2d.actions.Actions.scaleBy(float,float)"""
        return ScaleByAction.__wrap(__Actions.scaleBy(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def parallel(*arg0: 'scene2d.Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action...)"""
        return ParallelAction.__wrap(__Actions.parallel(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def parallel(arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action', arg4: 'Action') -> 'ParallelAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.ParallelAction com.badlogic.gdx.scenes.scene2d.actions.Actions.parallel(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        return ParallelAction.__wrap(__Actions.parallel(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def sizeTo(arg0: float, arg1: float, arg2: float) -> 'SizeToAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.SizeToAction com.badlogic.gdx.scenes.scene2d.actions.Actions.sizeTo(float,float,float)"""
        return SizeToAction.__wrap(__Actions.sizeTo(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def forever(arg0: 'Action') -> 'RepeatAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RepeatAction com.badlogic.gdx.scenes.scene2d.actions.Actions.forever(com.badlogic.gdx.scenes.scene2d.Action)"""
        return RepeatAction.__wrap(__Actions.forever(arg0))

    @staticmethod
    @overload
    def addListener(arg0: 'EventListener', arg1: bool) -> 'AddListenerAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.AddListenerAction com.badlogic.gdx.scenes.scene2d.actions.Actions.addListener(com.badlogic.gdx.scenes.scene2d.EventListener,boolean)"""
        return AddListenerAction.__wrap(__Actions.addListener(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def removeListener(arg0: 'EventListener', arg1: bool, arg2: 'Actor') -> 'RemoveListenerAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.RemoveListenerAction com.badlogic.gdx.scenes.scene2d.actions.Actions.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener,boolean,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return RemoveListenerAction.__wrap(__Actions.removeListener(arg0, __boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def delay(arg0: float) -> 'DelayAction':
        """public static com.badlogic.gdx.scenes.scene2d.actions.DelayAction com.badlogic.gdx.scenes.scene2d.actions.Actions.delay(float)"""
        return DelayAction.__wrap(__Actions.delay(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def targeting(arg0: 'Actor', arg1: 'Action') -> 'scene2d.Action':
        """public static com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.Actions.targeting(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Action)"""
        return scene2d.Action.__wrap(__Actions.targeting(arg0, arg1)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.ColorAction
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.actions.ColorAction as __ColorAction
__ColorAction = __ColorAction
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ColorAction(__TemporalAction, TemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.ColorAction"""
 
    @staticmethod
    def __wrap(java_value: __ColorAction) -> 'ColorAction':
        return ColorAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ColorAction):
        """
        Dynamic initializer for ColorAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.ColorAction()"""
        val = __ColorAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ColorAction.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__ColorAction, self).setColor(arg0)

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.actions.ColorAction.getColor()"""
        return 'graphics.Color'.__wrap(super(ColorAction, self).getColor())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setEndColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ColorAction.setEndColor(com.badlogic.gdx.graphics.Color)"""
        super(__ColorAction, self).setEndColor(arg0)

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @overload
    def getEndColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.actions.ColorAction.getEndColor()"""
        return 'graphics.Color'.__wrap(super(ColorAction, self).getEndColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

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
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ColorAction.reset()"""
        super(ColorAction, self).reset()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.ColorAction()"""
        val = __ColorAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.SequenceAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.actions.SequenceAction as __SequenceAction
__SequenceAction = __SequenceAction
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import com.badlogic.gdx.scenes.scene2d.actions.ParallelAction as __ParallelAction
__ParallelAction = __ParallelAction
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SequenceAction(__ParallelAction, ParallelAction):
    """com.badlogic.gdx.scenes.scene2d.actions.SequenceAction"""
 
    @staticmethod
    def __wrap(java_value: __SequenceAction) -> 'SequenceAction':
        return SequenceAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SequenceAction):
        """
        Dynamic initializer for SequenceAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action', arg4: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __SequenceAction(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action', arg3: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __SequenceAction(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__ParallelAction, self).setActor(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction()"""
        val = __SequenceAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.reset()"""
        super(ParallelAction, self).reset()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self, arg0: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __SequenceAction(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __SequenceAction(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.toString()"""
        return str.__wrap(super(ParallelAction, self).toString())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SequenceAction.restart()"""
        super(SequenceAction, self).restart()

    @override
    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__ParallelAction, self).addAction(arg0)

    @override
    @overload
    def getActions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Action> com.badlogic.gdx.scenes.scene2d.actions.ParallelAction.getActions()"""
        return 'utils.Array'.__wrap(super(ParallelAction, self).getActions())

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction()"""
        val = __SequenceAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.SequenceAction.act(float)"""
        return bool.__wrap(super(__SequenceAction, self).act(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Action', arg1: 'Action', arg2: 'Action'):
        """public com.badlogic.gdx.scenes.scene2d.actions.SequenceAction(com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action,com.badlogic.gdx.scenes.scene2d.Action)"""
        val = __SequenceAction(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.VisibleAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.actions.VisibleAction as __VisibleAction
__VisibleAction = __VisibleAction
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class VisibleAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.VisibleAction"""
 
    @staticmethod
    def __wrap(java_value: __VisibleAction) -> 'VisibleAction':
        return VisibleAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VisibleAction):
        """
        Dynamic initializer for VisibleAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.VisibleAction.setVisible(boolean)"""
        super(__VisibleAction, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.VisibleAction()"""
        val = __VisibleAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

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
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.VisibleAction.act(float)"""
        return bool.__wrap(super(__VisibleAction, self).act(__float.valueOf(arg0)))

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.VisibleAction()"""
        val = __VisibleAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.VisibleAction.isVisible()"""
        return bool.__wrap(super(VisibleAction, self).isVisible())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction as __ScaleToAction
__ScaleToAction = __ScaleToAction
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ScaleToAction(__TemporalAction, TemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction"""
 
    @staticmethod
    def __wrap(java_value: __ScaleToAction) -> 'ScaleToAction':
        return ScaleToAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScaleToAction):
        """
        Dynamic initializer for ScaleToAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.setX(float)"""
        super(__ScaleToAction, self).setX(__float.valueOf(arg0))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction()"""
        val = __ScaleToAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.setScale(float,float)"""
        super(__ScaleToAction, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.getX()"""
        return float.__wrap(super(ScaleToAction, self).getX())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.getY()"""
        return float.__wrap(super(ScaleToAction, self).getY())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.setScale(float)"""
        super(__ScaleToAction, self).setScale(__float.valueOf(arg0))

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction.setY(float)"""
        super(__ScaleToAction, self).setY(__float.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.ScaleToAction()"""
        val = __ScaleToAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.AlphaAction
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import com.badlogic.gdx.scenes.scene2d.actions.AlphaAction as __AlphaAction
__AlphaAction = __AlphaAction
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class AlphaAction(__TemporalAction, TemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.AlphaAction"""
 
    @staticmethod
    def __wrap(java_value: __AlphaAction) -> 'AlphaAction':
        return AlphaAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AlphaAction):
        """
        Dynamic initializer for AlphaAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.getColor()"""
        return 'graphics.Color'.__wrap(super(AlphaAction, self).getColor())

    @overload
    def setAlpha(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.setAlpha(float)"""
        super(__AlphaAction, self).setAlpha(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.AlphaAction()"""
        val = __AlphaAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.AlphaAction()"""
        val = __AlphaAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAlpha(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.getAlpha()"""
        return float.__wrap(super(AlphaAction, self).getAlpha())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

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
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__AlphaAction, self).setColor(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.AlphaAction.reset()"""
        super(AlphaAction, self).reset() 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import com.badlogic.gdx.scenes.scene2d.actions.EventAction as __EventAction
__EventAction = __EventAction
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction as __CountdownEventAction
__CountdownEventAction = __CountdownEventAction
from builtins import int
 
class CountdownEventAction(__EventAction, EventAction):
    """com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction"""
 
    @staticmethod
    def __wrap(java_value: __CountdownEventAction) -> 'CountdownEventAction':
        return CountdownEventAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CountdownEventAction):
        """
        Dynamic initializer for CountdownEventAction.
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
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @overload
    def __init__(self, arg0: 'Class', arg1: int):
        """public com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction(java.lang.Class<? extends T>,int)"""
        val = __CountdownEventAction(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(scene2d.Action, self).reset()

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.act(float)"""
        return bool.__wrap(super(__EventAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.restart()"""
        super(EventAction, self).restart()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

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
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setActive(boolean)"""
        super(__EventAction, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.EventAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__EventAction, self).setTarget(arg0)

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.CountdownEventAction.handle(T)"""
        return bool.__wrap(super(__CountdownEventAction, self).handle(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.EventAction.isActive()"""
        return bool.__wrap(super(EventAction, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.MoveByAction
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.scenes.scene2d.actions.MoveByAction as __MoveByAction
__MoveByAction = __MoveByAction
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MoveByAction(__RelativeTemporalAction, RelativeTemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.MoveByAction"""
 
    @staticmethod
    def __wrap(java_value: __MoveByAction) -> 'MoveByAction':
        return MoveByAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MoveByAction):
        """
        Dynamic initializer for MoveByAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.MoveByAction()"""
        val = __MoveByAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setAmountX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.setAmountX(float)"""
        super(__MoveByAction, self).setAmountX(__float.valueOf(arg0))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.MoveByAction()"""
        val = __MoveByAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAmountX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.getAmountX()"""
        return float.__wrap(super(MoveByAction, self).getAmountX())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @overload
    def setAmountY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.setAmountY(float)"""
        super(__MoveByAction, self).setAmountY(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @overload
    def getAmountY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.getAmountY()"""
        return float.__wrap(super(MoveByAction, self).getAmountY())

    @overload
    def setAmount(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.MoveByAction.setAmount(float,float)"""
        super(__MoveByAction, self).setAmount(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

import com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction as __TimeScaleAction
__TimeScaleAction = __TimeScaleAction
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.actions.DelegateAction as __DelegateAction
__DelegateAction = __DelegateAction
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TimeScaleAction(__DelegateAction, DelegateAction):
    """com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction"""
 
    @staticmethod
    def __wrap(java_value: __TimeScaleAction) -> 'TimeScaleAction':
        return TimeScaleAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimeScaleAction):
        """
        Dynamic initializer for TimeScaleAction.
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
    def getScale(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction.getScale()"""
        return float.__wrap(super(TimeScaleAction, self).getScale())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.reset()"""
        super(DelegateAction, self).reset()

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.getAction()"""
        return 'scene2d.Action'.__wrap(super(DelegateAction, self).getAction())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__DelegateAction, self).setTarget(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__DelegateAction, self).setActor(arg0)

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.restart()"""
        super(DelegateAction, self).restart()

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
    def act(self, arg0: float) -> bool:
        """public final boolean com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.act(float)"""
        return bool.__wrap(super(__DelegateAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__DelegateAction, self).setAction(arg0)

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction()"""
        val = __TimeScaleAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction()"""
        val = __TimeScaleAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TimeScaleAction.setScale(float)"""
        super(__TimeScaleAction, self).setScale(__float.valueOf(arg0))

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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.actions.DelegateAction.toString()"""
        return str.__wrap(super(DelegateAction, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.RemoveAction
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.actions.RemoveAction as __RemoveAction
__RemoveAction = __RemoveAction
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RemoveAction(scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.RemoveAction"""
 
    @staticmethod
    def __wrap(java_value: __RemoveAction) -> 'RemoveAction':
        return RemoveAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RemoveAction):
        """
        Dynamic initializer for RemoveAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAction(self) -> 'scene2d.Action':
        """public com.badlogic.gdx.scenes.scene2d.Action com.badlogic.gdx.scenes.scene2d.actions.RemoveAction.getAction()"""
        return 'scene2d.Action'.__wrap(super(RemoveAction, self).getAction())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @overload
    def setAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveAction.setAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__RemoveAction, self).setAction(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.RemoveAction.act(float)"""
        return bool.__wrap(super(__RemoveAction, self).act(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveAction()"""
        val = __RemoveAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.RemoveAction.reset()"""
        super(RemoveAction, self).reset()

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
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.RemoveAction()"""
        val = __RemoveAction()
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.TemporalAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TemporalAction(ABC, scenes.__Action, scene2d.Action):
    """com.badlogic.gdx.scenes.scene2d.actions.TemporalAction"""
 
    @staticmethod
    def __wrap(java_value: __TemporalAction) -> 'TemporalAction':
        return TemporalAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TemporalAction):
        """
        Dynamic initializer for TemporalAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.TemporalAction()"""
        val = __TemporalAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.TemporalAction()"""
        val = __TemporalAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.scenes.scene2d.actions.TemporalAction(float)"""
        val = __TemporalAction(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: 'Interpolation'):
        """public com.badlogic.gdx.scenes.scene2d.actions.TemporalAction(float,com.badlogic.gdx.math.Interpolation)"""
        val = __TemporalAction(__float.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.actions.SizeByAction
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.scenes.scene2d.actions.TemporalAction as __TemporalAction
__TemporalAction = __TemporalAction
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.scenes.scene2d.actions.SizeByAction as __SizeByAction
__SizeByAction = __SizeByAction
from builtins import int
 
class SizeByAction(__RelativeTemporalAction, RelativeTemporalAction):
    """com.badlogic.gdx.scenes.scene2d.actions.SizeByAction"""
 
    @staticmethod
    def __wrap(java_value: __SizeByAction) -> 'SizeByAction':
        return SizeByAction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SizeByAction):
        """
        Dynamic initializer for SizeByAction.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setTarget(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__TemporalAction, self).setInterpolation(arg0)

    @override
    @overload
    def setDuration(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setDuration(float)"""
        super(__TemporalAction, self).setDuration(__float.valueOf(arg0))

    @override
    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.restart()"""
        super(TemporalAction, self).restart()

    @override
    @overload
    def setReverse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setReverse(boolean)"""
        super(__TemporalAction, self).setReverse(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setAmountHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.setAmountHeight(float)"""
        super(__SizeByAction, self).setAmountHeight(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getActor())

    @overload
    def setAmount(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.setAmount(float,float)"""
        super(__SizeByAction, self).setAmount(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Action, self).getTarget())

    @overload
    def setAmountWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.setAmountWidth(float)"""
        super(__SizeByAction, self).setAmountWidth(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.actions.SizeByAction()"""
        val = __SizeByAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(scene2d.Action, self).getPool())

    @override
    @overload
    def getDuration(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getDuration()"""
        return float.__wrap(super(TemporalAction, self).getDuration())

    @override
    @overload
    def isReverse(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isReverse()"""
        return bool.__wrap(super(TemporalAction, self).isReverse())

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Action, self).setActor(arg0)

    @override
    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__scene2d.Action, self).setPool(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(scene2d.Action, self).toString())

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.isComplete()"""
        return bool.__wrap(super(TemporalAction, self).isComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.reset()"""
        super(TemporalAction, self).reset()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def finish(self):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.finish()"""
        super(TemporalAction, self).finish()

    @override
    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(TemporalAction, self).getInterpolation())

    @overload
    def getAmountHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.getAmountHeight()"""
        return float.__wrap(super(SizeByAction, self).getAmountHeight())

    @overload
    def act(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.act(float)"""
        return bool.__wrap(super(__TemporalAction, self).act(__float.valueOf(arg0)))

    @overload
    def getAmountWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.SizeByAction.getAmountWidth()"""
        return float.__wrap(super(SizeByAction, self).getAmountWidth())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.actions.SizeByAction()"""
        val = __SizeByAction()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.getTime()"""
        return float.__wrap(super(TemporalAction, self).getTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setTime(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.actions.TemporalAction.setTime(float)"""
        super(__TemporalAction, self).setTime(__float.valueOf(arg0))
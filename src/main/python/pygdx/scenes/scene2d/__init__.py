from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
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
 
class Action(ABC):
    """com.badlogic.gdx.scenes.scene2d.Action"""
 
    @staticmethod
    def __wrap(java_value: __Action) -> 'Action':
        return Action(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Action):
        """
        Dynamic initializer for Action.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Action, self).setTarget(arg0)

    @overload
    def getTarget(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'Actor'.__wrap(super(Action, self).getTarget())

    @abstractmethod
    def act(self, arg0: float):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.Action.act(float)"""
        pass

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Action()"""
        val = __Action()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(Action, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(Action, self).restart()

    @overload
    def getActor(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'Actor'.__wrap(super(Action, self).getActor())

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
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(Action, self).reset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Action()"""
        val = __Action()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(Action, self).getPool())

    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Action, self).setActor(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Action
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import com.badlogic.gdx.scenes.scene2d.Action as __Action
__Action = __Action
import java.lang.Long as __long
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
 
class Action(ABC):
    """com.badlogic.gdx.scenes.scene2d.Action"""
 
    @staticmethod
    def __wrap(java_value: __Action) -> 'Action':
        return Action(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Action):
        """
        Dynamic initializer for Action.
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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Action, self).setTarget(arg0)

    @overload
    def getTarget(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getTarget()"""
        return 'Actor'.__wrap(super(Action, self).getTarget())

    @abstractmethod
    def act(self, arg0: float):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.Action.act(float)"""
        pass

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Action()"""
        val = __Action()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Action.toString()"""
        return str.__wrap(super(Action, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setPool(self, arg0: 'Pool'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setPool(com.badlogic.gdx.utils.Pool)"""
        super(__Action, self).setPool(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def restart(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.restart()"""
        super(Action, self).restart()

    @overload
    def getActor(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Action.getActor()"""
        return 'Actor'.__wrap(super(Action, self).getActor())

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
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Action.reset()"""
        super(Action, self).reset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Action()"""
        val = __Action()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getPool(self) -> 'utils.Pool':
        """public com.badlogic.gdx.utils.Pool com.badlogic.gdx.scenes.scene2d.Action.getPool()"""
        return 'utils.Pool'.__wrap(super(Action, self).getPool())

    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Action.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Action, self).setActor(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Action 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Event
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Event as __Event
__Event = __Event
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import com.badlogic.gdx.scenes.scene2d.Stage as __Stage
__Stage = __Stage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Event():
    """com.badlogic.gdx.scenes.scene2d.Event"""
 
    @staticmethod
    def __wrap(java_value: __Event) -> 'Event':
        return Event(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Event):
        """
        Dynamic initializer for Event.
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
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCancelled()"""
        return bool.__wrap(super(Event, self).isCancelled())

    @overload
    def setListenerActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setListenerActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Event, self).setListenerActor(arg0)

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
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Event, self).setTarget(arg0)

    @overload
    def isCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCapture()"""
        return bool.__wrap(super(Event, self).isCapture())

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
    def getTarget(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getTarget()"""
        return 'Actor'.__wrap(super(Event, self).getTarget())

    @overload
    def stop(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.stop()"""
        super(Event, self).stop()

    @overload
    def isHandled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isHandled()"""
        return bool.__wrap(super(Event, self).isHandled())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setCapture(boolean)"""
        super(__Event, self).setCapture(__boolean.valueOf(arg0))

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.cancel()"""
        super(Event, self).cancel()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getStage(self) -> 'Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Event.getStage()"""
        return 'Stage'.__wrap(super(Event, self).getStage())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Event()"""
        val = __Event()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Event()"""
        val = __Event()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isStopped(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isStopped()"""
        return bool.__wrap(super(Event, self).isStopped())

    @overload
    def getListenerActor(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getListenerActor()"""
        return 'Actor'.__wrap(super(Event, self).getListenerActor())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setStage(self, arg0: 'Stage'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setStage(com.badlogic.gdx.scenes.scene2d.Stage)"""
        super(__Event, self).setStage(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setBubbles(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setBubbles(boolean)"""
        super(__Event, self).setBubbles(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getBubbles(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.getBubbles()"""
        return bool.__wrap(super(Event, self).getBubbles()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Group
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.scenes.scene2d.Touchable as __Touchable
__Touchable = __Touchable
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.scenes.scene2d.Group as __Group
__Group = __Group
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
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
import java.lang.Object as __object
from builtins import float
from builtins import object
import com.badlogic.gdx.utils.DelayedRemovalArray as __DelayedRemovalArray
__DelayedRemovalArray = __DelayedRemovalArray
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.SnapshotArray as __SnapshotArray
__SnapshotArray = __SnapshotArray
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
import com.badlogic.gdx.scenes.scene2d.Stage as __Stage
__Stage = __Stage
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class Group():
    """com.badlogic.gdx.scenes.scene2d.Group"""
 
    @staticmethod
    def __wrap(java_value: __Group) -> 'Group':
        return Group(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Group):
        """
        Dynamic initializer for Group.
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
    def sizeBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.sizeBy(float,float)"""
        super(__Actor, self).sizeBy(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScale(float)"""
        super(__Actor, self).setScale(__float.valueOf(arg0))

    @override
    @overload
    def getZIndex(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.Actor.getZIndex()"""
        return int.__wrap(super(Actor, self).getZIndex())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setVisible(boolean)"""
        super(__Actor, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getX()"""
        return float.__wrap(super(Actor, self).getX())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setColor(float,float,float,float)"""
        super(__Actor, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def hit(self, arg0: float, arg1: float, arg2: bool) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Group.hit(float,float,boolean)"""
        return 'Actor'.__wrap(super(__Group, self).hit(__float.valueOf(arg0), __float.valueOf(arg1), __boolean.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCaptureListeners(self) -> 'utils.DelayedRemovalArray':
        """public com.badlogic.gdx.utils.DelayedRemovalArray<com.badlogic.gdx.scenes.scene2d.EventListener> com.badlogic.gdx.scenes.scene2d.Actor.getCaptureListeners()"""
        return 'utils.DelayedRemovalArray'.__wrap(super(Actor, self).getCaptureListeners())

    @overload
    def addActorAt(self, arg0: int, arg1: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.addActorAt(int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Group, self).addActorAt(__int.valueOf(arg0), arg1)

    @overload
    def hasChildren(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.hasChildren()"""
        return bool.__wrap(super(Group, self).hasChildren())

    @overload
    def fire(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.fire(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool.__wrap(super(__Actor, self).fire(arg0))

    @overload
    def addActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.addActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Group, self).addActor(arg0)

    @override
    @overload
    def getDebug(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.getDebug()"""
        return bool.__wrap(super(Actor, self).getDebug())

    @overload
    def stageToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.stageToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).stageToLocalCoordinates(arg0))

    @override
    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOrigin(float,float)"""
        super(__Actor, self).setOrigin(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def clearChildren(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Group.clearChildren(boolean)"""
        super(__Group, self).clearChildren(__boolean.valueOf(arg0))

    @overload
    def addCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.addCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Actor, self).addCaptureListener(arg0))

    @override
    @overload
    def getUserObject(self) -> object:
        """public java.lang.Object com.badlogic.gdx.scenes.scene2d.Actor.getUserObject()"""
        return object.__wrap(super(Actor, self).getUserObject())

    @override
    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getRotation()"""
        return float.__wrap(super(Actor, self).getRotation())

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.Group.clear()"""
        super(Group, self).clear()

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isVisible()"""
        return bool.__wrap(super(Actor, self).isVisible())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getY(self, arg0: int) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getY(int)"""
        return float.__wrap(super(__Actor, self).getY(__int.valueOf(arg0)))

    @overload
    def setTransform(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Group.setTransform(boolean)"""
        super(__Group, self).setTransform(__boolean.valueOf(arg0))

    @override
    @overload
    def setUserObject(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setUserObject(java.lang.Object)"""
        super(__Actor, self).setUserObject(arg0)

    @override
    @overload
    def drawDebug(self, arg0: 'ShapeRenderer'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.drawDebug(com.badlogic.gdx.graphics.glutils.ShapeRenderer)"""
        super(__Group, self).drawDebug(arg0)

    @override
    @overload
    def getActions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Action> com.badlogic.gdx.scenes.scene2d.Actor.getActions()"""
        return 'utils.Array'.__wrap(super(Actor, self).getActions())

    @override
    @overload
    def scaleBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.scaleBy(float,float)"""
        super(__Actor, self).scaleBy(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def addActorAfter(self, arg0: 'Actor', arg1: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.addActorAfter(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Group, self).addActorAfter(arg0, arg1)

    @overload
    def isTransform(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.isTransform()"""
        return bool.__wrap(super(Group, self).isTransform())

    @overload
    def getCullingArea(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.scenes.scene2d.Group.getCullingArea()"""
        return 'math.Rectangle'.__wrap(super(Group, self).getCullingArea())

    @overload
    def getChild(self, arg0: int) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Group.getChild(int)"""
        return 'Actor'.__wrap(super(__Group, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setSize(float,float)"""
        super(__Actor, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def notify(self, arg0: 'Event', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.notify(com.badlogic.gdx.scenes.scene2d.Event,boolean)"""
        return bool.__wrap(super(__Actor, self).notify(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOriginX(float)"""
        super(__Actor, self).setOriginX(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setRotation(float)"""
        super(__Actor, self).setRotation(__float.valueOf(arg0))

    @override
    @overload
    def isTouchFocusListener(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchFocusListener()"""
        return bool.__wrap(super(Actor, self).isTouchFocusListener())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setDebug(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Group.setDebug(boolean,boolean)"""
        super(__Group, self).setDebug(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def clear(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Group.clear(boolean)"""
        super(__Group, self).clear(__boolean.valueOf(arg0))

    @override
    @overload
    def getTouchable(self) -> 'Touchable':
        """public com.badlogic.gdx.scenes.scene2d.Touchable com.badlogic.gdx.scenes.scene2d.Actor.getTouchable()"""
        return 'Touchable'.__wrap(super(Actor, self).getTouchable())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Group()"""
        val = __Group()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def debug(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Actor.debug()"""
        return 'Actor'.__wrap(super(Actor, self).debug())

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.Actor.getColor()"""
        return 'graphics.Color'.__wrap(super(Actor, self).getColor())

    @override
    @overload
    def ascendantsVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.ascendantsVisible()"""
        return bool.__wrap(super(Actor, self).ascendantsVisible())

    @override
    @overload
    def setHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setHeight(float)"""
        super(__Actor, self).setHeight(__float.valueOf(arg0))

    @overload
    def getX(self, arg0: int) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getX(int)"""
        return float.__wrap(super(__Actor, self).getX(__int.valueOf(arg0)))

    @override
    @overload
    def removeAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.removeAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__Actor, self).removeAction(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getOriginX()"""
        return float.__wrap(super(Actor, self).getOriginX())

    @override
    @overload
    def remove(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.remove()"""
        return bool.__wrap(super(Actor, self).remove())

    @override
    @overload
    def setY(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setY(float,int)"""
        super(__Actor, self).setY(__float.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def removeActorAt(self, arg0: int, arg1: bool) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Group.removeActorAt(int,boolean)"""
        return 'Actor'.__wrap(super(__Group, self).removeActorAt(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setPosition(float,float,int)"""
        super(__Actor, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setName(java.lang.String)"""
        super(__Actor, self).setName(arg0)

    @override
    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__Actor, self).addAction(arg0)

    @override
    @overload
    def isTouchable(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchable()"""
        return bool.__wrap(super(Actor, self).isTouchable())

    @override
    @overload
    def getListeners(self) -> 'utils.DelayedRemovalArray':
        """public com.badlogic.gdx.utils.DelayedRemovalArray<com.badlogic.gdx.scenes.scene2d.EventListener> com.badlogic.gdx.scenes.scene2d.Actor.getListeners()"""
        return 'utils.DelayedRemovalArray'.__wrap(super(Actor, self).getListeners())

    @overload
    def firstAscendant(self, arg0: 'Class') -> 'Actor':
        """public <T extends com.badlogic.gdx.scenes.scene2d.Actor> T com.badlogic.gdx.scenes.scene2d.Actor.firstAscendant(java.lang.Class<T>)"""
        return 'Actor'.__wrap(super(__Actor, self).firstAscendant(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getScaleX()"""
        return float.__wrap(super(Actor, self).getScaleX())

    @override
    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScaleY(float)"""
        super(__Actor, self).setScaleY(__float.valueOf(arg0))

    @override
    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOriginY(float)"""
        super(__Actor, self).setOriginY(__float.valueOf(arg0))

    @overload
    def localToActorCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToActorCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToActorCoordinates(arg0, arg1))

    @overload
    def localToAscendantCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToAscendantCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToAscendantCoordinates(arg0, arg1))

    @override
    @overload
    def hasKeyboardFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasKeyboardFocus()"""
        return bool.__wrap(super(Actor, self).hasKeyboardFocus())

    @override
    @overload
    def hasScrollFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasScrollFocus()"""
        return bool.__wrap(super(Actor, self).hasScrollFocus())

    @override
    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScale(float,float)"""
        super(__Actor, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getTop(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getTop()"""
        return float.__wrap(super(Actor, self).getTop())

    @override
    @overload
    def clipBegin(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.clipBegin()"""
        return bool.__wrap(super(Actor, self).clipBegin())

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Actor, self).setColor(arg0)

    @override
    @overload
    def act(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Group.act(float)"""
        super(__Group, self).act(__float.valueOf(arg0))

    @overload
    def debugAll(self) -> 'Group':
        """public com.badlogic.gdx.scenes.scene2d.Group com.badlogic.gdx.scenes.scene2d.Group.debugAll()"""
        return 'Group'.__wrap(super(Group, self).debugAll())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Group()"""
        val = __Group()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def localToStageCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToStageCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToStageCoordinates(arg0))

    @override
    @overload
    def setDebug(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setDebug(boolean)"""
        super(__Actor, self).setDebug(__boolean.valueOf(arg0))

    @override
    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getHeight()"""
        return float.__wrap(super(Actor, self).getHeight())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def removeCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.removeCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Actor, self).removeCaptureListener(arg0))

    @override
    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setY(float)"""
        super(__Actor, self).setY(__float.valueOf(arg0))

    @override
    @overload
    def getStage(self) -> 'Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Actor.getStage()"""
        return 'Stage'.__wrap(super(Actor, self).getStage())

    @overload
    def screenToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.screenToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).screenToLocalCoordinates(arg0))

    @override
    @overload
    def getParent(self) -> 'Group':
        """public com.badlogic.gdx.scenes.scene2d.Group com.badlogic.gdx.scenes.scene2d.Actor.getParent()"""
        return 'Group'.__wrap(super(Actor, self).getParent())

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Group.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__Group, self).draw(arg0, __float.valueOf(arg1))

    @override
    @overload
    def toFront(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.toFront()"""
        super(Actor, self).toFront()

    @override
    @overload
    def setX(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setX(float,int)"""
        super(__Actor, self).setX(__float.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.addListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Actor, self).addListener(arg0))

    @overload
    def addActorBefore(self, arg0: 'Actor', arg1: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.addActorBefore(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Group, self).addActorBefore(arg0, arg1)

    @override
    @overload
    def isTouchFocusTarget(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchFocusTarget()"""
        return bool.__wrap(super(Actor, self).isTouchFocusTarget())

    @overload
    def localToDescendantCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Group.localToDescendantCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Group, self).localToDescendantCoordinates(arg0, arg1))

    @overload
    def clearChildren(self):
        """public void com.badlogic.gdx.scenes.scene2d.Group.clearChildren()"""
        super(Group, self).clearChildren()

    @overload
    def findActor(self, arg0: str) -> 'Actor':
        """public <T extends com.badlogic.gdx.scenes.scene2d.Actor> T com.badlogic.gdx.scenes.scene2d.Group.findActor(java.lang.String)"""
        return 'Actor'.__wrap(super(__Group, self).findActor(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Actor.getName()"""
        return str.__wrap(super(Actor, self).getName())

    @overload
    def isDescendantOf(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isDescendantOf(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool.__wrap(super(__Actor, self).isDescendantOf(arg0))

    @overload
    def swapActor(self, arg0: 'Actor', arg1: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.swapActor(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool.__wrap(super(__Group, self).swapActor(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Group.toString()"""
        return str.__wrap(super(Group, self).toString())

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setPosition(float,float)"""
        super(__Actor, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def localToScreenCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToScreenCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToScreenCoordinates(arg0))

    @override
    @overload
    def toBack(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.toBack()"""
        super(Actor, self).toBack()

    @override
    @overload
    def sizeBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.sizeBy(float)"""
        super(__Actor, self).sizeBy(__float.valueOf(arg0))

    @overload
    def localToParentCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToParentCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToParentCoordinates(arg0))

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setX(float)"""
        super(__Actor, self).setX(__float.valueOf(arg0))

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getOriginY()"""
        return float.__wrap(super(Actor, self).getOriginY())

    @override
    @overload
    def setOrigin(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOrigin(int)"""
        super(__Actor, self).setOrigin(__int.valueOf(arg0))

    @override
    @overload
    def rotateBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.rotateBy(float)"""
        super(__Actor, self).rotateBy(__float.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setBounds(float,float,float,float)"""
        super(__Actor, self).setBounds(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def removeListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Actor, self).removeListener(arg0))

    @override
    @overload
    def getRight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getRight()"""
        return float.__wrap(super(Actor, self).getRight())

    @override
    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clearListeners()"""
        super(Actor, self).clearListeners()

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getScaleY()"""
        return float.__wrap(super(Actor, self).getScaleY())

    @overload
    def setZIndex(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.setZIndex(int)"""
        return bool.__wrap(super(__Actor, self).setZIndex(__int.valueOf(arg0)))

    @override
    @overload
    def setTouchable(self, arg0: 'Touchable'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setTouchable(com.badlogic.gdx.scenes.scene2d.Touchable)"""
        super(__Actor, self).setTouchable(arg0)

    @override
    @overload
    def hasActions(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasActions()"""
        return bool.__wrap(super(Actor, self).hasActions())

    @override
    @overload
    def clearActions(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clearActions()"""
        super(Actor, self).clearActions()

    @overload
    def parentToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.parentToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).parentToLocalCoordinates(arg0))

    @override
    @overload
    def setCullingArea(self, arg0: 'Rectangle'):
        """public void com.badlogic.gdx.scenes.scene2d.Group.setCullingArea(com.badlogic.gdx.math.Rectangle)"""
        super(__Group, self).setCullingArea(arg0)

    @override
    @overload
    def moveBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.moveBy(float,float)"""
        super(__Actor, self).moveBy(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getY()"""
        return float.__wrap(super(Actor, self).getY())

    @overload
    def swapActor(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.swapActor(int,int)"""
        return bool.__wrap(super(__Group, self).swapActor(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def isAscendantOf(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isAscendantOf(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool.__wrap(super(__Actor, self).isAscendantOf(arg0))

    @override
    @overload
    def scaleBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.scaleBy(float)"""
        super(__Actor, self).scaleBy(__float.valueOf(arg0))

    @override
    @overload
    def hasParent(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasParent()"""
        return bool.__wrap(super(Actor, self).hasParent())

    @overload
    def removeActor(self, arg0: 'Actor', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.removeActor(com.badlogic.gdx.scenes.scene2d.Actor,boolean)"""
        return bool.__wrap(super(__Group, self).removeActor(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def clipBegin(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.clipBegin(float,float,float,float)"""
        return bool.__wrap(super(__Actor, self).clipBegin(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def removeActor(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Group.removeActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool.__wrap(super(__Group, self).removeActor(arg0))

    @override
    @overload
    def clipEnd(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clipEnd()"""
        super(Actor, self).clipEnd()

    @override
    @overload
    def setWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setWidth(float)"""
        super(__Actor, self).setWidth(__float.valueOf(arg0))

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getWidth()"""
        return float.__wrap(super(Actor, self).getWidth())

    @overload
    def getChildren(self) -> 'utils.SnapshotArray':
        """public com.badlogic.gdx.utils.SnapshotArray<com.badlogic.gdx.scenes.scene2d.Actor> com.badlogic.gdx.scenes.scene2d.Group.getChildren()"""
        return 'utils.SnapshotArray'.__wrap(super(Group, self).getChildren())

    @override
    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScaleX(float)"""
        super(__Actor, self).setScaleX(__float.valueOf(arg0))

    @override
    @overload
    def ancestorsVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.ancestorsVisible()"""
        return bool.__wrap(super(Actor, self).ancestorsVisible()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Touchable
import com.badlogic.gdx.scenes.scene2d.Touchable as __Touchable
__Touchable = __Touchable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Touchable():
    """com.badlogic.gdx.scenes.scene2d.Touchable"""
 
    @staticmethod
    def __wrap(java_value: __Touchable) -> 'Touchable':
        return Touchable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Touchable):
        """
        Dynamic initializer for Touchable.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['Touchable']:
        """public static com.badlogic.gdx.scenes.scene2d.Touchable[] com.badlogic.gdx.scenes.scene2d.Touchable.values()"""
        return List[Touchable].__wrap(__Touchable.values())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Touchable':
        """public static com.badlogic.gdx.scenes.scene2d.Touchable com.badlogic.gdx.scenes.scene2d.Touchable.valueOf(java.lang.String)"""
        return Touchable.__wrap(__Touchable.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Stage
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Character as __char
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.scenes.scene2d.Group as __Group
__Group = __Group
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
try:
    from pygdx.utils import viewport
except ImportError:
    viewport = __import_once__("pygdx.utils.viewport")

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
import java.lang.Object as __object
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.viewport.Viewport as __Viewport
__Viewport = __Viewport
try:
    from pygdx.scenes.scene2d import ui
except ImportError:
    ui = __import_once__("pygdx.scenes.scene2d.ui")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import com.badlogic.gdx.scenes.scene2d.Stage as __Stage
__Stage = __Stage
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class Stage():
    """com.badlogic.gdx.scenes.scene2d.Stage"""
 
    @staticmethod
    def __wrap(java_value: __Stage) -> 'Stage':
        return Stage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Stage):
        """
        Dynamic initializer for Stage.
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
    def getViewport(self) -> 'viewport.Viewport':
        """public com.badlogic.gdx.utils.viewport.Viewport com.badlogic.gdx.scenes.scene2d.Stage.getViewport()"""
        return 'viewport.Viewport'.__wrap(super(Stage, self).getViewport())

    @overload
    def getActors(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Actor> com.badlogic.gdx.scenes.scene2d.Stage.getActors()"""
        return 'utils.Array'.__wrap(super(Stage, self).getActors())

    @overload
    def hit(self, arg0: float, arg1: float, arg2: bool) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Stage.hit(float,float,boolean)"""
        return 'Actor'.__wrap(super(__Stage, self).hit(__float.valueOf(arg0), __float.valueOf(arg1), __boolean.valueOf(arg2)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Stage()"""
        val = __Stage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDebugColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.Stage.getDebugColor()"""
        return 'graphics.Color'.__wrap(super(Stage, self).getDebugColor())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRoot(self) -> 'Group':
        """public com.badlogic.gdx.scenes.scene2d.Group com.badlogic.gdx.scenes.scene2d.Stage.getRoot()"""
        return 'Group'.__wrap(super(Stage, self).getRoot())

    @overload
    def addCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.addCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Stage, self).addCaptureListener(arg0))

    @overload
    def cancelTouchFocusExcept(self, arg0: 'EventListener', arg1: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.cancelTouchFocusExcept(com.badlogic.gdx.scenes.scene2d.EventListener,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Stage, self).cancelTouchFocusExcept(arg0, arg1)

    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.clear()"""
        super(Stage, self).clear()

    @overload
    def setScrollFocus(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.setScrollFocus(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool.__wrap(super(__Stage, self).setScrollFocus(arg0))

    @overload
    def touchUp(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.touchUp(int,int,int,int)"""
        return bool.__wrap(super(__Stage, self).touchUp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def setDebugTableUnderMouse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugTableUnderMouse(boolean)"""
        super(__Stage, self).setDebugTableUnderMouse(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def unfocusAll(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.unfocusAll()"""
        super(Stage, self).unfocusAll()

    @overload
    def setDebugParentUnderMouse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugParentUnderMouse(boolean)"""
        super(__Stage, self).setDebugParentUnderMouse(__boolean.valueOf(arg0))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Stage.getHeight()"""
        return float.__wrap(super(Stage, self).getHeight())

    @overload
    def getScrollFocus(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Stage.getScrollFocus()"""
        return 'Actor'.__wrap(super(Stage, self).getScrollFocus())

    @overload
    def setActionsRequestRendering(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setActionsRequestRendering(boolean)"""
        super(__Stage, self).setActionsRequestRendering(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setDebugInvisible(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugInvisible(boolean)"""
        super(__Stage, self).setDebugInvisible(__boolean.valueOf(arg0))

    @overload
    def setDebugAll(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugAll(boolean)"""
        super(__Stage, self).setDebugAll(__boolean.valueOf(arg0))

    @overload
    def keyTyped(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.keyTyped(char)"""
        return bool.__wrap(super(__Stage, self).keyTyped(__char.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def mouseMoved(self, arg0: int, arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.mouseMoved(int,int)"""
        return bool.__wrap(super(__Stage, self).mouseMoved(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def cancelTouchFocus(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.cancelTouchFocus(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Stage, self).cancelTouchFocus(arg0)

    @overload
    def calculateScissors(self, arg0: 'Rectangle', arg1: 'Rectangle'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.calculateScissors(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        super(__Stage, self).calculateScissors(arg0, arg1)

    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__Stage, self).addAction(arg0)

    @overload
    def setRoot(self, arg0: 'Group'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setRoot(com.badlogic.gdx.scenes.scene2d.Group)"""
        super(__Stage, self).setRoot(arg0)

    @overload
    def setViewport(self, arg0: 'Viewport'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setViewport(com.badlogic.gdx.utils.viewport.Viewport)"""
        super(__Stage, self).setViewport(arg0)

    @overload
    def screenToStageCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Stage.screenToStageCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Stage, self).screenToStageCoordinates(arg0))

    @overload
    def touchCancelled(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.touchCancelled(int,int,int,int)"""
        return bool.__wrap(super(__Stage, self).touchCancelled(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def act(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.act(float)"""
        super(__Stage, self).act(__float.valueOf(arg0))

    @overload
    def touchDown(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.touchDown(int,int,int,int)"""
        return bool.__wrap(super(__Stage, self).touchDown(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def unfocus(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.unfocus(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Stage, self).unfocus(arg0)

    @overload
    def setKeyboardFocus(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.setKeyboardFocus(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool.__wrap(super(__Stage, self).setKeyboardFocus(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def scrolled(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.scrolled(float,float)"""
        return bool.__wrap(super(__Stage, self).scrolled(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.scenes.scene2d.Stage.getCamera()"""
        return 'graphics.Camera'.__wrap(super(Stage, self).getCamera())

    @overload
    def setDebugUnderMouse(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugUnderMouse(boolean)"""
        super(__Stage, self).setDebugUnderMouse(__boolean.valueOf(arg0))

    @overload
    def act(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.act()"""
        super(Stage, self).act()

    @overload
    def cancelTouchFocus(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.cancelTouchFocus()"""
        super(Stage, self).cancelTouchFocus()

    @overload
    def setDebugTableUnderMouse(self, arg0: 'Debug'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.setDebugTableUnderMouse(com.badlogic.gdx.scenes.scene2d.ui.Table$Debug)"""
        super(__Stage, self).setDebugTableUnderMouse(arg0)

    @overload
    def addListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.addListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Stage, self).addListener(arg0))

    @overload
    def keyDown(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.keyDown(int)"""
        return bool.__wrap(super(__Stage, self).keyDown(__int.valueOf(arg0)))

    @overload
    def draw(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.draw()"""
        super(Stage, self).draw()

    @overload
    def __init__(self, arg0: 'Viewport', arg1: 'Batch'):
        """public com.badlogic.gdx.scenes.scene2d.Stage(com.badlogic.gdx.utils.viewport.Viewport,com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __Stage(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Viewport'):
        """public com.badlogic.gdx.scenes.scene2d.Stage(com.badlogic.gdx.utils.viewport.Viewport)"""
        val = __Stage(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeTouchFocus(self, arg0: 'EventListener', arg1: 'Actor', arg2: 'Actor', arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.removeTouchFocus(com.badlogic.gdx.scenes.scene2d.EventListener,com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor,int,int)"""
        super(__Stage, self).removeTouchFocus(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def getActionsRequestRendering(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.getActionsRequestRendering()"""
        return bool.__wrap(super(Stage, self).getActionsRequestRendering())

    @overload
    def stageToScreenCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Stage.stageToScreenCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Stage, self).stageToScreenCoordinates(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def addTouchFocus(self, arg0: 'EventListener', arg1: 'Actor', arg2: 'Actor', arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.addTouchFocus(com.badlogic.gdx.scenes.scene2d.EventListener,com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.scenes.scene2d.Actor,int,int)"""
        super(__Stage, self).addTouchFocus(arg0, arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.dispose()"""
        super(Stage, self).dispose()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Stage()"""
        val = __Stage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isDebugAll(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.isDebugAll()"""
        return bool.__wrap(super(Stage, self).isDebugAll())

    @overload
    def keyUp(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.keyUp(int)"""
        return bool.__wrap(super(__Stage, self).keyUp(__int.valueOf(arg0)))

    @overload
    def removeListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Stage, self).removeListener(arg0))

    @overload
    def touchDragged(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.touchDragged(int,int,int)"""
        return bool.__wrap(super(__Stage, self).touchDragged(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getKeyboardFocus(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Stage.getKeyboardFocus()"""
        return 'Actor'.__wrap(super(Stage, self).getKeyboardFocus())

    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch com.badlogic.gdx.scenes.scene2d.Stage.getBatch()"""
        return 'g2d.Batch'.__wrap(super(Stage, self).getBatch())

    @overload
    def removeCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Stage.removeCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Stage, self).removeCaptureListener(arg0))

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
    def toScreenCoordinates(self, arg0: 'Vector2', arg1: 'Matrix4') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Stage.toScreenCoordinates(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Matrix4)"""
        return 'math.Vector2'.__wrap(super(__Stage, self).toScreenCoordinates(arg0, arg1))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Stage.getWidth()"""
        return float.__wrap(super(Stage, self).getWidth())

    @overload
    def addActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Stage.addActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Stage, self).addActor(arg0) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.InputEvent
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.InputEvent as __InputEvent
__InputEvent = __InputEvent
from builtins import float
import com.badlogic.gdx.scenes.scene2d.Event as __Event
__Event = __Event
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.InputEvent as __InputEvent_Type
__Type = __InputEvent_Type.Type
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import com.badlogic.gdx.scenes.scene2d.Stage as __Stage
__Stage = __Stage
from builtins import bool
from builtins import int
 
class InputEvent():
    """com.badlogic.gdx.scenes.scene2d.InputEvent"""
 
    @staticmethod
    def __wrap(java_value: __InputEvent) -> 'InputEvent':
        return InputEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InputEvent):
        """
        Dynamic initializer for InputEvent.
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
    def getScrollAmountY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.InputEvent.getScrollAmountY()"""
        return float.__wrap(super(InputEvent, self).getScrollAmountY())

    @overload
    def setKeyCode(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setKeyCode(int)"""
        super(__InputEvent, self).setKeyCode(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setButton(int)"""
        super(__InputEvent, self).setButton(__int.valueOf(arg0))

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCancelled()"""
        return bool.__wrap(super(Event, self).isCancelled())

    @overload
    def setType(self, arg0: 'Type'):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setType(com.badlogic.gdx.scenes.scene2d.InputEvent$Type)"""
        super(__InputEvent, self).setType(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTouchFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputEvent.getTouchFocus()"""
        return bool.__wrap(super(InputEvent, self).getTouchFocus())

    @overload
    def setCharacter(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setCharacter(char)"""
        super(__InputEvent, self).setCharacter(__char.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setStage(self, arg0: 'Stage'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setStage(com.badlogic.gdx.scenes.scene2d.Stage)"""
        super(__Event, self).setStage(arg0)

    @overload
    def toCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.InputEvent.toCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__InputEvent, self).toCoordinates(arg0, arg1))

    @overload
    def getStageX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.InputEvent.getStageX()"""
        return float.__wrap(super(InputEvent, self).getStageX())

    @overload
    def setStageX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setStageX(float)"""
        super(__InputEvent, self).setStageX(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.InputEvent.toString()"""
        return str.__wrap(super(InputEvent, self).toString())

    @override
    @overload
    def isHandled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isHandled()"""
        return bool.__wrap(super(Event, self).isHandled())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setStageY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setStageY(float)"""
        super(__InputEvent, self).setStageY(__float.valueOf(arg0))

    @overload
    def setScrollAmountY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setScrollAmountY(float)"""
        super(__InputEvent, self).setScrollAmountY(__float.valueOf(arg0))

    @overload
    def getScrollAmountX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.InputEvent.getScrollAmountX()"""
        return float.__wrap(super(InputEvent, self).getScrollAmountX())

    @overload
    def isTouchFocusCancel(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputEvent.isTouchFocusCancel()"""
        return bool.__wrap(super(InputEvent, self).isTouchFocusCancel())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.InputEvent()"""
        val = __InputEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setRelatedActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setRelatedActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__InputEvent, self).setRelatedActor(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.reset()"""
        super(InputEvent, self).reset()

    @overload
    def getRelatedActor(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.InputEvent.getRelatedActor()"""
        return 'Actor'.__wrap(super(InputEvent, self).getRelatedActor())

    @override
    @overload
    def isStopped(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isStopped()"""
        return bool.__wrap(super(Event, self).isStopped())

    @override
    @overload
    def setBubbles(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setBubbles(boolean)"""
        super(__Event, self).setBubbles(__boolean.valueOf(arg0))

    @override
    @overload
    def getTarget(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getTarget()"""
        return 'Actor'.__wrap(super(Event, self).getTarget())

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Event, self).setTarget(arg0)

    @override
    @overload
    def getListenerActor(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getListenerActor()"""
        return 'Actor'.__wrap(super(Event, self).getListenerActor())

    @overload
    def getStageY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.InputEvent.getStageY()"""
        return float.__wrap(super(InputEvent, self).getStageY())

    @override
    @overload
    def getStage(self) -> 'Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Event.getStage()"""
        return 'Stage'.__wrap(super(Event, self).getStage())

    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.scenes.scene2d.InputEvent$Type com.badlogic.gdx.scenes.scene2d.InputEvent.getType()"""
        return 'Type'.__wrap(super(InputEvent, self).getType())

    @overload
    def setScrollAmountX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setScrollAmountX(float)"""
        super(__InputEvent, self).setScrollAmountX(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
    def getBubbles(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.getBubbles()"""
        return bool.__wrap(super(Event, self).getBubbles())

    @override
    @overload
    def handle(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.handle()"""
        super(Event, self).handle()

    @overload
    def setPointer(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setPointer(int)"""
        super(__InputEvent, self).setPointer(__int.valueOf(arg0))

    @override
    @overload
    def setListenerActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setListenerActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Event, self).setListenerActor(arg0)

    @overload
    def setTouchFocus(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.InputEvent.setTouchFocus(boolean)"""
        super(__InputEvent, self).setTouchFocus(__boolean.valueOf(arg0))

    @overload
    def getCharacter(self) -> str:
        """public char com.badlogic.gdx.scenes.scene2d.InputEvent.getCharacter()"""
        return str.__wrap(super(InputEvent, self).getCharacter())

    @overload
    def getPointer(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.InputEvent.getPointer()"""
        return int.__wrap(super(InputEvent, self).getPointer())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.InputEvent()"""
        val = __InputEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.InputEvent.getButton()"""
        return int.__wrap(super(InputEvent, self).getButton())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setCapture(boolean)"""
        super(__Event, self).setCapture(__boolean.valueOf(arg0))

    @override
    @overload
    def isCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCapture()"""
        return bool.__wrap(super(Event, self).isCapture())

    @overload
    def getKeyCode(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.InputEvent.getKeyCode()"""
        return int.__wrap(super(InputEvent, self).getKeyCode()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.EventListener
import com.badlogic.gdx.scenes.scene2d.EventListener as __EventListener
__EventListener = __EventListener
from abc import abstractmethod, ABC
 
class EventListener(ABC):
    """com.badlogic.gdx.scenes.scene2d.EventListener"""
 
    @staticmethod
    def __wrap(java_value: __EventListener) -> 'EventListener':
        return EventListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventListener):
        """
        Dynamic initializer for EventListener.
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
    def handle(self, arg0: 'Event'):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.EventListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.InputListener
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.InputListener as __InputListener
__InputListener = __InputListener
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InputListener():
    """com.badlogic.gdx.scenes.scene2d.InputListener"""
 
    @staticmethod
    def __wrap(java_value: __InputListener) -> 'InputListener':
        return InputListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InputListener):
        """
        Dynamic initializer for InputListener.
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
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool.__wrap(super(__InputListener, self).scrolled(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool.__wrap(super(__InputListener, self).mouseMoved(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool.__wrap(super(__InputListener, self).handle(arg0))

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
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__InputListener, self).enter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__InputListener, self).exit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool.__wrap(super(__InputListener, self).keyTyped(arg0, __char.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.InputListener()"""
        val = __InputListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool.__wrap(super(__InputListener, self).keyUp(arg0, __int.valueOf(arg1)))

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool.__wrap(super(__InputListener, self).touchDown(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(__InputListener, self).touchUp(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__InputListener, self).touchDragged(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool.__wrap(super(__InputListener, self).keyDown(arg0, __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.InputListener()"""
        val = __InputListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Stage$TouchFocus
import com.badlogic.gdx.scenes.scene2d.Stage as __Stage_TouchFocus
__TouchFocus = __Stage_TouchFocus.TouchFocus
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TouchFocus():
    """com.badlogic.gdx.scenes.scene2d.Stage.TouchFocus"""
 
    @staticmethod
    def __wrap(java_value: __TouchFocus) -> 'TouchFocus':
        return TouchFocus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TouchFocus):
        """
        Dynamic initializer for TouchFocus.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Stage$TouchFocus()"""
        val = __TouchFocus()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Stage$TouchFocus()"""
        val = __TouchFocus()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Stage$TouchFocus.reset()"""
        super(TouchFocus, self).reset() 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.Actor
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.scenes.scene2d.Touchable as __Touchable
__Touchable = __Touchable
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.scenes.scene2d.Group as __Group
__Group = __Group
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
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
import java.lang.Object as __object
from builtins import float
from builtins import object
import com.badlogic.gdx.utils.DelayedRemovalArray as __DelayedRemovalArray
__DelayedRemovalArray = __DelayedRemovalArray
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
import com.badlogic.gdx.scenes.scene2d.Stage as __Stage
__Stage = __Stage
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class Actor():
    """com.badlogic.gdx.scenes.scene2d.Actor"""
 
    @staticmethod
    def __wrap(java_value: __Actor) -> 'Actor':
        return Actor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Actor):
        """
        Dynamic initializer for Actor.
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
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getRotation()"""
        return float.__wrap(super(Actor, self).getRotation())

    @overload
    def setUserObject(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setUserObject(java.lang.Object)"""
        super(__Actor, self).setUserObject(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Actor.toString()"""
        return str.__wrap(super(Actor, self).toString())

    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScaleX(float)"""
        super(__Actor, self).setScaleX(__float.valueOf(arg0))

    @overload
    def setOriginY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOriginY(float)"""
        super(__Actor, self).setOriginY(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def fire(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.fire(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool.__wrap(super(__Actor, self).fire(arg0))

    @overload
    def clipEnd(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clipEnd()"""
        super(Actor, self).clipEnd()

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScale(float)"""
        super(__Actor, self).setScale(__float.valueOf(arg0))

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOrigin(float,float)"""
        super(__Actor, self).setOrigin(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def stageToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.stageToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).stageToLocalCoordinates(arg0))

    @overload
    def addCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.addCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Actor, self).addCaptureListener(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getStage(self) -> 'Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Actor.getStage()"""
        return 'Stage'.__wrap(super(Actor, self).getStage())

    @overload
    def getY(self, arg0: int) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getY(int)"""
        return float.__wrap(super(__Actor, self).getY(__int.valueOf(arg0)))

    @overload
    def setX(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setX(float,int)"""
        super(__Actor, self).setX(__float.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setVisible(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setVisible(boolean)"""
        super(__Actor, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def setY(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setY(float,int)"""
        super(__Actor, self).setY(__float.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def hasKeyboardFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasKeyboardFocus()"""
        return bool.__wrap(super(Actor, self).hasKeyboardFocus())

    @overload
    def notify(self, arg0: 'Event', arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.notify(com.badlogic.gdx.scenes.scene2d.Event,boolean)"""
        return bool.__wrap(super(__Actor, self).notify(arg0, __boolean.valueOf(arg1)))

    @overload
    def sizeBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.sizeBy(float)"""
        super(__Actor, self).sizeBy(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def hit(self, arg0: float, arg1: float, arg2: bool) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Actor.hit(float,float,boolean)"""
        return 'Actor'.__wrap(super(__Actor, self).hit(__float.valueOf(arg0), __float.valueOf(arg1), __boolean.valueOf(arg2)))

    @overload
    def getActions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.scenes.scene2d.Action> com.badlogic.gdx.scenes.scene2d.Actor.getActions()"""
        return 'utils.Array'.__wrap(super(Actor, self).getActions())

    @overload
    def getRight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getRight()"""
        return float.__wrap(super(Actor, self).getRight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def hasActions(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasActions()"""
        return bool.__wrap(super(Actor, self).hasActions())

    @overload
    def isTouchFocusTarget(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchFocusTarget()"""
        return bool.__wrap(super(Actor, self).isTouchFocusTarget())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getY()"""
        return float.__wrap(super(Actor, self).getY())

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getScaleX()"""
        return float.__wrap(super(Actor, self).getScaleX())

    @overload
    def getX(self, arg0: int) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getX(int)"""
        return float.__wrap(super(__Actor, self).getX(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getCaptureListeners(self) -> 'utils.DelayedRemovalArray':
        """public com.badlogic.gdx.utils.DelayedRemovalArray<com.badlogic.gdx.scenes.scene2d.EventListener> com.badlogic.gdx.scenes.scene2d.Actor.getCaptureListeners()"""
        return 'utils.DelayedRemovalArray'.__wrap(super(Actor, self).getCaptureListeners())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getX()"""
        return float.__wrap(super(Actor, self).getX())

    @overload
    def moveBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.moveBy(float,float)"""
        super(__Actor, self).moveBy(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScale(float,float)"""
        super(__Actor, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def clipBegin(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.clipBegin()"""
        return bool.__wrap(super(Actor, self).clipBegin())

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getWidth()"""
        return float.__wrap(super(Actor, self).getWidth())

    @overload
    def firstAscendant(self, arg0: 'Class') -> 'Actor':
        """public <T extends com.badlogic.gdx.scenes.scene2d.Actor> T com.badlogic.gdx.scenes.scene2d.Actor.firstAscendant(java.lang.Class<T>)"""
        return 'Actor'.__wrap(super(__Actor, self).firstAscendant(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getOriginY()"""
        return float.__wrap(super(Actor, self).getOriginY())

    @overload
    def localToActorCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToActorCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToActorCoordinates(arg0, arg1))

    @overload
    def localToAscendantCoordinates(self, arg0: 'Actor', arg1: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToAscendantCoordinates(com.badlogic.gdx.scenes.scene2d.Actor,com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToAscendantCoordinates(arg0, arg1))

    @overload
    def getZIndex(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.Actor.getZIndex()"""
        return int.__wrap(super(Actor, self).getZIndex())

    @overload
    def getListeners(self) -> 'utils.DelayedRemovalArray':
        """public com.badlogic.gdx.utils.DelayedRemovalArray<com.badlogic.gdx.scenes.scene2d.EventListener> com.badlogic.gdx.scenes.scene2d.Actor.getListeners()"""
        return 'utils.DelayedRemovalArray'.__wrap(super(Actor, self).getListeners())

    @overload
    def isVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isVisible()"""
        return bool.__wrap(super(Actor, self).isVisible())

    @overload
    def ascendantsVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.ascendantsVisible()"""
        return bool.__wrap(super(Actor, self).ascendantsVisible())

    @overload
    def toBack(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.toBack()"""
        super(Actor, self).toBack()

    @overload
    def debug(self) -> 'Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Actor.debug()"""
        return 'Actor'.__wrap(super(Actor, self).debug())

    @overload
    def localToStageCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToStageCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToStageCoordinates(arg0))

    @overload
    def drawDebug(self, arg0: 'ShapeRenderer'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.drawDebug(com.badlogic.gdx.graphics.glutils.ShapeRenderer)"""
        super(__Actor, self).drawDebug(arg0)

    @overload
    def setTouchable(self, arg0: 'Touchable'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setTouchable(com.badlogic.gdx.scenes.scene2d.Touchable)"""
        super(__Actor, self).setTouchable(arg0)

    @overload
    def sizeBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.sizeBy(float,float)"""
        super(__Actor, self).sizeBy(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def toFront(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.toFront()"""
        super(Actor, self).toFront()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Actor, self).setColor(arg0)

    @overload
    def removeCaptureListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.removeCaptureListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Actor, self).removeCaptureListener(arg0))

    @overload
    def screenToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.screenToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).screenToLocalCoordinates(arg0))

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setPosition(float,float,int)"""
        super(__Actor, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def getDebug(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.getDebug()"""
        return bool.__wrap(super(Actor, self).getDebug())

    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clearListeners()"""
        super(Actor, self).clearListeners()

    @overload
    def addListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.addListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Actor, self).addListener(arg0))

    @overload
    def addAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.addAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__Actor, self).addAction(arg0)

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setPosition(float,float)"""
        super(__Actor, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.Actor()"""
        val = __Actor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.Actor()"""
        val = __Actor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setBounds(float,float,float,float)"""
        super(__Actor, self).setBounds(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def isTouchFocusListener(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchFocusListener()"""
        return bool.__wrap(super(Actor, self).isTouchFocusListener())

    @overload
    def hasParent(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasParent()"""
        return bool.__wrap(super(Actor, self).hasParent())

    @overload
    def isDescendantOf(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isDescendantOf(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool.__wrap(super(__Actor, self).isDescendantOf(arg0))

    @overload
    def clearActions(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clearActions()"""
        super(Actor, self).clearActions()

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setX(float)"""
        super(__Actor, self).setX(__float.valueOf(arg0))

    @overload
    def ancestorsVisible(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.ancestorsVisible()"""
        return bool.__wrap(super(Actor, self).ancestorsVisible())

    @overload
    def getParent(self) -> 'Group':
        """public com.badlogic.gdx.scenes.scene2d.Group com.badlogic.gdx.scenes.scene2d.Actor.getParent()"""
        return 'Group'.__wrap(super(Actor, self).getParent())

    @overload
    def setDebug(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setDebug(boolean)"""
        super(__Actor, self).setDebug(__boolean.valueOf(arg0))

    @overload
    def localToScreenCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToScreenCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToScreenCoordinates(arg0))

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getScaleY()"""
        return float.__wrap(super(Actor, self).getScaleY())

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getOriginX()"""
        return float.__wrap(super(Actor, self).getOriginX())

    @overload
    def setHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setHeight(float)"""
        super(__Actor, self).setHeight(__float.valueOf(arg0))

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setY(float)"""
        super(__Actor, self).setY(__float.valueOf(arg0))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.Actor.getColor()"""
        return 'graphics.Color'.__wrap(super(Actor, self).getColor())

    @overload
    def setOriginX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOriginX(float)"""
        super(__Actor, self).setOriginX(__float.valueOf(arg0))

    @overload
    def localToParentCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.localToParentCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).localToParentCoordinates(arg0))

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setName(java.lang.String)"""
        super(__Actor, self).setName(arg0)

    @overload
    def scaleBy(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.scaleBy(float,float)"""
        super(__Actor, self).scaleBy(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.clear()"""
        super(Actor, self).clear()

    @overload
    def setOrigin(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setOrigin(int)"""
        super(__Actor, self).setOrigin(__int.valueOf(arg0))

    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setSize(float,float)"""
        super(__Actor, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setRotation(float)"""
        super(__Actor, self).setRotation(__float.valueOf(arg0))

    @overload
    def removeListener(self, arg0: 'EventListener') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.removeListener(com.badlogic.gdx.scenes.scene2d.EventListener)"""
        return bool.__wrap(super(__Actor, self).removeListener(arg0))

    @overload
    def hasScrollFocus(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.hasScrollFocus()"""
        return bool.__wrap(super(Actor, self).hasScrollFocus())

    @overload
    def setZIndex(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.setZIndex(int)"""
        return bool.__wrap(super(__Actor, self).setZIndex(__int.valueOf(arg0)))

    @overload
    def getUserObject(self) -> object:
        """public java.lang.Object com.badlogic.gdx.scenes.scene2d.Actor.getUserObject()"""
        return object.__wrap(super(Actor, self).getUserObject())

    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setScaleY(float)"""
        super(__Actor, self).setScaleY(__float.valueOf(arg0))

    @overload
    def setWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setWidth(float)"""
        super(__Actor, self).setWidth(__float.valueOf(arg0))

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__Actor, self).draw(arg0, __float.valueOf(arg1))

    @overload
    def parentToLocalCoordinates(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.scenes.scene2d.Actor.parentToLocalCoordinates(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__Actor, self).parentToLocalCoordinates(arg0))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.setColor(float,float,float,float)"""
        super(__Actor, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.Actor.getName()"""
        return str.__wrap(super(Actor, self).getName())

    @overload
    def isAscendantOf(self, arg0: 'Actor') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isAscendantOf(com.badlogic.gdx.scenes.scene2d.Actor)"""
        return bool.__wrap(super(__Actor, self).isAscendantOf(arg0))

    @overload
    def isTouchable(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.isTouchable()"""
        return bool.__wrap(super(Actor, self).isTouchable())

    @overload
    def act(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.act(float)"""
        super(__Actor, self).act(__float.valueOf(arg0))

    @overload
    def scaleBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.scaleBy(float)"""
        super(__Actor, self).scaleBy(__float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getTop(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getTop()"""
        return float.__wrap(super(Actor, self).getTop())

    @overload
    def clipBegin(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.clipBegin(float,float,float,float)"""
        return bool.__wrap(super(__Actor, self).clipBegin(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.Actor.getHeight()"""
        return float.__wrap(super(Actor, self).getHeight())

    @overload
    def remove(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Actor.remove()"""
        return bool.__wrap(super(Actor, self).remove())

    @overload
    def getTouchable(self) -> 'Touchable':
        """public com.badlogic.gdx.scenes.scene2d.Touchable com.badlogic.gdx.scenes.scene2d.Actor.getTouchable()"""
        return 'Touchable'.__wrap(super(Actor, self).getTouchable())

    @overload
    def removeAction(self, arg0: 'Action'):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.removeAction(com.badlogic.gdx.scenes.scene2d.Action)"""
        super(__Actor, self).removeAction(arg0)

    @overload
    def rotateBy(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.Actor.rotateBy(float)"""
        super(__Actor, self).rotateBy(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.InputEvent$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.scenes.scene2d.InputEvent as __InputEvent_Type
__Type = __InputEvent_Type.Type
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Type():
    """com.badlogic.gdx.scenes.scene2d.InputEvent.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.gdx.scenes.scene2d.InputEvent$Type[] com.badlogic.gdx.scenes.scene2d.InputEvent$Type.values()"""
        return List[Type].__wrap(__Type.values())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.gdx.scenes.scene2d.InputEvent$Type com.badlogic.gdx.scenes.scene2d.InputEvent$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))
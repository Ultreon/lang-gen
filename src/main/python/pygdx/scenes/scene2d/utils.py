from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as __DragAndDrop_Source
__Source = __DragAndDrop_Source.Source
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Source(ABC):
    """com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.Source"""
 
    @staticmethod
    def __wrap(java_value: __Source) -> 'Source':
        return Source(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Source):
        """
        Dynamic initializer for Source.
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
    def dragStop(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Payload', arg5: 'Target'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.dragStop(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target)"""
        super(__Source, self).dragStop(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5)

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
    def __init__(self, arg0: 'Actor'):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source(com.badlogic.gdx.scenes.scene2d.Actor)"""
        val = __Source(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.getActor()"""
        return 'scene2d.Actor'.__wrap(super(Source, self).getActor())

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
    def drag(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.drag(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__Source, self).drag(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as __DragAndDrop_Source
__Source = __DragAndDrop_Source.Source
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Source(ABC):
    """com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.Source"""
 
    @staticmethod
    def __wrap(java_value: __Source) -> 'Source':
        return Source(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Source):
        """
        Dynamic initializer for Source.
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
    def dragStop(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Payload', arg5: 'Target'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.dragStop(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target)"""
        super(__Source, self).dragStop(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5)

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
    def __init__(self, arg0: 'Actor'):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source(com.badlogic.gdx.scenes.scene2d.Actor)"""
        val = __Source(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.getActor()"""
        return 'scene2d.Actor'.__wrap(super(Source, self).getActor())

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
    def drag(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source.drag(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__Source, self).drag(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ChangeListener
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener as __ChangeListener
__ChangeListener = __ChangeListener
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ChangeListener(ABC, scenes.__EventListener, scene2d.EventListener):
    """com.badlogic.gdx.scenes.scene2d.utils.ChangeListener"""
 
    @staticmethod
    def __wrap(java_value: __ChangeListener) -> 'ChangeListener':
        return ChangeListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChangeListener):
        """
        Dynamic initializer for ChangeListener.
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

    @abstractmethod
    def changed(self, arg0: 'ChangeEvent', arg1: 'Actor'):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.ChangeListener.changed(com.badlogic.gdx.scenes.scene2d.utils.ChangeListener$ChangeEvent,com.badlogic.gdx.scenes.scene2d.Actor)"""
        pass

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
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ChangeListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool.__wrap(super(__ChangeListener, self).handle(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ChangeListener()"""
        val = __ChangeListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.ChangeListener()"""
        val = __ChangeListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.FocusListener
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener as __FocusListener
__FocusListener = __FocusListener
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FocusListener(ABC, scenes.__EventListener, scene2d.EventListener):
    """com.badlogic.gdx.scenes.scene2d.utils.FocusListener"""
 
    @staticmethod
    def __wrap(java_value: __FocusListener) -> 'FocusListener':
        return FocusListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FocusListener):
        """
        Dynamic initializer for FocusListener.
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
    def keyboardFocusChanged(self, arg0: 'FocusEvent', arg1: 'Actor', arg2: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener.keyboardFocusChanged(com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent,com.badlogic.gdx.scenes.scene2d.Actor,boolean)"""
        super(__FocusListener, self).keyboardFocusChanged(arg0, arg1, __boolean.valueOf(arg2))

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.FocusListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool.__wrap(super(__FocusListener, self).handle(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener()"""
        val = __FocusListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener()"""
        val = __FocusListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def scrollFocusChanged(self, arg0: 'FocusEvent', arg1: 'Actor', arg2: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener.scrollFocusChanged(com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent,com.badlogic.gdx.scenes.scene2d.Actor,boolean)"""
        super(__FocusListener, self).scrollFocusChanged(arg0, arg1, __boolean.valueOf(arg2))

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ChangeListener$ChangeEvent
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

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
import com.badlogic.gdx.scenes.scene2d.utils.ChangeListener as __ChangeListener_ChangeEvent
__ChangeEvent = __ChangeListener_ChangeEvent.ChangeEvent
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
 
class ChangeEvent(scenes.__Event, scene2d.Event):
    """com.badlogic.gdx.scenes.scene2d.utils.ChangeListener.ChangeEvent"""
 
    @staticmethod
    def __wrap(java_value: __ChangeEvent) -> 'ChangeEvent':
        return ChangeEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChangeEvent):
        """
        Dynamic initializer for ChangeEvent.
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
        """public com.badlogic.gdx.scenes.scene2d.utils.ChangeListener$ChangeEvent()"""
        val = __ChangeEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ChangeListener$ChangeEvent()"""
        val = __ChangeEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setListenerActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setListenerActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Event, self).setListenerActor(arg0)

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCancelled()"""
        return bool.__wrap(super(scene2d.Event, self).isCancelled())

    @override
    @overload
    def getBubbles(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.getBubbles()"""
        return bool.__wrap(super(scene2d.Event, self).getBubbles())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getListenerActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getListenerActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Event, self).getListenerActor())

    @override
    @overload
    def isHandled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isHandled()"""
        return bool.__wrap(super(scene2d.Event, self).isHandled())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.reset()"""
        super(scene2d.Event, self).reset()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isStopped(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isStopped()"""
        return bool.__wrap(super(scene2d.Event, self).isStopped())

    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.stop()"""
        super(scene2d.Event, self).stop()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCapture()"""
        return bool.__wrap(super(scene2d.Event, self).isCapture())

    @override
    @overload
    def setStage(self, arg0: 'Stage'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setStage(com.badlogic.gdx.scenes.scene2d.Stage)"""
        super(__scene2d.Event, self).setStage(arg0)

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Event, self).setTarget(arg0)

    @override
    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setCapture(boolean)"""
        super(__scene2d.Event, self).setCapture(__boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.cancel()"""
        super(scene2d.Event, self).cancel()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Event, self).getTarget())

    @override
    @overload
    def getStage(self) -> 'scene2d.Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Event.getStage()"""
        return 'scene2d.Stage'.__wrap(super(scene2d.Event, self).getStage())

    @override
    @overload
    def setBubbles(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setBubbles(boolean)"""
        super(__scene2d.Event, self).setBubbles(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def handle(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.handle()"""
        super(scene2d.Event, self).handle() 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.UIUtils
import com.badlogic.gdx.scenes.scene2d.utils.UIUtils as __UIUtils
__UIUtils = __UIUtils
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
 
class UIUtils():
    """com.badlogic.gdx.scenes.scene2d.utils.UIUtils"""
 
    @staticmethod
    def __wrap(java_value: __UIUtils) -> 'UIUtils':
        return UIUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UIUtils):
        """
        Dynamic initializer for UIUtils.
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
    def shift() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.shift()"""
        return bool.__wrap(__UIUtils.shift())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def alt() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.alt()"""
        return bool.__wrap(__UIUtils.alt())

    @staticmethod
    @overload
    def ctrl() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.ctrl()"""
        return bool.__wrap(__UIUtils.ctrl())

    @staticmethod
    @overload
    def left(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.left(int)"""
        return bool.__wrap(__UIUtils.left(__int.valueOf(arg0)))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def left() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.left()"""
        return bool.__wrap(__UIUtils.left())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def right(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.right(int)"""
        return bool.__wrap(__UIUtils.right(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ctrl(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.ctrl(int)"""
        return bool.__wrap(__UIUtils.ctrl(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def shift(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.shift(int)"""
        return bool.__wrap(__UIUtils.shift(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def middle() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.middle()"""
        return bool.__wrap(__UIUtils.middle())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def alt(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.alt(int)"""
        return bool.__wrap(__UIUtils.alt(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def right() -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.right()"""
        return bool.__wrap(__UIUtils.right())

    @staticmethod
    @overload
    def middle(arg0: int) -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.UIUtils.middle(int)"""
        return bool.__wrap(__UIUtils.middle(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener as __FocusListener_FocusEvent_Type
__Type = __FocusListener_FocusEvent_Type.FocusEvent.Type
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
 
class Type(__Enum, Enum):
    """com.badlogic.gdx.scenes.scene2d.utils.FocusListener.FocusEvent.Type"""
 
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

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type[] com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type.values()"""
        return List[Type].__wrap(__Type.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Cullable
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.scenes.scene2d.utils.Cullable as __Cullable
__Cullable = __Cullable
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from abc import abstractmethod, ABC
 
class Cullable(ABC):
    """com.badlogic.gdx.scenes.scene2d.utils.Cullable"""
 
    @staticmethod
    def __wrap(java_value: __Cullable) -> 'Cullable':
        return Cullable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Cullable):
        """
        Dynamic initializer for Cullable.
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
    def setCullingArea(self, arg0: 'Rectangle'):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Cullable.setCullingArea(com.badlogic.gdx.math.Rectangle)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Layout
import com.badlogic.gdx.scenes.scene2d.utils.Layout as __Layout
__Layout = __Layout
from abc import abstractmethod, ABC
 
class Layout(ABC):
    """com.badlogic.gdx.scenes.scene2d.utils.Layout"""
 
    @staticmethod
    def __wrap(java_value: __Layout) -> 'Layout':
        return Layout(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Layout):
        """
        Dynamic initializer for Layout.
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as __BaseDrawable
__BaseDrawable = __BaseDrawable
from builtins import float
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable as __TextureRegionDrawable
__TextureRegionDrawable = __TextureRegionDrawable
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.scenes.scene2d.utils.Drawable as __Drawable
__Drawable = __Drawable
from builtins import bool
from builtins import int
 
class TextureRegionDrawable(__BaseDrawable, BaseDrawable, __TransformDrawable, TransformDrawable):
    """com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable"""
 
    @staticmethod
    def __wrap(java_value: __TextureRegionDrawable) -> 'TextureRegionDrawable':
        return TextureRegionDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureRegionDrawable):
        """
        Dynamic initializer for TextureRegionDrawable.
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
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(__BaseDrawable, self).setMinHeight(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable()"""
        val = __TextureRegionDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(__BaseDrawable, self).setBottomHeight(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __TextureRegionDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float.__wrap(super(BaseDrawable, self).getMinWidth())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(__BaseDrawable, self).setMinWidth(__float.valueOf(arg0))

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float.__wrap(super(BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float.__wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(__BaseDrawable, self).setName(arg0)

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
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(__BaseDrawable, self).setRightWidth(__float.valueOf(arg0))

    @overload
    def tint(self, arg0: 'Color') -> 'Drawable':
        """public com.badlogic.gdx.scenes.scene2d.utils.Drawable com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.tint(com.badlogic.gdx.graphics.Color)"""
        return 'Drawable'.__wrap(super(__TextureRegionDrawable, self).tint(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str.__wrap(super(BaseDrawable, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(__TextureRegionDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str.__wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(__BaseDrawable, self).setLeftWidth(__float.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable()"""
        val = __TextureRegionDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(__BaseDrawable, self).setTopHeight(__float.valueOf(arg0))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float.__wrap(super(BaseDrawable, self).getMinHeight())

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(__BaseDrawable, self).setMinSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(__BaseDrawable, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.getRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(TextureRegionDrawable, self).getRegion())

    @overload
    def __init__(self, arg0: 'TextureRegionDrawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable(com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable)"""
        val = __TextureRegionDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable(com.badlogic.gdx.graphics.Texture)"""
        val = __TextureRegionDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TextureRegionDrawable, self).setRegion(arg0)

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(__TextureRegionDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

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

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float.__wrap(super(BaseDrawable, self).getRightWidth())

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float.__wrap(super(BaseDrawable, self).getTopHeight()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as __DragAndDrop
__DragAndDrop = __DragAndDrop
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as __DragAndDrop_Source
__Source = __DragAndDrop_Source.Source
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as __DragAndDrop_Payload
__Payload = __DragAndDrop_Payload.Payload
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DragAndDrop():
    """com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop"""
 
    @staticmethod
    def __wrap(java_value: __DragAndDrop) -> 'DragAndDrop':
        return DragAndDrop(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DragAndDrop):
        """
        Dynamic initializer for DragAndDrop.
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
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setButton(int)"""
        super(__DragAndDrop, self).setButton(__int.valueOf(arg0))

    @overload
    def isDragValid(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.isDragValid()"""
        return bool.__wrap(super(DragAndDrop, self).isDragValid())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addTarget(self, arg0: 'Target'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.addTarget(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target)"""
        super(__DragAndDrop, self).addTarget(arg0)

    @overload
    def setDragTime(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setDragTime(int)"""
        super(__DragAndDrop, self).setDragTime(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setTapSquareSize(float)"""
        super(__DragAndDrop, self).setTapSquareSize(__float.valueOf(arg0))

    @overload
    def setCancelTouchFocus(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setCancelTouchFocus(boolean)"""
        super(__DragAndDrop, self).setCancelTouchFocus(__boolean.valueOf(arg0))

    @overload
    def setKeepWithinStage(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setKeepWithinStage(boolean)"""
        super(__DragAndDrop, self).setKeepWithinStage(__boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop()"""
        val = __DragAndDrop()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getDragPayload(self) -> 'Payload':
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.getDragPayload()"""
        return 'Payload'.__wrap(super(DragAndDrop, self).getDragPayload())

    @overload
    def setDragActorPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setDragActorPosition(float,float)"""
        super(__DragAndDrop, self).setDragActorPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def addSource(self, arg0: 'Source'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.addSource(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source)"""
        super(__DragAndDrop, self).addSource(arg0)

    @overload
    def setTouchOffset(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.setTouchOffset(float,float)"""
        super(__DragAndDrop, self).setTouchOffset(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def removeTarget(self, arg0: 'Target'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.removeTarget(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target)"""
        super(__DragAndDrop, self).removeTarget(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop()"""
        val = __DragAndDrop()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.clear()"""
        super(DragAndDrop, self).clear()

    @overload
    def removeSource(self, arg0: 'Source'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.removeSource(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source)"""
        super(__DragAndDrop, self).removeSource(arg0)

    @overload
    def cancelTouchFocusExcept(self, arg0: 'Source'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.cancelTouchFocusExcept(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source)"""
        super(__DragAndDrop, self).cancelTouchFocusExcept(arg0)

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
    def isDragging(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.isDragging()"""
        return bool.__wrap(super(DragAndDrop, self).isDragging())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDragTime(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.getDragTime()"""
        return int.__wrap(super(DragAndDrop, self).getDragTime())

    @overload
    def getDragSource(self) -> 'Source':
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.getDragSource()"""
        return 'Source'.__wrap(super(DragAndDrop, self).getDragSource())

    @overload
    def getDragActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.getDragActor()"""
        return 'scene2d.Actor'.__wrap(super(DragAndDrop, self).getDragActor()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Selection
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.utils.OrderedSet as __OrderedSet
__OrderedSet = __OrderedSet
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
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.Selection as __Selection
__Selection = __Selection
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Selection(__Disableable, Disableable, __Iterable, Iterable):
    """com.badlogic.gdx.scenes.scene2d.utils.Selection"""
 
    @staticmethod
    def __wrap(java_value: __Selection) -> 'Selection':
        return Selection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Selection):
        """
        Dynamic initializer for Selection.
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
        """public com.badlogic.gdx.scenes.scene2d.utils.Selection()"""
        val = __Selection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.contains(T)"""
        return bool.__wrap(super(__Selection, self).contains(arg0))

    @overload
    def setMultiple(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setMultiple(boolean)"""
        super(__Selection, self).setMultiple(__boolean.valueOf(arg0))

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.Selection.size()"""
        return int.__wrap(super(Selection, self).size())

    @overload
    def set(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.set(T)"""
        super(__Selection, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def fireChangeEvent(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.fireChangeEvent()"""
        return bool.__wrap(super(Selection, self).fireChangeEvent())

    @overload
    def setProgrammaticChangeEvents(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setProgrammaticChangeEvents(boolean)"""
        super(__Selection, self).setProgrammaticChangeEvents(__boolean.valueOf(arg0))

    @overload
    def addAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.addAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__Selection, self).addAll(arg0)

    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.add(T)"""
        super(__Selection, self).add(arg0)

    @overload
    def toArray(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.toArray()"""
        return 'utils.Array'.__wrap(super(Selection, self).toArray())

    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.notEmpty()"""
        return bool.__wrap(super(Selection, self).notEmpty())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.Selection()"""
        val = __Selection()
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
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.Selection.toString()"""
        return str.__wrap(super(Selection, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def removeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.removeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__Selection, self).removeAll(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def getMultiple(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getMultiple()"""
        return bool.__wrap(super(Selection, self).getMultiple())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.iterator()"""
        return 'Iterator'.__wrap(super(Selection, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.toArray(com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'.__wrap(super(__Selection, self).toArray(arg0))

    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.scenes.scene2d.utils.Selection.first()"""
        return object.__wrap(super(Selection, self).first())

    @override
    @overload
    def setDisabled(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setDisabled(boolean)"""
        super(__Selection, self).setDisabled(__boolean.valueOf(arg0))

    @overload
    def getToggle(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getToggle()"""
        return bool.__wrap(super(Selection, self).getToggle())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.clear()"""
        super(Selection, self).clear()

    @overload
    def getRequired(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getRequired()"""
        return bool.__wrap(super(Selection, self).getRequired())

    @overload
    def setAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__Selection, self).setAll(arg0)

    @overload
    def hasItems(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.hasItems()"""
        return bool.__wrap(super(Selection, self).hasItems())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Selection, self).setActor(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setToggle(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setToggle(boolean)"""
        super(__Selection, self).setToggle(__boolean.valueOf(arg0))

    @override
    @overload
    def isDisabled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.isDisabled()"""
        return bool.__wrap(super(Selection, self).isDisabled())

    @overload
    def getLastSelected(self) -> object:
        """public T com.badlogic.gdx.scenes.scene2d.utils.Selection.getLastSelected()"""
        return object.__wrap(super(Selection, self).getLastSelected())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.isEmpty()"""
        return bool.__wrap(super(Selection, self).isEmpty())

    @overload
    def remove(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.remove(T)"""
        super(__Selection, self).remove(arg0)

    @overload
    def setRequired(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setRequired(boolean)"""
        super(__Selection, self).setRequired(__boolean.valueOf(arg0))

    @overload
    def choose(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.choose(T)"""
        super(__Selection, self).choose(arg0)

    @overload
    def items(self) -> 'utils.OrderedSet':
        """public com.badlogic.gdx.utils.OrderedSet<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.items()"""
        return 'utils.OrderedSet'.__wrap(super(Selection, self).items()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as __BaseDrawable
__BaseDrawable = __BaseDrawable
from builtins import float
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable as __TextureRegionDrawable
__TextureRegionDrawable = __TextureRegionDrawable
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable as __TiledDrawable
__TiledDrawable = __TiledDrawable
from builtins import int
 
class TiledDrawable(__TextureRegionDrawable, TextureRegionDrawable):
    """com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable"""
 
    @staticmethod
    def __wrap(java_value: __TiledDrawable) -> 'TiledDrawable':
        return TiledDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TiledDrawable):
        """
        Dynamic initializer for TiledDrawable.
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
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(__BaseDrawable, self).setMinHeight(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.getRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(TextureRegionDrawable, self).getRegion())

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(__BaseDrawable, self).setBottomHeight(__float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float.__wrap(super(BaseDrawable, self).getMinWidth())

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.getColor()"""
        return 'graphics.Color'.__wrap(super(TiledDrawable, self).getColor())

    @overload
    def getScale(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.getScale()"""
        return float.__wrap(super(TiledDrawable, self).getScale())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(__BaseDrawable, self).setMinWidth(__float.valueOf(arg0))

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float.__wrap(super(BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float.__wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable()"""
        val = __TiledDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def tint(self, arg0: 'Color') -> 'TiledDrawable':
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.tint(com.badlogic.gdx.graphics.Color)"""
        return 'TiledDrawable'.__wrap(super(__TiledDrawable, self).tint(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable()"""
        val = __TiledDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(__TiledDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def __init__(self, arg0: 'TextureRegionDrawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable(com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable)"""
        val = __TiledDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(__BaseDrawable, self).setName(arg0)

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
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(__BaseDrawable, self).setRightWidth(__float.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str.__wrap(super(BaseDrawable, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __TiledDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.setScale(float)"""
        super(__TiledDrawable, self).setScale(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str.__wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(__BaseDrawable, self).setLeftWidth(__float.valueOf(arg0))

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(__BaseDrawable, self).setTopHeight(__float.valueOf(arg0))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float.__wrap(super(BaseDrawable, self).getMinHeight())

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(__BaseDrawable, self).setMinSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(__BaseDrawable, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def draw(arg0: 'Batch', arg1: 'TextureRegion', arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,int)"""
        __TiledDrawable.draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getAlign(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.getAlign()"""
        return int.__wrap(super(TiledDrawable, self).getAlign())

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(__TiledDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float.__wrap(super(BaseDrawable, self).getRightWidth())

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TextureRegionDrawable, self).setRegion(arg0)

    @overload
    def setAlign(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.TiledDrawable.setAlign(int)"""
        super(__TiledDrawable, self).setAlign(__int.valueOf(arg0))

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float.__wrap(super(BaseDrawable, self).getTopHeight()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as __BaseDrawable
__BaseDrawable = __BaseDrawable
from builtins import float
import java.lang.Long as __long
import com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable as __NinePatchDrawable
__NinePatchDrawable = __NinePatchDrawable
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g2d.NinePatch as __NinePatch
__NinePatch = __NinePatch
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class NinePatchDrawable(__BaseDrawable, BaseDrawable, __TransformDrawable, TransformDrawable):
    """com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable"""
 
    @staticmethod
    def __wrap(java_value: __NinePatchDrawable) -> 'NinePatchDrawable':
        return NinePatchDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NinePatchDrawable):
        """
        Dynamic initializer for NinePatchDrawable.
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
    def tint(self, arg0: 'Color') -> 'NinePatchDrawable':
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.tint(com.badlogic.gdx.graphics.Color)"""
        return 'NinePatchDrawable'.__wrap(super(__NinePatchDrawable, self).tint(arg0))

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(__BaseDrawable, self).setMinHeight(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(__BaseDrawable, self).setBottomHeight(__float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float.__wrap(super(BaseDrawable, self).getMinWidth())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(__BaseDrawable, self).setMinWidth(__float.valueOf(arg0))

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float.__wrap(super(BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float.__wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(__BaseDrawable, self).setName(arg0)

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
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(__BaseDrawable, self).setRightWidth(__float.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable()"""
        val = __NinePatchDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str.__wrap(super(BaseDrawable, self).getName())

    @overload
    def setPatch(self, arg0: 'NinePatch'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.setPatch(com.badlogic.gdx.graphics.g2d.NinePatch)"""
        super(__NinePatchDrawable, self).setPatch(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str.__wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(__BaseDrawable, self).setLeftWidth(__float.valueOf(arg0))

    @overload
    def getPatch(self) -> 'g2d.NinePatch':
        """public com.badlogic.gdx.graphics.g2d.NinePatch com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.getPatch()"""
        return 'g2d.NinePatch'.__wrap(super(NinePatchDrawable, self).getPatch())

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(__BaseDrawable, self).setTopHeight(__float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(__NinePatchDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float.__wrap(super(BaseDrawable, self).getMinHeight())

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(__BaseDrawable, self).setMinSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(__BaseDrawable, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'NinePatch'):
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable(com.badlogic.gdx.graphics.g2d.NinePatch)"""
        val = __NinePatchDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'NinePatchDrawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable(com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable)"""
        val = __NinePatchDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(__NinePatchDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float.__wrap(super(BaseDrawable, self).getRightWidth())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.NinePatchDrawable()"""
        val = __NinePatchDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float.__wrap(super(BaseDrawable, self).getTopHeight()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ClickListener
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.scenes.scene2d.InputListener as __InputListener
__InputListener = __InputListener
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener as __ClickListener
__ClickListener = __ClickListener
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
 
class ClickListener(scenes.__InputListener, scene2d.InputListener):
    """com.badlogic.gdx.scenes.scene2d.utils.ClickListener"""
 
    @staticmethod
    def __wrap(java_value: __ClickListener) -> 'ClickListener':
        return ClickListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClickListener):
        """
        Dynamic initializer for ClickListener.
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
    def getTapCount(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTapCount()"""
        return int.__wrap(super(ClickListener, self).getTapCount())

    @override
    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__ClickListener, self).touchDragged(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def getTapSquareSize(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTapSquareSize()"""
        return float.__wrap(super(ClickListener, self).getTapSquareSize())

    @overload
    def setTapCountInterval(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setTapCountInterval(float)"""
        super(__ClickListener, self).setTapCountInterval(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(__ClickListener, self).touchUp(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def isPressed(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isPressed()"""
        return bool.__wrap(super(ClickListener, self).isPressed())

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setTapSquareSize(float)"""
        super(__ClickListener, self).setTapSquareSize(__float.valueOf(arg0))

    @overload
    def getPressedButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getPressedButton()"""
        return int.__wrap(super(ClickListener, self).getPressedButton())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.ClickListener()"""
        val = __ClickListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.scenes.scene2d.utils.ClickListener(int)"""
        val = __ClickListener(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def invalidateTapSquare(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.invalidateTapSquare()"""
        super(ClickListener, self).invalidateTapSquare()

    @overload
    def setVisualPressed(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setVisualPressed(boolean)"""
        super(__ClickListener, self).setVisualPressed(__boolean.valueOf(arg0))

    @overload
    def isVisualPressed(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isVisualPressed()"""
        return bool.__wrap(super(ClickListener, self).isVisualPressed())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def clicked(self, arg0: 'InputEvent', arg1: float, arg2: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.clicked(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        super(__ClickListener, self).clicked(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def getTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTouchDownX()"""
        return float.__wrap(super(ClickListener, self).getTouchDownX())

    @overload
    def setTapCount(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setTapCount(int)"""
        super(__ClickListener, self).setTapCount(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__ClickListener, self).exit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def inTapSquare(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.inTapSquare()"""
        return bool.__wrap(super(ClickListener, self).inTapSquare())

    @override
    @overload
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__ClickListener, self).enter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4)

    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ClickListener.setButton(int)"""
        super(__ClickListener, self).setButton(__int.valueOf(arg0))

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool.__wrap(super(__scene2d.InputListener, self).mouseMoved(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def getPressedPointer(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getPressedPointer()"""
        return int.__wrap(super(ClickListener, self).getPressedPointer())

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool.__wrap(super(__scene2d.InputListener, self).keyTyped(arg0, __char.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isOver(self, arg0: 'Actor', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isOver(com.badlogic.gdx.scenes.scene2d.Actor,float,float)"""
        return bool.__wrap(super(__ClickListener, self).isOver(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getButton()"""
        return int.__wrap(super(ClickListener, self).getButton())

    @overload
    def inTapSquare(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.inTapSquare(float,float)"""
        return bool.__wrap(super(__ClickListener, self).inTapSquare(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool.__wrap(super(__scene2d.InputListener, self).keyDown(arg0, __int.valueOf(arg1)))

    @overload
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool.__wrap(super(__scene2d.InputListener, self).scrolled(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool.__wrap(super(__scene2d.InputListener, self).keyUp(arg0, __int.valueOf(arg1)))

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool.__wrap(super(__ClickListener, self).touchDown(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool.__wrap(super(__scene2d.InputListener, self).handle(arg0))

    @overload
    def getTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.ClickListener.getTouchDownY()"""
        return float.__wrap(super(ClickListener, self).getTouchDownY())

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
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ClickListener()"""
        val = __ClickListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isOver(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ClickListener.isOver()"""
        return bool.__wrap(super(ClickListener, self).isOver()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Drawable
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from abc import abstractmethod, ABC
import com.badlogic.gdx.scenes.scene2d.utils.Drawable as __Drawable
__Drawable = __Drawable
 
class Drawable(ABC):
    """com.badlogic.gdx.scenes.scene2d.utils.Drawable"""
 
    @staticmethod
    def __wrap(java_value: __Drawable) -> 'Drawable':
        return Drawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Drawable):
        """
        Dynamic initializer for Drawable.
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as __DragAndDrop_Payload
__Payload = __DragAndDrop_Payload.Payload
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Payload():
    """com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.Payload"""
 
    @staticmethod
    def __wrap(java_value: __Payload) -> 'Payload':
        return Payload(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Payload):
        """
        Dynamic initializer for Payload.
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
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload()"""
        val = __Payload()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setValidDragActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.setValidDragActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Payload, self).setValidDragActor(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setDragActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.setDragActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Payload, self).setDragActor(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload()"""
        val = __Payload()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getDragActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.getDragActor()"""
        return 'scene2d.Actor'.__wrap(super(Payload, self).getDragActor())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getInvalidDragActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.getInvalidDragActor()"""
        return 'scene2d.Actor'.__wrap(super(Payload, self).getInvalidDragActor())

    @overload
    def getObject(self) -> object:
        """public java.lang.Object com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.getObject()"""
        return object.__wrap(super(Payload, self).getObject())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setObject(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.setObject(java.lang.Object)"""
        super(__Payload, self).setObject(arg0)

    @overload
    def getValidDragActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.getValidDragActor()"""
        return 'scene2d.Actor'.__wrap(super(Payload, self).getValidDragActor())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setInvalidDragActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload.setInvalidDragActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Payload, self).setInvalidDragActor(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as __BaseDrawable
__BaseDrawable = __BaseDrawable
from builtins import float
import com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable as __SpriteDrawable
__SpriteDrawable = __SpriteDrawable
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.graphics.g2d.Sprite as __Sprite
__Sprite = __Sprite
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class SpriteDrawable(__BaseDrawable, BaseDrawable, __TransformDrawable, TransformDrawable):
    """com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable"""
 
    @staticmethod
    def __wrap(java_value: __SpriteDrawable) -> 'SpriteDrawable':
        return SpriteDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpriteDrawable):
        """
        Dynamic initializer for SpriteDrawable.
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
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(__BaseDrawable, self).setMinHeight(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(__BaseDrawable, self).setBottomHeight(__float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float.__wrap(super(BaseDrawable, self).getMinWidth())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(__BaseDrawable, self).setMinWidth(__float.valueOf(arg0))

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float.__wrap(super(BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float.__wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(__SpriteDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(__SpriteDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(__BaseDrawable, self).setName(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable()"""
        val = __SpriteDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def tint(self, arg0: 'Color') -> 'SpriteDrawable':
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.tint(com.badlogic.gdx.graphics.Color)"""
        return 'SpriteDrawable'.__wrap(super(__SpriteDrawable, self).tint(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable()"""
        val = __SpriteDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(__BaseDrawable, self).setRightWidth(__float.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str.__wrap(super(BaseDrawable, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'SpriteDrawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable(com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable)"""
        val = __SpriteDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str.__wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(__BaseDrawable, self).setLeftWidth(__float.valueOf(arg0))

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(__BaseDrawable, self).setTopHeight(__float.valueOf(arg0))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float.__wrap(super(BaseDrawable, self).getMinHeight())

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(__BaseDrawable, self).setMinSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(__BaseDrawable, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getSprite(self) -> 'g2d.Sprite':
        """public com.badlogic.gdx.graphics.g2d.Sprite com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.getSprite()"""
        return 'g2d.Sprite'.__wrap(super(SpriteDrawable, self).getSprite())

    @overload
    def setSprite(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable.setSprite(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(__SpriteDrawable, self).setSprite(arg0)

    @overload
    def __init__(self, arg0: 'Sprite'):
        """public com.badlogic.gdx.scenes.scene2d.utils.SpriteDrawable(com.badlogic.gdx.graphics.g2d.Sprite)"""
        val = __SpriteDrawable(arg0)
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float.__wrap(super(BaseDrawable, self).getRightWidth())

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float.__wrap(super(BaseDrawable, self).getTopHeight()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.TransformDrawable
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.scenes.scene2d.utils.TransformDrawable as __TransformDrawable
__TransformDrawable = __TransformDrawable
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from abc import abstractmethod, ABC
import com.badlogic.gdx.scenes.scene2d.utils.Drawable as __Drawable
__Drawable = __Drawable
 
class TransformDrawable(ABC, __Drawable, Drawable):
    """com.badlogic.gdx.scenes.scene2d.utils.TransformDrawable"""
 
    @staticmethod
    def __wrap(java_value: __TransformDrawable) -> 'TransformDrawable':
        return TransformDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TransformDrawable):
        """
        Dynamic initializer for TransformDrawable.
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
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as __BaseDrawable
__BaseDrawable = __BaseDrawable
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
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
 
class BaseDrawable(__Drawable, Drawable):
    """com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable"""
 
    @staticmethod
    def __wrap(java_value: __BaseDrawable) -> 'BaseDrawable':
        return BaseDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseDrawable):
        """
        Dynamic initializer for BaseDrawable.
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
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(__BaseDrawable, self).setMinHeight(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(__BaseDrawable, self).setBottomHeight(__float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float.__wrap(super(BaseDrawable, self).getMinWidth())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(__BaseDrawable, self).setMinWidth(__float.valueOf(arg0))

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float.__wrap(super(BaseDrawable, self).getBottomHeight())

    @overload
    def __init__(self, arg0: 'Drawable'):
        """public com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable(com.badlogic.gdx.scenes.scene2d.utils.Drawable)"""
        val = __BaseDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float.__wrap(super(BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable()"""
        val = __BaseDrawable()
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

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str.__wrap(super(BaseDrawable, self).getName())

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(__BaseDrawable, self).setRightWidth(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str.__wrap(super(BaseDrawable, self).toString())

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(__BaseDrawable, self).setLeftWidth(__float.valueOf(arg0))

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(__BaseDrawable, self).setTopHeight(__float.valueOf(arg0))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float.__wrap(super(BaseDrawable, self).getMinHeight())

    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(__BaseDrawable, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(__BaseDrawable, self).setMinSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable()"""
        val = __BaseDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(__BaseDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float.__wrap(super(BaseDrawable, self).getRightWidth())

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(__BaseDrawable, self).setName(arg0)

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float.__wrap(super(BaseDrawable, self).getTopHeight()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop as __DragAndDrop_Target
__Target = __DragAndDrop_Target.Target
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Target(ABC):
    """com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop.Target"""
 
    @staticmethod
    def __wrap(java_value: __Target) -> 'Target':
        return Target(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Target):
        """
        Dynamic initializer for Target.
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
    def drop(self, arg0: 'Source', arg1: 'Payload', arg2: float, arg3: float, arg4: int):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target.drop(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload,float,float,int)"""
        pass

    @abstractmethod
    def drag(self, arg0: 'Source', arg1: 'Payload', arg2: float, arg3: float, arg4: int):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target.drag(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload,float,float,int)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Actor'):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target(com.badlogic.gdx.scenes.scene2d.Actor)"""
        val = __Target(arg0)
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target.getActor()"""
        return 'scene2d.Actor'.__wrap(super(Target, self).getActor())

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
    def reset(self, arg0: 'Source', arg1: 'Payload'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Target.reset(com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Source,com.badlogic.gdx.scenes.scene2d.utils.DragAndDrop$Payload)"""
        super(__Target, self).reset(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
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
import com.badlogic.gdx.scenes.scene2d.Actor as __Actor
__Actor = __Actor
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener as __ActorGestureListener
__ActorGestureListener = __ActorGestureListener
from builtins import bool
try:
    from pygdx import input
except ImportError:
    input = __import_once__("pygdx.input")

import com.badlogic.gdx.input.GestureDetector as __GestureDetector
__GestureDetector = __GestureDetector
from builtins import int
 
class ActorGestureListener(scenes.__EventListener, scene2d.EventListener):
    """com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener"""
 
    @staticmethod
    def __wrap(java_value: __ActorGestureListener) -> 'ActorGestureListener':
        return ActorGestureListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ActorGestureListener):
        """
        Dynamic initializer for ActorGestureListener.
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
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(__ActorGestureListener, self).touchDown(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener(float,float,float,float)"""
        val = __ActorGestureListener(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def pinch(self, arg0: 'InputEvent', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Vector2', arg4: 'Vector2'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.pinch(com.badlogic.gdx.scenes.scene2d.InputEvent,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__ActorGestureListener, self).pinch(arg0, arg1, arg2, arg3, arg4)

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool.__wrap(super(__ActorGestureListener, self).handle(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def pan(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.pan(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        super(__ActorGestureListener, self).pan(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def longPress(self, arg0: 'Actor', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.longPress(com.badlogic.gdx.scenes.scene2d.Actor,float,float)"""
        return bool.__wrap(super(__ActorGestureListener, self).longPress(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def panStop(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.panStop(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(__ActorGestureListener, self).panStop(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(__ActorGestureListener, self).touchUp(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

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
        """public com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener()"""
        val = __ActorGestureListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getGestureDetector(self) -> 'input.GestureDetector':
        """public com.badlogic.gdx.input.GestureDetector com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.getGestureDetector()"""
        return 'input.GestureDetector'.__wrap(super(ActorGestureListener, self).getGestureDetector())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener()"""
        val = __ActorGestureListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def zoom(self, arg0: 'InputEvent', arg1: float, arg2: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.zoom(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        super(__ActorGestureListener, self).zoom(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def fling(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.fling(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__ActorGestureListener, self).fling(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTouchDownTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.getTouchDownTarget()"""
        return 'scene2d.Actor'.__wrap(super(ActorGestureListener, self).getTouchDownTarget())

    @overload
    def tap(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ActorGestureListener.tap(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(__ActorGestureListener, self).tap(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
import com.badlogic.gdx.scenes.scene2d.utils.DragListener as __DragListener
__DragListener = __DragListener
import java.lang.Character as __char
import com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener as __DragScrollListener
__DragScrollListener = __DragScrollListener
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.scenes.scene2d.InputListener as __InputListener
__InputListener = __InputListener
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.scenes.scene2d import ui
except ImportError:
    ui = __import_once__("pygdx.scenes.scene2d.ui")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DragScrollListener(__DragListener, DragListener):
    """com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener"""
 
    @staticmethod
    def __wrap(java_value: __DragScrollListener) -> 'DragScrollListener':
        return DragScrollListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DragScrollListener):
        """
        Dynamic initializer for DragScrollListener.
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
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.InputListener, self).exit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4)

    @override
    @overload
    def drag(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener.drag(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__DragScrollListener, self).drag(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getDragStartY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragStartY()"""
        return float.__wrap(super(DragListener, self).getDragStartY())

    @override
    @overload
    def isDragging(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragListener.isDragging()"""
        return bool.__wrap(super(DragListener, self).isDragging())

    @override
    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(__DragListener, self).touchUp(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def getDragStartX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragStartX()"""
        return float.__wrap(super(DragListener, self).getDragStartX())

    @override
    @overload
    def dragStop(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener.dragStop(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__DragScrollListener, self).dragStop(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setDragStartY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setDragStartY(float)"""
        super(__DragListener, self).setDragStartY(__float.valueOf(arg0))

    @override
    @overload
    def getButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.DragListener.getButton()"""
        return int.__wrap(super(DragListener, self).getButton())

    @override
    @overload
    def getTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTouchDownX()"""
        return float.__wrap(super(DragListener, self).getTouchDownX())

    @override
    @overload
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.InputListener, self).enter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4)

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
    def getDeltaY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDeltaY()"""
        return float.__wrap(super(DragListener, self).getDeltaY())

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool.__wrap(super(__DragListener, self).touchDown(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'ScrollPane'):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener(com.badlogic.gdx.scenes.scene2d.ui.ScrollPane)"""
        val = __DragScrollListener(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getDragX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragX()"""
        return float.__wrap(super(DragListener, self).getDragX())

    @override
    @overload
    def getDragDistance(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragDistance()"""
        return float.__wrap(super(DragListener, self).getDragDistance())

    @override
    @overload
    def getTapSquareSize(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTapSquareSize()"""
        return float.__wrap(super(DragListener, self).getTapSquareSize())

    @overload
    def setPadding(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener.setPadding(float,float)"""
        super(__DragScrollListener, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setDragStartX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setDragStartX(float)"""
        super(__DragListener, self).setDragStartX(__float.valueOf(arg0))

    @override
    @overload
    def getTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTouchDownY()"""
        return float.__wrap(super(DragListener, self).getTouchDownY())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__DragListener, self).touchDragged(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool.__wrap(super(__scene2d.InputListener, self).mouseMoved(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setTapSquareSize(float)"""
        super(__DragListener, self).setTapSquareSize(__float.valueOf(arg0))

    @override
    @overload
    def getDragY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragY()"""
        return float.__wrap(super(DragListener, self).getDragY())

    @overload
    def setup(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragScrollListener.setup(float,float,float,float)"""
        super(__DragScrollListener, self).setup(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool.__wrap(super(__scene2d.InputListener, self).keyTyped(arg0, __char.valueOf(arg1)))

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
    def getDeltaX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDeltaX()"""
        return float.__wrap(super(DragListener, self).getDeltaX())

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool.__wrap(super(__scene2d.InputListener, self).keyDown(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setButton(int)"""
        super(__DragListener, self).setButton(__int.valueOf(arg0))

    @overload
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool.__wrap(super(__scene2d.InputListener, self).scrolled(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool.__wrap(super(__scene2d.InputListener, self).keyUp(arg0, __int.valueOf(arg1)))

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool.__wrap(super(__scene2d.InputListener, self).handle(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getStageTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getStageTouchDownX()"""
        return float.__wrap(super(DragListener, self).getStageTouchDownX())

    @override
    @overload
    def dragStart(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.dragStart(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__DragListener, self).dragStart(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getStageTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getStageTouchDownY()"""
        return float.__wrap(super(DragListener, self).getStageTouchDownY()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.Event as __Event
__Event = __Event
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener as __FocusListener_FocusEvent
__FocusEvent = __FocusListener_FocusEvent.FocusEvent
import com.badlogic.gdx.scenes.scene2d.utils.FocusListener as __FocusListener_FocusEvent_Type
__Type = __FocusListener_FocusEvent_Type.FocusEvent.Type
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
 
class FocusEvent(scenes.__Event, scene2d.Event):
    """com.badlogic.gdx.scenes.scene2d.utils.FocusListener.FocusEvent"""
 
    @staticmethod
    def __wrap(java_value: __FocusEvent) -> 'FocusEvent':
        return FocusEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FocusEvent):
        """
        Dynamic initializer for FocusEvent.
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
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent()"""
        val = __FocusEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setRelatedActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.setRelatedActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__FocusEvent, self).setRelatedActor(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent()"""
        val = __FocusEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setListenerActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setListenerActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Event, self).setListenerActor(arg0)

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCancelled()"""
        return bool.__wrap(super(scene2d.Event, self).isCancelled())

    @override
    @overload
    def getBubbles(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.getBubbles()"""
        return bool.__wrap(super(scene2d.Event, self).getBubbles())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getListenerActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getListenerActor()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Event, self).getListenerActor())

    @override
    @overload
    def isHandled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isHandled()"""
        return bool.__wrap(super(scene2d.Event, self).isHandled())

    @overload
    def setType(self, arg0: 'Type'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.setType(com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type)"""
        super(__FocusEvent, self).setType(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def isStopped(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isStopped()"""
        return bool.__wrap(super(scene2d.Event, self).isStopped())

    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.stop()"""
        super(scene2d.Event, self).stop()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isCapture(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.Event.isCapture()"""
        return bool.__wrap(super(scene2d.Event, self).isCapture())

    @override
    @overload
    def setStage(self, arg0: 'Stage'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setStage(com.badlogic.gdx.scenes.scene2d.Stage)"""
        super(__scene2d.Event, self).setStage(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.reset()"""
        super(FocusEvent, self).reset()

    @override
    @overload
    def setTarget(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setTarget(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.Event, self).setTarget(arg0)

    @override
    @overload
    def setCapture(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setCapture(boolean)"""
        super(__scene2d.Event, self).setCapture(__boolean.valueOf(arg0))

    @overload
    def getRelatedActor(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.getRelatedActor()"""
        return 'scene2d.Actor'.__wrap(super(FocusEvent, self).getRelatedActor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isFocused(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.isFocused()"""
        return bool.__wrap(super(FocusEvent, self).isFocused())

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
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.cancel()"""
        super(scene2d.Event, self).cancel()

    @override
    @overload
    def getTarget(self) -> 'scene2d.Actor':
        """public com.badlogic.gdx.scenes.scene2d.Actor com.badlogic.gdx.scenes.scene2d.Event.getTarget()"""
        return 'scene2d.Actor'.__wrap(super(scene2d.Event, self).getTarget())

    @override
    @overload
    def getStage(self) -> 'scene2d.Stage':
        """public com.badlogic.gdx.scenes.scene2d.Stage com.badlogic.gdx.scenes.scene2d.Event.getStage()"""
        return 'scene2d.Stage'.__wrap(super(scene2d.Event, self).getStage())

    @override
    @overload
    def setBubbles(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.Event.setBubbles(boolean)"""
        super(__scene2d.Event, self).setBubbles(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setFocused(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.setFocused(boolean)"""
        super(__FocusEvent, self).setFocused(__boolean.valueOf(arg0))

    @overload
    def getType(self) -> 'Type':
        """public com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent$Type com.badlogic.gdx.scenes.scene2d.utils.FocusListener$FocusEvent.getType()"""
        return 'Type'.__wrap(super(FocusEvent, self).getType())

    @override
    @overload
    def handle(self):
        """public void com.badlogic.gdx.scenes.scene2d.Event.handle()"""
        super(scene2d.Event, self).handle() 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.DragListener
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

from builtins import str
import com.badlogic.gdx.scenes.scene2d.utils.DragListener as __DragListener
__DragListener = __DragListener
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
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
 
class DragListener(scenes.__InputListener, scene2d.InputListener):
    """com.badlogic.gdx.scenes.scene2d.utils.DragListener"""
 
    @staticmethod
    def __wrap(java_value: __DragListener) -> 'DragListener':
        return DragListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DragListener):
        """
        Dynamic initializer for DragListener.
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
    def getDragStartY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragStartY()"""
        return float.__wrap(super(DragListener, self).getDragStartY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getButton(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.DragListener.getButton()"""
        return int.__wrap(super(DragListener, self).getButton())

    @override
    @overload
    def exit(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.exit(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.InputListener, self).exit(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4)

    @overload
    def getDeltaX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDeltaX()"""
        return float.__wrap(super(DragListener, self).getDeltaX())

    @override
    @overload
    def touchUp(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchUp(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        super(__DragListener, self).touchUp(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def getDragY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragY()"""
        return float.__wrap(super(DragListener, self).getDragY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setTapSquareSize(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setTapSquareSize(float)"""
        super(__DragListener, self).setTapSquareSize(__float.valueOf(arg0))

    @overload
    def setDragStartY(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setDragStartY(float)"""
        super(__DragListener, self).setDragStartY(__float.valueOf(arg0))

    @override
    @overload
    def enter(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.InputListener.enter(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__scene2d.InputListener, self).enter(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def touchDown(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchDown(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int,int)"""
        return bool.__wrap(super(__DragListener, self).touchDown(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def getTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTouchDownX()"""
        return float.__wrap(super(DragListener, self).getTouchDownX())

    @overload
    def getDragStartX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragStartX()"""
        return float.__wrap(super(DragListener, self).getDragStartX())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragListener()"""
        val = __DragListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setButton(self, arg0: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setButton(int)"""
        super(__DragListener, self).setButton(__int.valueOf(arg0))

    @overload
    def setDragStartX(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.setDragStartX(float)"""
        super(__DragListener, self).setDragStartX(__float.valueOf(arg0))

    @overload
    def getDeltaY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDeltaY()"""
        return float.__wrap(super(DragListener, self).getDeltaY())

    @overload
    def dragStart(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.dragStart(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__DragListener, self).dragStart(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getStageTouchDownX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getStageTouchDownX()"""
        return float.__wrap(super(DragListener, self).getStageTouchDownX())

    @override
    @overload
    def touchDragged(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.touchDragged(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__DragListener, self).touchDragged(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def getTapSquareSize(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTapSquareSize()"""
        return float.__wrap(super(DragListener, self).getTapSquareSize())

    @overload
    def mouseMoved(self, arg0: 'InputEvent', arg1: float, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.mouseMoved(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float)"""
        return bool.__wrap(super(__scene2d.InputListener, self).mouseMoved(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def getTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getTouchDownY()"""
        return float.__wrap(super(DragListener, self).getTouchDownY())

    @overload
    def isDragging(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.DragListener.isDragging()"""
        return bool.__wrap(super(DragListener, self).isDragging())

    @overload
    def dragStop(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.dragStop(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__DragListener, self).dragStop(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def keyTyped(self, arg0: 'InputEvent', arg1: str) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyTyped(com.badlogic.gdx.scenes.scene2d.InputEvent,char)"""
        return bool.__wrap(super(__scene2d.InputListener, self).keyTyped(arg0, __char.valueOf(arg1)))

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
    def getStageTouchDownY(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getStageTouchDownY()"""
        return float.__wrap(super(DragListener, self).getStageTouchDownY())

    @overload
    def keyDown(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyDown(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool.__wrap(super(__scene2d.InputListener, self).keyDown(arg0, __int.valueOf(arg1)))

    @overload
    def scrolled(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.scrolled(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,float,float)"""
        return bool.__wrap(super(__scene2d.InputListener, self).scrolled(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def keyUp(self, arg0: 'InputEvent', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.keyUp(com.badlogic.gdx.scenes.scene2d.InputEvent,int)"""
        return bool.__wrap(super(__scene2d.InputListener, self).keyUp(arg0, __int.valueOf(arg1)))

    @overload
    def cancel(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.cancel()"""
        super(DragListener, self).cancel()

    @overload
    def handle(self, arg0: 'Event') -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.InputListener.handle(com.badlogic.gdx.scenes.scene2d.Event)"""
        return bool.__wrap(super(__scene2d.InputListener, self).handle(arg0))

    @overload
    def getDragDistance(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragDistance()"""
        return float.__wrap(super(DragListener, self).getDragDistance())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.DragListener()"""
        val = __DragListener()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDragX(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.DragListener.getDragX()"""
        return float.__wrap(super(DragListener, self).getDragX())

    @overload
    def drag(self, arg0: 'InputEvent', arg1: float, arg2: float, arg3: int):
        """public void com.badlogic.gdx.scenes.scene2d.utils.DragListener.drag(com.badlogic.gdx.scenes.scene2d.InputEvent,float,float,int)"""
        super(__DragListener, self).drag(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ScissorStack
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.ScissorStack as __ScissorStack
__ScissorStack = __ScissorStack
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ScissorStack():
    """com.badlogic.gdx.scenes.scene2d.utils.ScissorStack"""
 
    @staticmethod
    def __wrap(java_value: __ScissorStack) -> 'ScissorStack':
        return ScissorStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScissorStack):
        """
        Dynamic initializer for ScissorStack.
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
    def calculateScissors(arg0: 'Camera', arg1: 'Matrix4', arg2: 'Rectangle', arg3: 'Rectangle'):
        """public static void com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.calculateScissors(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        __ScissorStack.calculateScissors(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def calculateScissors(arg0: 'Camera', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Matrix4', arg6: 'Rectangle', arg7: 'Rectangle'):
        """public static void com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.calculateScissors(com.badlogic.gdx.graphics.Camera,float,float,float,float,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.math.Rectangle)"""
        __ScissorStack.calculateScissors(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5, arg6, arg7)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.scenes.scene2d.utils.ScissorStack()"""
        val = __ScissorStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.scenes.scene2d.utils.ScissorStack()"""
        val = __ScissorStack()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def peekScissors() -> 'math.Rectangle':
        """public static com.badlogic.gdx.math.Rectangle com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.peekScissors()"""
        return math.Rectangle.__wrap(__ScissorStack.peekScissors())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def popScissors() -> 'math.Rectangle':
        """public static com.badlogic.gdx.math.Rectangle com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.popScissors()"""
        return math.Rectangle.__wrap(__ScissorStack.popScissors())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def pushScissors(arg0: 'Rectangle') -> bool:
        """public static boolean com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.pushScissors(com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(__ScissorStack.pushScissors(arg0))

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

    @staticmethod
    @overload
    def getViewport() -> 'math.Rectangle':
        """public static com.badlogic.gdx.math.Rectangle com.badlogic.gdx.scenes.scene2d.utils.ScissorStack.getViewport()"""
        return math.Rectangle.__wrap(__ScissorStack.getViewport())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.ArraySelection
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.utils.OrderedSet as __OrderedSet
__OrderedSet = __OrderedSet
try:
    from pygdx.scenes import scene2d
except ImportError:
    scene2d = __import_once__("pygdx.scenes.scene2d")

import java.lang.Boolean as __boolean
from builtins import type
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
from builtins import bool
from builtins import str
import com.badlogic.gdx.scenes.scene2d.utils.ArraySelection as __ArraySelection
__ArraySelection = __ArraySelection
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import com.badlogic.gdx.scenes.scene2d.utils.Selection as __Selection
__Selection = __Selection
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class ArraySelection(__Selection, Selection):
    """com.badlogic.gdx.scenes.scene2d.utils.ArraySelection"""
 
    @staticmethod
    def __wrap(java_value: __ArraySelection) -> 'ArraySelection':
        return ArraySelection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArraySelection):
        """
        Dynamic initializer for ArraySelection.
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
    def validate(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ArraySelection.validate()"""
        super(ArraySelection, self).validate()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.contains(T)"""
        return bool.__wrap(super(__Selection, self).contains(arg0))

    @override
    @overload
    def first(self) -> object:
        """public T com.badlogic.gdx.scenes.scene2d.utils.Selection.first()"""
        return object.__wrap(super(Selection, self).first())

    @override
    @overload
    def setProgrammaticChangeEvents(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setProgrammaticChangeEvents(boolean)"""
        super(__Selection, self).setProgrammaticChangeEvents(__boolean.valueOf(arg0))

    @override
    @overload
    def choose(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ArraySelection.choose(T)"""
        super(__ArraySelection, self).choose(arg0)

    @override
    @overload
    def removeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.removeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__Selection, self).removeAll(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRangeSelect(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.ArraySelection.getRangeSelect()"""
        return bool.__wrap(super(ArraySelection, self).getRangeSelect())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.scenes.scene2d.utils.ArraySelection(com.badlogic.gdx.utils.Array<T>)"""
        val = __ArraySelection(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def set(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.set(T)"""
        super(__Selection, self).set(arg0)

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.clear()"""
        super(Selection, self).clear()

    @override
    @overload
    def fireChangeEvent(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.fireChangeEvent()"""
        return bool.__wrap(super(Selection, self).fireChangeEvent())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMultiple(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setMultiple(boolean)"""
        super(__Selection, self).setMultiple(__boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.Selection.toString()"""
        return str.__wrap(super(Selection, self).toString())

    @override
    @overload
    def addAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.addAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__Selection, self).addAll(arg0)

    @override
    @overload
    def getToggle(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getToggle()"""
        return bool.__wrap(super(Selection, self).getToggle())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.add(T)"""
        super(__Selection, self).add(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.iterator()"""
        return 'Iterator'.__wrap(super(Selection, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def toArray(self, arg0: 'Array') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.toArray(com.badlogic.gdx.utils.Array<T>)"""
        return 'utils.Array'.__wrap(super(__Selection, self).toArray(arg0))

    @override
    @overload
    def notEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.notEmpty()"""
        return bool.__wrap(super(Selection, self).notEmpty())

    @override
    @overload
    def setDisabled(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setDisabled(boolean)"""
        super(__Selection, self).setDisabled(__boolean.valueOf(arg0))

    @override
    @overload
    def getRequired(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getRequired()"""
        return bool.__wrap(super(Selection, self).getRequired())

    @override
    @overload
    def setRequired(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setRequired(boolean)"""
        super(__Selection, self).setRequired(__boolean.valueOf(arg0))

    @override
    @overload
    def getLastSelected(self) -> object:
        """public T com.badlogic.gdx.scenes.scene2d.utils.Selection.getLastSelected()"""
        return object.__wrap(super(Selection, self).getLastSelected())

    @override
    @overload
    def getMultiple(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.getMultiple()"""
        return bool.__wrap(super(Selection, self).getMultiple())

    @overload
    def setRangeSelect(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.ArraySelection.setRangeSelect(boolean)"""
        super(__ArraySelection, self).setRangeSelect(__boolean.valueOf(arg0))

    @override
    @overload
    def toArray(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.toArray()"""
        return 'utils.Array'.__wrap(super(Selection, self).toArray())

    @override
    @overload
    def remove(self, arg0: object):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.remove(T)"""
        super(__Selection, self).remove(arg0)

    @override
    @overload
    def setToggle(self, arg0: bool):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setToggle(boolean)"""
        super(__Selection, self).setToggle(__boolean.valueOf(arg0))

    @override
    @overload
    def setActor(self, arg0: 'Actor'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setActor(com.badlogic.gdx.scenes.scene2d.Actor)"""
        super(__Selection, self).setActor(arg0)

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
    def setAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.scenes.scene2d.utils.Selection.setAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__Selection, self).setAll(arg0)

    @override
    @overload
    def hasItems(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.hasItems()"""
        return bool.__wrap(super(Selection, self).hasItems())

    @override
    @overload
    def items(self) -> 'utils.OrderedSet':
        """public com.badlogic.gdx.utils.OrderedSet<T> com.badlogic.gdx.scenes.scene2d.utils.Selection.items()"""
        return 'utils.OrderedSet'.__wrap(super(Selection, self).items())

    @override
    @overload
    def isDisabled(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.isDisabled()"""
        return bool.__wrap(super(Selection, self).isDisabled())

    @override
    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.scenes.scene2d.utils.Selection.size()"""
        return int.__wrap(super(Selection, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.badlogic.gdx.scenes.scene2d.utils.Selection.isEmpty()"""
        return bool.__wrap(super(Selection, self).isEmpty()) 
 
 
# CLASS: com.badlogic.gdx.scenes.scene2d.utils.Disableable
import com.badlogic.gdx.scenes.scene2d.utils.Disableable as __Disableable
__Disableable = __Disableable
from abc import abstractmethod, ABC
 
class Disableable(ABC):
    """com.badlogic.gdx.scenes.scene2d.utils.Disableable"""
 
    @staticmethod
    def __wrap(java_value: __Disableable) -> 'Disableable':
        return Disableable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Disableable):
        """
        Dynamic initializer for Disableable.
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
    def setDisabled(self, arg0: bool):
        """public abstract void com.badlogic.gdx.scenes.scene2d.utils.Disableable.setDisabled(boolean)"""
        pass

    @abstractmethod
    def isDisabled(self, ):
        """public abstract boolean com.badlogic.gdx.scenes.scene2d.utils.Disableable.isDisabled()"""
        pass
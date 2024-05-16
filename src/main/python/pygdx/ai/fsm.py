from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.fsm.State as _State
_State = _State
from abc import abstractmethod, ABC
try:
    from pygdx.ai import msg
except ImportError:
    msg = _import_once("pygdx.ai.msg")

 
class State():
    """com.badlogic.gdx.ai.fsm.State"""
 
    @staticmethod
    def _wrap(java_value: _State) -> 'State':
        return State(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _State):
        """
        Dynamic initializer for State.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_State__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_State__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def update(self, arg0: object):
        """public abstract void com.badlogic.gdx.ai.fsm.State.update(E)"""
        pass

    @abstractmethod
    def exit(self, arg0: object):
        """public abstract void com.badlogic.gdx.ai.fsm.State.exit(E)"""
        pass

    @abstractmethod
    def onMessage(self, arg0: object, arg1: 'Telegram'):
        """public abstract boolean com.badlogic.gdx.ai.fsm.State.onMessage(E,com.badlogic.gdx.ai.msg.Telegram)"""
        pass

    @abstractmethod
    def enter(self, arg0: object):
        """public abstract void com.badlogic.gdx.ai.fsm.State.enter(E)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.fsm.State
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.fsm.State as _State
_State = _State
from abc import abstractmethod, ABC
try:
    from pygdx.ai import msg
except ImportError:
    msg = _import_once("pygdx.ai.msg")

 
class State():
    """com.badlogic.gdx.ai.fsm.State"""
 
    @staticmethod
    def _wrap(java_value: _State) -> 'State':
        return State(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _State):
        """
        Dynamic initializer for State.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_State__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_State__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def update(self, arg0: object):
        """public abstract void com.badlogic.gdx.ai.fsm.State.update(E)"""
        pass

    @abstractmethod
    def exit(self, arg0: object):
        """public abstract void com.badlogic.gdx.ai.fsm.State.exit(E)"""
        pass

    @abstractmethod
    def onMessage(self, arg0: object, arg1: 'Telegram'):
        """public abstract boolean com.badlogic.gdx.ai.fsm.State.onMessage(E,com.badlogic.gdx.ai.msg.Telegram)"""
        pass

    @abstractmethod
    def enter(self, arg0: object):
        """public abstract void com.badlogic.gdx.ai.fsm.State.enter(E)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.fsm.State 
 
 
# CLASS: com.badlogic.gdx.ai.fsm.StateMachine
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.fsm.StateMachine as _StateMachine
_StateMachine = _StateMachine
from abc import abstractmethod, ABC
try:
    from pygdx.ai import msg
except ImportError:
    msg = _import_once("pygdx.ai.msg")

 
class StateMachine():
    """com.badlogic.gdx.ai.fsm.StateMachine"""
 
    @staticmethod
    def _wrap(java_value: _StateMachine) -> 'StateMachine':
        return StateMachine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StateMachine):
        """
        Dynamic initializer for StateMachine.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StateMachine__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StateMachine__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setInitialState(self, arg0: 'State'):
        """public abstract void com.badlogic.gdx.ai.fsm.StateMachine.setInitialState(S)"""
        pass

    @abstractmethod
    def changeState(self, arg0: 'State'):
        """public abstract void com.badlogic.gdx.ai.fsm.StateMachine.changeState(S)"""
        pass

    @abstractmethod
    def isInState(self, arg0: 'State'):
        """public abstract boolean com.badlogic.gdx.ai.fsm.StateMachine.isInState(S)"""
        pass

    @abstractmethod
    def revertToPreviousState(self, ):
        """public abstract boolean com.badlogic.gdx.ai.fsm.StateMachine.revertToPreviousState()"""
        pass

    @abstractmethod
    def getGlobalState(self, ):
        """public abstract S com.badlogic.gdx.ai.fsm.StateMachine.getGlobalState()"""
        pass

    @abstractmethod
    def getCurrentState(self, ):
        """public abstract S com.badlogic.gdx.ai.fsm.StateMachine.getCurrentState()"""
        pass

    @abstractmethod
    def handleMessage(self, arg0: 'Telegram'):
        """public abstract boolean com.badlogic.gdx.ai.fsm.StateMachine.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        pass

    @abstractmethod
    def update(self, ):
        """public abstract void com.badlogic.gdx.ai.fsm.StateMachine.update()"""
        pass

    @abstractmethod
    def setGlobalState(self, arg0: 'State'):
        """public abstract void com.badlogic.gdx.ai.fsm.StateMachine.setGlobalState(S)"""
        pass

    @abstractmethod
    def getPreviousState(self, ):
        """public abstract S com.badlogic.gdx.ai.fsm.StateMachine.getPreviousState()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.fsm.DefaultStateMachine
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.ai.fsm.DefaultStateMachine as _DefaultStateMachine
_DefaultStateMachine = _DefaultStateMachine
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pygdx.ai import msg
except ImportError:
    msg = _import_once("pygdx.ai.msg")

import com.badlogic.gdx.ai.fsm.State as _State
_State = _State
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultStateMachine():
    """com.badlogic.gdx.ai.fsm.DefaultStateMachine"""
 
    @staticmethod
    def _wrap(java_value: _DefaultStateMachine) -> 'DefaultStateMachine':
        return DefaultStateMachine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultStateMachine):
        """
        Dynamic initializer for DefaultStateMachine.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultStateMachine__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultStateMachine__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def changeState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.changeState(S)"""
        super(_DefaultStateMachine, self).changeState(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getGlobalState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.DefaultStateMachine.getGlobalState()"""
        return 'State'._wrap(super(DefaultStateMachine, self).getGlobalState())

    @override
    @overload
    def getCurrentState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.DefaultStateMachine.getCurrentState()"""
        return 'State'._wrap(super(DefaultStateMachine, self).getCurrentState())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine()"""
        val = _DefaultStateMachine()
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
    def getPreviousState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.DefaultStateMachine.getPreviousState()"""
        return 'State'._wrap(super(DefaultStateMachine, self).getPreviousState())

    @override
    @overload
    def setInitialState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setInitialState(S)"""
        super(_DefaultStateMachine, self).setInitialState(arg0)

    @override
    @overload
    def revertToPreviousState(self) -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.revertToPreviousState()"""
        return bool._wrap(super(DefaultStateMachine, self).revertToPreviousState())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.update()"""
        super(DefaultStateMachine, self).update()

    @override
    @overload
    def setGlobalState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setGlobalState(S)"""
        super(_DefaultStateMachine, self).setGlobalState(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: 'State'):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine(E,S)"""
        val = _DefaultStateMachine(arg0, arg1)
        self.__wrapper = val

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool._wrap(super(_DefaultStateMachine, self).handleMessage(arg0))

    @overload
    def __init__(self, arg0: object):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine(E)"""
        val = _DefaultStateMachine(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine()"""
        val = _DefaultStateMachine()
        self.__wrapper = val

    @overload
    def setOwner(self, arg0: object):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setOwner(E)"""
        super(_DefaultStateMachine, self).setOwner(arg0)

    @overload
    def isInState(self, arg0: 'State') -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.isInState(S)"""
        return bool._wrap(super(_DefaultStateMachine, self).isInState(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'State', arg2: 'State'):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine(E,S,S)"""
        val = _DefaultStateMachine(arg0, arg1, arg2)
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
    def getOwner(self) -> object:
        """public E com.badlogic.gdx.ai.fsm.DefaultStateMachine.getOwner()"""
        return object._wrap(super(DefaultStateMachine, self).getOwner())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.fsm.StackStateMachine
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.fsm.StackStateMachine as _StackStateMachine
_StackStateMachine = _StackStateMachine
from builtins import str
import com.badlogic.gdx.ai.fsm.DefaultStateMachine as _DefaultStateMachine
_DefaultStateMachine = _DefaultStateMachine
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pygdx.ai import msg
except ImportError:
    msg = _import_once("pygdx.ai.msg")

import com.badlogic.gdx.ai.fsm.State as _State
_State = _State
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StackStateMachine():
    """com.badlogic.gdx.ai.fsm.StackStateMachine"""
 
    @staticmethod
    def _wrap(java_value: _StackStateMachine) -> 'StackStateMachine':
        return StackStateMachine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StackStateMachine):
        """
        Dynamic initializer for StackStateMachine.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StackStateMachine__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StackStateMachine__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object, arg1: 'State'):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine(E,S)"""
        val = _StackStateMachine(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def setOwner(self, arg0: object):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setOwner(E)"""
        super(_DefaultStateMachine, self).setOwner(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def changeState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.StackStateMachine.changeState(S)"""
        super(_StackStateMachine, self).changeState(arg0)

    @override
    @overload
    def getGlobalState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.DefaultStateMachine.getGlobalState()"""
        return 'State'._wrap(super(DefaultStateMachine, self).getGlobalState())

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
    def revertToPreviousState(self) -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.StackStateMachine.revertToPreviousState()"""
        return bool._wrap(super(StackStateMachine, self).revertToPreviousState())

    @overload
    def __init__(self, arg0: object, arg1: 'State', arg2: 'State'):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine(E,S,S)"""
        val = _StackStateMachine(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.update()"""
        super(DefaultStateMachine, self).update()

    @overload
    def __init__(self, arg0: object):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine(E)"""
        val = _StackStateMachine(arg0)
        self.__wrapper = val

    @override
    @overload
    def setGlobalState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setGlobalState(S)"""
        super(_DefaultStateMachine, self).setGlobalState(arg0)

    @override
    @overload
    def getCurrentState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.StackStateMachine.getCurrentState()"""
        return 'State'._wrap(super(StackStateMachine, self).getCurrentState())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine()"""
        val = _StackStateMachine()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool._wrap(super(_DefaultStateMachine, self).handleMessage(arg0))

    @override
    @overload
    def getOwner(self) -> object:
        """public E com.badlogic.gdx.ai.fsm.DefaultStateMachine.getOwner()"""
        return object._wrap(super(DefaultStateMachine, self).getOwner())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine()"""
        val = _StackStateMachine()
        self.__wrapper = val

    @overload
    def isInState(self, arg0: 'State') -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.isInState(S)"""
        return bool._wrap(super(_DefaultStateMachine, self).isInState(arg0))

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
    def setInitialState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.StackStateMachine.setInitialState(S)"""
        super(_StackStateMachine, self).setInitialState(arg0)

    @override
    @overload
    def getPreviousState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.StackStateMachine.getPreviousState()"""
        return 'State'._wrap(super(StackStateMachine, self).getPreviousState())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())
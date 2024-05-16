from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from abc import abstractmethod, ABC
try:
    from pygdx.ai import msg
except ImportError:
    msg = __import_once__("pygdx.ai.msg")

import com.badlogic.gdx.ai.fsm.StateMachine as __StateMachine
__StateMachine = __StateMachine
 
class StateMachine(ABC):
    """com.badlogic.gdx.ai.fsm.StateMachine"""
 
    @staticmethod
    def __wrap(java_value: __StateMachine) -> 'StateMachine':
        return StateMachine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StateMachine):
        """
        Dynamic initializer for StateMachine.
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

 
 
 
# CLASS: com.badlogic.gdx.ai.fsm.StateMachine
from pyquantum_helper import import_once as __import_once__
from abc import abstractmethod, ABC
try:
    from pygdx.ai import msg
except ImportError:
    msg = __import_once__("pygdx.ai.msg")

import com.badlogic.gdx.ai.fsm.StateMachine as __StateMachine
__StateMachine = __StateMachine
 
class StateMachine(ABC):
    """com.badlogic.gdx.ai.fsm.StateMachine"""
 
    @staticmethod
    def __wrap(java_value: __StateMachine) -> 'StateMachine':
        return StateMachine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StateMachine):
        """
        Dynamic initializer for StateMachine.
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

 
 
 
# CLASS: com.badlogic.gdx.ai.fsm.StateMachine 
 
 
# CLASS: com.badlogic.gdx.ai.fsm.DefaultStateMachine
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pygdx.ai import msg
except ImportError:
    msg = __import_once__("pygdx.ai.msg")

import com.badlogic.gdx.ai.fsm.DefaultStateMachine as __DefaultStateMachine
__DefaultStateMachine = __DefaultStateMachine
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.fsm.State as __State
__State = __State
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DefaultStateMachine():
    """com.badlogic.gdx.ai.fsm.DefaultStateMachine"""
 
    @staticmethod
    def __wrap(java_value: __DefaultStateMachine) -> 'DefaultStateMachine':
        return DefaultStateMachine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultStateMachine):
        """
        Dynamic initializer for DefaultStateMachine.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine()"""
        val = __DefaultStateMachine()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine()"""
        val = __DefaultStateMachine()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setOwner(self, arg0: object):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setOwner(E)"""
        super(__DefaultStateMachine, self).setOwner(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setGlobalState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setGlobalState(S)"""
        super(__DefaultStateMachine, self).setGlobalState(arg0)

    @override
    @overload
    def setInitialState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setInitialState(S)"""
        super(__DefaultStateMachine, self).setInitialState(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.update()"""
        super(DefaultStateMachine, self).update()

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool.__wrap(super(__DefaultStateMachine, self).handleMessage(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'State'):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine(E,S)"""
        val = __DefaultStateMachine(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine(E)"""
        val = __DefaultStateMachine(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isInState(self, arg0: 'State') -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.isInState(S)"""
        return bool.__wrap(super(__DefaultStateMachine, self).isInState(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: 'State', arg2: 'State'):
        """public com.badlogic.gdx.ai.fsm.DefaultStateMachine(E,S,S)"""
        val = __DefaultStateMachine(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getGlobalState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.DefaultStateMachine.getGlobalState()"""
        return 'State'.__wrap(super(DefaultStateMachine, self).getGlobalState())

    @override
    @overload
    def revertToPreviousState(self) -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.revertToPreviousState()"""
        return bool.__wrap(super(DefaultStateMachine, self).revertToPreviousState())

    @overload
    def getOwner(self) -> object:
        """public E com.badlogic.gdx.ai.fsm.DefaultStateMachine.getOwner()"""
        return object.__wrap(super(DefaultStateMachine, self).getOwner())

    @override
    @overload
    def getPreviousState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.DefaultStateMachine.getPreviousState()"""
        return 'State'.__wrap(super(DefaultStateMachine, self).getPreviousState())

    @override
    @overload
    def getCurrentState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.DefaultStateMachine.getCurrentState()"""
        return 'State'.__wrap(super(DefaultStateMachine, self).getCurrentState())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def changeState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.changeState(S)"""
        super(__DefaultStateMachine, self).changeState(arg0)

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
 
 
# CLASS: com.badlogic.gdx.ai.fsm.State
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.fsm.State as __State
__State = __State
from abc import abstractmethod, ABC
try:
    from pygdx.ai import msg
except ImportError:
    msg = __import_once__("pygdx.ai.msg")

 
class State(ABC):
    """com.badlogic.gdx.ai.fsm.State"""
 
    @staticmethod
    def __wrap(java_value: __State) -> 'State':
        return State(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __State):
        """
        Dynamic initializer for State.
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
 
 
# CLASS: com.badlogic.gdx.ai.fsm.StackStateMachine
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
try:
    from pygdx.ai import msg
except ImportError:
    msg = __import_once__("pygdx.ai.msg")

import com.badlogic.gdx.ai.fsm.DefaultStateMachine as __DefaultStateMachine
__DefaultStateMachine = __DefaultStateMachine
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.fsm.State as __State
__State = __State
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.fsm.StackStateMachine as __StackStateMachine
__StackStateMachine = __StackStateMachine
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StackStateMachine():
    """com.badlogic.gdx.ai.fsm.StackStateMachine"""
 
    @staticmethod
    def __wrap(java_value: __StackStateMachine) -> 'StackStateMachine':
        return StackStateMachine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StackStateMachine):
        """
        Dynamic initializer for StackStateMachine.
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
    def setInitialState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.StackStateMachine.setInitialState(S)"""
        super(__StackStateMachine, self).setInitialState(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def revertToPreviousState(self) -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.StackStateMachine.revertToPreviousState()"""
        return bool.__wrap(super(StackStateMachine, self).revertToPreviousState())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: object):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine(E)"""
        val = __StackStateMachine(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getOwner(self) -> object:
        """public E com.badlogic.gdx.ai.fsm.DefaultStateMachine.getOwner()"""
        return object.__wrap(super(DefaultStateMachine, self).getOwner())

    @override
    @overload
    def setGlobalState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setGlobalState(S)"""
        super(__DefaultStateMachine, self).setGlobalState(arg0)

    @overload
    def __init__(self, arg0: object, arg1: 'State', arg2: 'State'):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine(E,S,S)"""
        val = __StackStateMachine(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def changeState(self, arg0: 'State'):
        """public void com.badlogic.gdx.ai.fsm.StackStateMachine.changeState(S)"""
        super(__StackStateMachine, self).changeState(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine()"""
        val = __StackStateMachine()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.update()"""
        super(DefaultStateMachine, self).update()

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool.__wrap(super(__DefaultStateMachine, self).handleMessage(arg0))

    @override
    @overload
    def setOwner(self, arg0: object):
        """public void com.badlogic.gdx.ai.fsm.DefaultStateMachine.setOwner(E)"""
        super(__DefaultStateMachine, self).setOwner(arg0)

    @overload
    def isInState(self, arg0: 'State') -> bool:
        """public boolean com.badlogic.gdx.ai.fsm.DefaultStateMachine.isInState(S)"""
        return bool.__wrap(super(__DefaultStateMachine, self).isInState(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getGlobalState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.DefaultStateMachine.getGlobalState()"""
        return 'State'.__wrap(super(DefaultStateMachine, self).getGlobalState())

    @overload
    def __init__(self, arg0: object, arg1: 'State'):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine(E,S)"""
        val = __StackStateMachine(arg0, arg1)
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
    def getPreviousState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.StackStateMachine.getPreviousState()"""
        return 'State'.__wrap(super(StackStateMachine, self).getPreviousState())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fsm.StackStateMachine()"""
        val = __StackStateMachine()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCurrentState(self) -> 'State':
        """public S com.badlogic.gdx.ai.fsm.StackStateMachine.getCurrentState()"""
        return 'State'.__wrap(super(StackStateMachine, self).getCurrentState())
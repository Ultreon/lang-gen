from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.ai.msg.TelegramProvider as _TelegramProvider
_TelegramProvider = _TelegramProvider
from abc import abstractmethod, ABC
 
class TelegramProvider():
    """com.badlogic.gdx.ai.msg.TelegramProvider"""
 
    @staticmethod
    def _wrap(java_value: _TelegramProvider) -> 'TelegramProvider':
        return TelegramProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TelegramProvider):
        """
        Dynamic initializer for TelegramProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TelegramProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TelegramProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def provideMessageInfo(self, arg0: int, arg1: 'Telegraph'):
        """public abstract java.lang.Object com.badlogic.gdx.ai.msg.TelegramProvider.provideMessageInfo(int,com.badlogic.gdx.ai.msg.Telegraph)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.msg.TelegramProvider
import com.badlogic.gdx.ai.msg.TelegramProvider as _TelegramProvider
_TelegramProvider = _TelegramProvider
from abc import abstractmethod, ABC
 
class TelegramProvider():
    """com.badlogic.gdx.ai.msg.TelegramProvider"""
 
    @staticmethod
    def _wrap(java_value: _TelegramProvider) -> 'TelegramProvider':
        return TelegramProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TelegramProvider):
        """
        Dynamic initializer for TelegramProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TelegramProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TelegramProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def provideMessageInfo(self, arg0: int, arg1: 'Telegraph'):
        """public abstract java.lang.Object com.badlogic.gdx.ai.msg.TelegramProvider.provideMessageInfo(int,com.badlogic.gdx.ai.msg.Telegraph)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.msg.TelegramProvider 
 
 
# CLASS: com.badlogic.gdx.ai.msg.PriorityQueue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Comparable as Comparable
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.ai.msg.PriorityQueue as _PriorityQueue
_PriorityQueue = _PriorityQueue
import java.lang.Comparable as _Comparable
_Comparable = _Comparable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PriorityQueue():
    """com.badlogic.gdx.ai.msg.PriorityQueue"""
 
    @staticmethod
    def _wrap(java_value: _PriorityQueue) -> 'PriorityQueue':
        return PriorityQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PriorityQueue):
        """
        Dynamic initializer for PriorityQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PriorityQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PriorityQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def peek(self) -> 'Comparable':
        """public E com.badlogic.gdx.ai.msg.PriorityQueue.peek()"""
        return 'Comparable'._wrap(super(PriorityQueue, self).peek())

    @overload
    def poll(self) -> 'Comparable':
        """public E com.badlogic.gdx.ai.msg.PriorityQueue.poll()"""
        return 'Comparable'._wrap(super(PriorityQueue, self).poll())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setUniqueness(self, arg0: bool):
        """public void com.badlogic.gdx.ai.msg.PriorityQueue.setUniqueness(boolean)"""
        super(_PriorityQueue, self).setUniqueness(_boolean.valueOf(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.msg.PriorityQueue.clear()"""
        super(PriorityQueue, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Comparable') -> bool:
        """public boolean com.badlogic.gdx.ai.msg.PriorityQueue.add(E)"""
        return bool._wrap(super(_PriorityQueue, self).add(arg0))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.msg.PriorityQueue()"""
        val = _PriorityQueue()
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'Comparable':
        """public E com.badlogic.gdx.ai.msg.PriorityQueue.get(int)"""
        return 'Comparable'._wrap(super(_PriorityQueue, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getUniqueness(self) -> bool:
        """public boolean com.badlogic.gdx.ai.msg.PriorityQueue.getUniqueness()"""
        return bool._wrap(super(PriorityQueue, self).getUniqueness())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.msg.PriorityQueue(int)"""
        val = _PriorityQueue(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.ai.msg.PriorityQueue.size()"""
        return int._wrap(super(PriorityQueue, self).size())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.msg.PriorityQueue()"""
        val = _PriorityQueue()
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
 
 
# CLASS: com.badlogic.gdx.ai.msg.Telegraph
import com.badlogic.gdx.ai.msg.Telegraph as _Telegraph
_Telegraph = _Telegraph
from abc import abstractmethod, ABC
 
class Telegraph():
    """com.badlogic.gdx.ai.msg.Telegraph"""
 
    @staticmethod
    def _wrap(java_value: _Telegraph) -> 'Telegraph':
        return Telegraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Telegraph):
        """
        Dynamic initializer for Telegraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Telegraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Telegraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def handleMessage(self, arg0: 'Telegram'):
        """public abstract boolean com.badlogic.gdx.ai.msg.Telegraph.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.msg.MessageManager
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.msg.MessageManager as _MessageManager
_MessageManager = _MessageManager
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.ai.msg.MessageDispatcher as _MessageDispatcher
_MessageDispatcher = _MessageDispatcher
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MessageManager():
    """com.badlogic.gdx.ai.msg.MessageManager"""
 
    @staticmethod
    def _wrap(java_value: _MessageManager) -> 'MessageManager':
        return MessageManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageManager):
        """
        Dynamic initializer for MessageManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clearListeners(self, *arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners(int...)"""
        super(_MessageDispatcher, self).clearListeners(arg0)

    @override
    @overload
    def clearProviders(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders()"""
        super(MessageDispatcher, self).clearProviders()

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), arg4)

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: object, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, _int.valueOf(arg1), arg2, _boolean.valueOf(arg3))

    @override
    @overload
    def addProvider(self, arg0: 'TelegramProvider', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addProvider(com.badlogic.gdx.ai.msg.TelegramProvider,int)"""
        super(_MessageDispatcher, self).addProvider(arg0, _int.valueOf(arg1))

    @override
    @overload
    def addProviders(self, arg0: 'TelegramProvider', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addProviders(com.badlogic.gdx.ai.msg.TelegramProvider,int...)"""
        super(_MessageDispatcher, self).addProviders(arg0, arg1)

    @override
    @overload
    def addListeners(self, arg0: 'Telegraph', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addListeners(com.badlogic.gdx.ai.msg.Telegraph,int...)"""
        super(_MessageDispatcher, self).addListeners(arg0, arg1)

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.msg.MessageDispatcher.isDebugEnabled()"""
        return bool._wrap(super(MessageDispatcher, self).isDebugEnabled())

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: object, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _boolean.valueOf(arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, arg2, _int.valueOf(arg3))

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
    def clearQueue(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearQueue()"""
        super(MessageDispatcher, self).clearQueue()

    @override
    @overload
    def clearProviders(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders(int)"""
        super(_MessageDispatcher, self).clearProviders(_int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2))

    @staticmethod
    @overload
    def getInstance() -> 'MessageManager':
        """public static com.badlogic.gdx.ai.msg.MessageManager com.badlogic.gdx.ai.msg.MessageManager.getInstance()"""
        return MessageManager._wrap(_MessageManager.getInstance())

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, _int.valueOf(arg1), arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.update()"""
        super(MessageDispatcher, self).update()

    @override
    @overload
    def addListener(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addListener(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).addListener(arg0, _int.valueOf(arg1))

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, arg1, _int.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), _boolean.valueOf(arg4))

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, arg1, _int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def scanQueue(self, arg0: 'PendingMessageCallback'):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.scanQueue(com.badlogic.gdx.ai.msg.MessageDispatcher$PendingMessageCallback)"""
        super(_MessageDispatcher, self).scanQueue(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: int, arg2: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), _int.valueOf(arg1), arg2)

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: object, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, arg1, _int.valueOf(arg2), arg3, _boolean.valueOf(arg4))

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.msg.MessageDispatcher.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool._wrap(super(_MessageDispatcher, self).handleMessage(arg0))

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, _int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clear()"""
        super(MessageDispatcher, self).clear()

    @override
    @overload
    def dispatchMessage(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(int)"""
        super(_MessageDispatcher, self).dispatchMessage(_int.valueOf(arg0))

    @override
    @overload
    def setDebugEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.setDebugEnabled(boolean)"""
        super(_MessageDispatcher, self).setDebugEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, _int.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,int)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def clearListeners(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners(int)"""
        super(_MessageDispatcher, self).clearListeners(_int.valueOf(arg0))

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, _int.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def clearProviders(self, *arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders(int...)"""
        super(_MessageDispatcher, self).clearProviders(arg0)

    @override
    @overload
    def removeListener(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.removeListener(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).removeListener(arg0, _int.valueOf(arg1))

    @override
    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners()"""
        super(MessageDispatcher, self).clearListeners()

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object, arg5: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @override
    @overload
    def dispatchMessage(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(_int.valueOf(arg0), arg1)

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, arg1, _int.valueOf(arg2), arg3)

    @override
    @overload
    def removeListener(self, arg0: 'Telegraph', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.removeListener(com.badlogic.gdx.ai.msg.Telegraph,int...)"""
        super(_MessageDispatcher, self).removeListener(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass()) 
 
 
# CLASS: com.badlogic.gdx.ai.msg.MessageDispatcher
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.ai.msg.MessageDispatcher as _MessageDispatcher
_MessageDispatcher = _MessageDispatcher
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MessageDispatcher():
    """com.badlogic.gdx.ai.msg.MessageDispatcher"""
 
    @staticmethod
    def _wrap(java_value: _MessageDispatcher) -> 'MessageDispatcher':
        return MessageDispatcher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageDispatcher):
        """
        Dynamic initializer for MessageDispatcher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageDispatcher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageDispatcher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), _boolean.valueOf(arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.msg.MessageDispatcher()"""
        val = _MessageDispatcher()
        self.__wrapper = val

    @overload
    def dispatchMessage(self, arg0: float, arg1: int, arg2: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def dispatchMessage(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(_int.valueOf(arg0), arg1)

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: object, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, arg1, _int.valueOf(arg2), arg3, _boolean.valueOf(arg4))

    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners()"""
        super(MessageDispatcher, self).clearListeners()

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: object, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _boolean.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.msg.MessageDispatcher()"""
        val = _MessageDispatcher()
        self.__wrapper = val

    @overload
    def addListeners(self, arg0: 'Telegraph', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addListeners(com.badlogic.gdx.ai.msg.Telegraph,int...)"""
        super(_MessageDispatcher, self).addListeners(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def dispatchMessage(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(int)"""
        super(_MessageDispatcher, self).dispatchMessage(_int.valueOf(arg0))

    @overload
    def addProvider(self, arg0: 'TelegramProvider', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addProvider(com.badlogic.gdx.ai.msg.TelegramProvider,int)"""
        super(_MessageDispatcher, self).addProvider(arg0, _int.valueOf(arg1))

    @overload
    def removeListener(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.removeListener(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).removeListener(arg0, _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def clearListeners(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners(int)"""
        super(_MessageDispatcher, self).clearListeners(_int.valueOf(arg0))

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, _int.valueOf(arg2), arg3)

    @overload
    def clearListeners(self, *arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners(int...)"""
        super(_MessageDispatcher, self).clearListeners(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def addProviders(self, arg0: 'TelegramProvider', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addProviders(com.badlogic.gdx.ai.msg.TelegramProvider,int...)"""
        super(_MessageDispatcher, self).addProviders(arg0, arg1)

    @overload
    def update(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.update()"""
        super(MessageDispatcher, self).update()

    @overload
    def setDebugEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.setDebugEnabled(boolean)"""
        super(_MessageDispatcher, self).setDebugEnabled(_boolean.valueOf(arg0))

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, arg2, _int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dispatchMessage(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,int)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.msg.MessageDispatcher.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool._wrap(super(_MessageDispatcher, self).handleMessage(arg0))

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, _int.valueOf(arg2), _boolean.valueOf(arg3))

    @overload
    def scanQueue(self, arg0: 'PendingMessageCallback'):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.scanQueue(com.badlogic.gdx.ai.msg.MessageDispatcher$PendingMessageCallback)"""
        super(_MessageDispatcher, self).scanQueue(arg0)

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: object, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, _int.valueOf(arg1), arg2, _boolean.valueOf(arg3))

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, arg1, _int.valueOf(arg2))

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object, arg5: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, _int.valueOf(arg1))

    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.msg.MessageDispatcher.isDebugEnabled()"""
        return bool._wrap(super(MessageDispatcher, self).isDebugEnabled())

    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clear()"""
        super(MessageDispatcher, self).clear()

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, arg1, _int.valueOf(arg2), arg3)

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, _int.valueOf(arg2))

    @overload
    def removeListener(self, arg0: 'Telegraph', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.removeListener(com.badlogic.gdx.ai.msg.Telegraph,int...)"""
        super(_MessageDispatcher, self).removeListener(arg0, arg1)

    @overload
    def clearQueue(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearQueue()"""
        super(MessageDispatcher, self).clearQueue()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addListener(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addListener(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(_MessageDispatcher, self).addListener(arg0, _int.valueOf(arg1))

    @overload
    def clearProviders(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders(int)"""
        super(_MessageDispatcher, self).clearProviders(_int.valueOf(arg0))

    @overload
    def clearProviders(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders()"""
        super(MessageDispatcher, self).clearProviders()

    @overload
    def clearProviders(self, *arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders(int...)"""
        super(_MessageDispatcher, self).clearProviders(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(_float.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), arg4)

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, arg1, _int.valueOf(arg2), _boolean.valueOf(arg3))

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, _int.valueOf(arg1), arg2)

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(_MessageDispatcher, self).dispatchMessage(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2)) 
 
 
# CLASS: com.badlogic.gdx.ai.msg.Telegram
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.ai.msg.Telegram as _Telegram
_Telegram = _Telegram
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Telegram():
    """com.badlogic.gdx.ai.msg.Telegram"""
 
    @staticmethod
    def _wrap(java_value: _Telegram) -> 'Telegram':
        return Telegram(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Telegram):
        """
        Dynamic initializer for Telegram.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Telegram__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Telegram__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.ai.msg.Telegram.equals(java.lang.Object)"""
        return bool._wrap(super(_Telegram, self).equals(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.msg.Telegram.reset()"""
        super(Telegram, self).reset()

    @overload
    def getTimestamp(self) -> float:
        """public float com.badlogic.gdx.ai.msg.Telegram.getTimestamp()"""
        return float._wrap(super(Telegram, self).getTimestamp())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.msg.Telegram()"""
        val = _Telegram()
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setTimestamp(self, arg0: float):
        """public void com.badlogic.gdx.ai.msg.Telegram.setTimestamp(float)"""
        super(_Telegram, self).setTimestamp(_float.valueOf(arg0))

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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.ai.msg.Telegram.hashCode()"""
        return int._wrap(super(Telegram, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Telegram') -> int:
        """public int com.badlogic.gdx.ai.msg.Telegram.compareTo(com.badlogic.gdx.ai.msg.Telegram)"""
        return int._wrap(super(_Telegram, self).compareTo(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.msg.Telegram()"""
        val = _Telegram()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.msg.MessageDispatcher$PendingMessageCallback
import com.badlogic.gdx.ai.msg.MessageDispatcher as _MessageDispatcher_PendingMessageCallback
_PendingMessageCallback = _MessageDispatcher_PendingMessageCallback.PendingMessageCallback
from abc import abstractmethod, ABC
 
class PendingMessageCallback():
    """com.badlogic.gdx.ai.msg.MessageDispatcher.PendingMessageCallback"""
 
    @staticmethod
    def _wrap(java_value: _PendingMessageCallback) -> 'PendingMessageCallback':
        return PendingMessageCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PendingMessageCallback):
        """
        Dynamic initializer for PendingMessageCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PendingMessageCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PendingMessageCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def report(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object, arg5: int):
        """public abstract void com.badlogic.gdx.ai.msg.MessageDispatcher$PendingMessageCallback.report(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,int)"""
        pass
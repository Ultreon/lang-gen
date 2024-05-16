from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.msg.Telegram as __Telegram
__Telegram = __Telegram
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
 
class Telegram():
    """com.badlogic.gdx.ai.msg.Telegram"""
 
    @staticmethod
    def __wrap(java_value: __Telegram) -> 'Telegram':
        return Telegram(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Telegram):
        """
        Dynamic initializer for Telegram.
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
    def compareTo(self, arg0: 'Telegram') -> int:
        """public int com.badlogic.gdx.ai.msg.Telegram.compareTo(com.badlogic.gdx.ai.msg.Telegram)"""
        return int.__wrap(super(__Telegram, self).compareTo(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.msg.Telegram.reset()"""
        super(Telegram, self).reset()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setTimestamp(self, arg0: float):
        """public void com.badlogic.gdx.ai.msg.Telegram.setTimestamp(float)"""
        super(__Telegram, self).setTimestamp(__float.valueOf(arg0))

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
    def __init__(self):
        """public com.badlogic.gdx.ai.msg.Telegram()"""
        val = __Telegram()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.ai.msg.Telegram.hashCode()"""
        return int.__wrap(super(Telegram, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.msg.Telegram()"""
        val = __Telegram()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTimestamp(self) -> float:
        """public float com.badlogic.gdx.ai.msg.Telegram.getTimestamp()"""
        return float.__wrap(super(Telegram, self).getTimestamp())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.ai.msg.Telegram.equals(java.lang.Object)"""
        return bool.__wrap(super(__Telegram, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.ai.msg.Telegram
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.msg.Telegram as __Telegram
__Telegram = __Telegram
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
 
class Telegram():
    """com.badlogic.gdx.ai.msg.Telegram"""
 
    @staticmethod
    def __wrap(java_value: __Telegram) -> 'Telegram':
        return Telegram(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Telegram):
        """
        Dynamic initializer for Telegram.
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
    def compareTo(self, arg0: 'Telegram') -> int:
        """public int com.badlogic.gdx.ai.msg.Telegram.compareTo(com.badlogic.gdx.ai.msg.Telegram)"""
        return int.__wrap(super(__Telegram, self).compareTo(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.msg.Telegram.reset()"""
        super(Telegram, self).reset()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setTimestamp(self, arg0: float):
        """public void com.badlogic.gdx.ai.msg.Telegram.setTimestamp(float)"""
        super(__Telegram, self).setTimestamp(__float.valueOf(arg0))

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
    def __init__(self):
        """public com.badlogic.gdx.ai.msg.Telegram()"""
        val = __Telegram()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.ai.msg.Telegram.hashCode()"""
        return int.__wrap(super(Telegram, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.msg.Telegram()"""
        val = __Telegram()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTimestamp(self) -> float:
        """public float com.badlogic.gdx.ai.msg.Telegram.getTimestamp()"""
        return float.__wrap(super(Telegram, self).getTimestamp())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.ai.msg.Telegram.equals(java.lang.Object)"""
        return bool.__wrap(super(__Telegram, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.ai.msg.Telegram 
 
 
# CLASS: com.badlogic.gdx.ai.msg.TelegramProvider
import com.badlogic.gdx.ai.msg.TelegramProvider as __TelegramProvider
__TelegramProvider = __TelegramProvider
from abc import abstractmethod, ABC
 
class TelegramProvider(ABC):
    """com.badlogic.gdx.ai.msg.TelegramProvider"""
 
    @staticmethod
    def __wrap(java_value: __TelegramProvider) -> 'TelegramProvider':
        return TelegramProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TelegramProvider):
        """
        Dynamic initializer for TelegramProvider.
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
    def provideMessageInfo(self, arg0: int, arg1: 'Telegraph'):
        """public abstract java.lang.Object com.badlogic.gdx.ai.msg.TelegramProvider.provideMessageInfo(int,com.badlogic.gdx.ai.msg.Telegraph)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.msg.Telegraph
import com.badlogic.gdx.ai.msg.Telegraph as __Telegraph
__Telegraph = __Telegraph
from abc import abstractmethod, ABC
 
class Telegraph(ABC):
    """com.badlogic.gdx.ai.msg.Telegraph"""
 
    @staticmethod
    def __wrap(java_value: __Telegraph) -> 'Telegraph':
        return Telegraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Telegraph):
        """
        Dynamic initializer for Telegraph.
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
    def handleMessage(self, arg0: 'Telegram'):
        """public abstract boolean com.badlogic.gdx.ai.msg.Telegraph.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.msg.MessageDispatcher$PendingMessageCallback
import com.badlogic.gdx.ai.msg.MessageDispatcher as __MessageDispatcher_PendingMessageCallback
__PendingMessageCallback = __MessageDispatcher_PendingMessageCallback.PendingMessageCallback
from abc import abstractmethod, ABC
 
class PendingMessageCallback(ABC):
    """com.badlogic.gdx.ai.msg.MessageDispatcher.PendingMessageCallback"""
 
    @staticmethod
    def __wrap(java_value: __PendingMessageCallback) -> 'PendingMessageCallback':
        return PendingMessageCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PendingMessageCallback):
        """
        Dynamic initializer for PendingMessageCallback.
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
    def report(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object, arg5: int):
        """public abstract void com.badlogic.gdx.ai.msg.MessageDispatcher$PendingMessageCallback.report(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.msg.MessageManager
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.msg.MessageDispatcher as __MessageDispatcher
__MessageDispatcher = __MessageDispatcher
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.msg.MessageManager as __MessageManager
__MessageManager = __MessageManager
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MessageManager():
    """com.badlogic.gdx.ai.msg.MessageManager"""
 
    @staticmethod
    def __wrap(java_value: __MessageManager) -> 'MessageManager':
        return MessageManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageManager):
        """
        Dynamic initializer for MessageManager.
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
    def clearProviders(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders()"""
        super(MessageDispatcher, self).clearProviders()

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: int, arg2: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), __int.valueOf(arg1), arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object, arg5: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), arg4, __boolean.valueOf(arg5))

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
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, __int.valueOf(arg1), arg2)

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), __boolean.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setDebugEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.setDebugEnabled(boolean)"""
        super(__MessageDispatcher, self).setDebugEnabled(__boolean.valueOf(arg0))

    @override
    @overload
    def removeListener(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.removeListener(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).removeListener(arg0, __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.msg.MessageDispatcher.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool.__wrap(super(__MessageDispatcher, self).handleMessage(arg0))

    @override
    @overload
    def clearProviders(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders(int)"""
        super(__MessageDispatcher, self).clearProviders(__int.valueOf(arg0))

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, __int.valueOf(arg2), arg3)

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: object, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, __int.valueOf(arg1), arg2, __boolean.valueOf(arg3))

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.update()"""
        super(MessageDispatcher, self).update()

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,int)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, __int.valueOf(arg2), __boolean.valueOf(arg3))

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: object, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __boolean.valueOf(arg4))

    @override
    @overload
    def scanQueue(self, arg0: 'PendingMessageCallback'):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.scanQueue(com.badlogic.gdx.ai.msg.MessageDispatcher$PendingMessageCallback)"""
        super(__MessageDispatcher, self).scanQueue(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, __int.valueOf(arg1))

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: object, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, arg1, __int.valueOf(arg2), arg3, __boolean.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.msg.MessageDispatcher.isDebugEnabled()"""
        return bool.__wrap(super(MessageDispatcher, self).isDebugEnabled())

    @override
    @overload
    def addListeners(self, arg0: 'Telegraph', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addListeners(com.badlogic.gdx.ai.msg.Telegraph,int...)"""
        super(__MessageDispatcher, self).addListeners(arg0, arg1)

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, arg1, __int.valueOf(arg2), __boolean.valueOf(arg3))

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clear()"""
        super(MessageDispatcher, self).clear()

    @override
    @overload
    def addProvider(self, arg0: 'TelegramProvider', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addProvider(com.badlogic.gdx.ai.msg.TelegramProvider,int)"""
        super(__MessageDispatcher, self).addProvider(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def getInstance() -> 'MessageManager':
        """public static com.badlogic.gdx.ai.msg.MessageManager com.badlogic.gdx.ai.msg.MessageManager.getInstance()"""
        return MessageManager.__wrap(__MessageManager.getInstance())

    @override
    @overload
    def dispatchMessage(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(__int.valueOf(arg0), arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, arg1, __int.valueOf(arg2), arg3)

    @override
    @overload
    def addProviders(self, arg0: 'TelegramProvider', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addProviders(com.badlogic.gdx.ai.msg.TelegramProvider,int...)"""
        super(__MessageDispatcher, self).addProviders(arg0, arg1)

    @override
    @overload
    def dispatchMessage(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(int)"""
        super(__MessageDispatcher, self).dispatchMessage(__int.valueOf(arg0))

    @override
    @overload
    def clearProviders(self, *arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders(int...)"""
        super(__MessageDispatcher, self).clearProviders(arg0)

    @override
    @overload
    def addListener(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addListener(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).addListener(arg0, __int.valueOf(arg1))

    @override
    @overload
    def removeListener(self, arg0: 'Telegraph', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.removeListener(com.badlogic.gdx.ai.msg.Telegraph,int...)"""
        super(__MessageDispatcher, self).removeListener(arg0, arg1)

    @override
    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners()"""
        super(MessageDispatcher, self).clearListeners()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, arg2, __int.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), arg4)

    @override
    @overload
    def clearListeners(self, *arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners(int...)"""
        super(__MessageDispatcher, self).clearListeners(arg0)

    @override
    @overload
    def clearListeners(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners(int)"""
        super(__MessageDispatcher, self).clearListeners(__int.valueOf(arg0))

    @override
    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, arg1, __int.valueOf(arg2)) 
 
 
# CLASS: com.badlogic.gdx.ai.msg.MessageDispatcher
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.msg.MessageDispatcher as __MessageDispatcher
__MessageDispatcher = __MessageDispatcher
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
 
class MessageDispatcher():
    """com.badlogic.gdx.ai.msg.MessageDispatcher"""
 
    @staticmethod
    def __wrap(java_value: __MessageDispatcher) -> 'MessageDispatcher':
        return MessageDispatcher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageDispatcher):
        """
        Dynamic initializer for MessageDispatcher.
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
    def removeListener(self, arg0: 'Telegraph', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.removeListener(com.badlogic.gdx.ai.msg.Telegraph,int...)"""
        super(__MessageDispatcher, self).removeListener(arg0, arg1)

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, __int.valueOf(arg2))

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, arg1, __int.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def addProvider(self, arg0: 'TelegramProvider', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addProvider(com.badlogic.gdx.ai.msg.TelegramProvider,int)"""
        super(__MessageDispatcher, self).addProvider(arg0, __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: object, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, arg1, __int.valueOf(arg2), arg3, __boolean.valueOf(arg4))

    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners()"""
        super(MessageDispatcher, self).clearListeners()

    @overload
    def addListener(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addListener(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).addListener(arg0, __int.valueOf(arg1))

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: object, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __boolean.valueOf(arg4))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, arg1, __int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def clearListeners(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners(int)"""
        super(__MessageDispatcher, self).clearListeners(__int.valueOf(arg0))

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, arg2, __int.valueOf(arg3))

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.msg.MessageDispatcher.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool.__wrap(super(__MessageDispatcher, self).handleMessage(arg0))

    @overload
    def clearListeners(self, *arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearListeners(int...)"""
        super(__MessageDispatcher, self).clearListeners(arg0)

    @overload
    def scanQueue(self, arg0: 'PendingMessageCallback'):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.scanQueue(com.badlogic.gdx.ai.msg.MessageDispatcher$PendingMessageCallback)"""
        super(__MessageDispatcher, self).scanQueue(arg0)

    @overload
    def update(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.update()"""
        super(MessageDispatcher, self).update()

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), arg4)

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), __boolean.valueOf(arg4))

    @overload
    def addListeners(self, arg0: 'Telegraph', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addListeners(com.badlogic.gdx.ai.msg.Telegraph,int...)"""
        super(__MessageDispatcher, self).addListeners(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: object, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, __int.valueOf(arg1), arg2, __boolean.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def dispatchMessage(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(int)"""
        super(__MessageDispatcher, self).dispatchMessage(__int.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.msg.MessageDispatcher()"""
        val = __MessageDispatcher()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, __int.valueOf(arg1))

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: 'Telegraph', arg2: int, arg3: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, arg1, __int.valueOf(arg2), arg3)

    @overload
    def clearProviders(self, arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders(int)"""
        super(__MessageDispatcher, self).clearProviders(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def dispatchMessage(self, arg0: int, arg1: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(__int.valueOf(arg0), arg1)

    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clear()"""
        super(MessageDispatcher, self).clear()

    @overload
    def clearProviders(self, *arg0: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders(int...)"""
        super(__MessageDispatcher, self).clearProviders(arg0)

    @overload
    def dispatchMessage(self, arg0: float, arg1: int, arg2: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), __int.valueOf(arg1), arg2)

    @overload
    def dispatchMessage(self, arg0: float, arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,int)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, __int.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2))

    @overload
    def setDebugEnabled(self, arg0: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.setDebugEnabled(boolean)"""
        super(__MessageDispatcher, self).setDebugEnabled(__boolean.valueOf(arg0))

    @overload
    def dispatchMessage(self, arg0: 'Telegraph', arg1: int, arg2: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(arg0, __int.valueOf(arg1), arg2)

    @overload
    def removeListener(self, arg0: 'Telegraph', arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.removeListener(com.badlogic.gdx.ai.msg.Telegraph,int)"""
        super(__MessageDispatcher, self).removeListener(arg0, __int.valueOf(arg1))

    @overload
    def clearQueue(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearQueue()"""
        super(MessageDispatcher, self).clearQueue()

    @overload
    def addProviders(self, arg0: 'TelegramProvider', *arg1: int):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.addProviders(com.badlogic.gdx.ai.msg.TelegramProvider,int...)"""
        super(__MessageDispatcher, self).addProviders(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def clearProviders(self):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.clearProviders()"""
        super(MessageDispatcher, self).clearProviders()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: 'Telegraph', arg3: int, arg4: object, arg5: bool):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object,boolean)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.ai.msg.MessageDispatcher.isDebugEnabled()"""
        return bool.__wrap(super(MessageDispatcher, self).isDebugEnabled())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.msg.MessageDispatcher()"""
        val = __MessageDispatcher()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dispatchMessage(self, arg0: float, arg1: 'Telegraph', arg2: int, arg3: object):
        """public void com.badlogic.gdx.ai.msg.MessageDispatcher.dispatchMessage(float,com.badlogic.gdx.ai.msg.Telegraph,int,java.lang.Object)"""
        super(__MessageDispatcher, self).dispatchMessage(__float.valueOf(arg0), arg1, __int.valueOf(arg2), arg3) 
 
 
# CLASS: com.badlogic.gdx.ai.msg.PriorityQueue
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.msg.PriorityQueue as __PriorityQueue
__PriorityQueue = __PriorityQueue
import java.lang.Comparable as Comparable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Comparable as __Comparable
__Comparable = __Comparable
from builtins import int
 
class PriorityQueue():
    """com.badlogic.gdx.ai.msg.PriorityQueue"""
 
    @staticmethod
    def __wrap(java_value: __PriorityQueue) -> 'PriorityQueue':
        return PriorityQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PriorityQueue):
        """
        Dynamic initializer for PriorityQueue.
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
    def get(self, arg0: int) -> 'Comparable':
        """public E com.badlogic.gdx.ai.msg.PriorityQueue.get(int)"""
        return 'Comparable'.__wrap(super(__PriorityQueue, self).get(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.msg.PriorityQueue(int)"""
        val = __PriorityQueue(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.msg.PriorityQueue()"""
        val = __PriorityQueue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.ai.msg.PriorityQueue.size()"""
        return int.__wrap(super(PriorityQueue, self).size())

    @overload
    def getUniqueness(self) -> bool:
        """public boolean com.badlogic.gdx.ai.msg.PriorityQueue.getUniqueness()"""
        return bool.__wrap(super(PriorityQueue, self).getUniqueness())

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.msg.PriorityQueue()"""
        val = __PriorityQueue()
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setUniqueness(self, arg0: bool):
        """public void com.badlogic.gdx.ai.msg.PriorityQueue.setUniqueness(boolean)"""
        super(__PriorityQueue, self).setUniqueness(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def add(self, arg0: 'Comparable') -> bool:
        """public boolean com.badlogic.gdx.ai.msg.PriorityQueue.add(E)"""
        return bool.__wrap(super(__PriorityQueue, self).add(arg0))

    @overload
    def poll(self) -> 'Comparable':
        """public E com.badlogic.gdx.ai.msg.PriorityQueue.poll()"""
        return 'Comparable'.__wrap(super(PriorityQueue, self).poll())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def peek(self) -> 'Comparable':
        """public E com.badlogic.gdx.ai.msg.PriorityQueue.peek()"""
        return 'Comparable'.__wrap(super(PriorityQueue, self).peek())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))
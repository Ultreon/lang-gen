from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import com.badlogic.gdx.ai.btree.TaskCloneException as __TaskCloneException
__TaskCloneException = __TaskCloneException
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TaskCloneException():
    """com.badlogic.gdx.ai.btree.TaskCloneException"""
 
    @staticmethod
    def __wrap(java_value: __TaskCloneException) -> 'TaskCloneException':
        return TaskCloneException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TaskCloneException):
        """
        Dynamic initializer for TaskCloneException.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.TaskCloneException(java.lang.String)"""
        val = __TaskCloneException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.TaskCloneException(java.lang.String,java.lang.Throwable)"""
        val = __TaskCloneException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.TaskCloneException()"""
        val = __TaskCloneException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.TaskCloneException(java.lang.Throwable)"""
        val = __TaskCloneException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.TaskCloneException()"""
        val = __TaskCloneException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.TaskCloneException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import com.badlogic.gdx.ai.btree.TaskCloneException as __TaskCloneException
__TaskCloneException = __TaskCloneException
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TaskCloneException():
    """com.badlogic.gdx.ai.btree.TaskCloneException"""
 
    @staticmethod
    def __wrap(java_value: __TaskCloneException) -> 'TaskCloneException':
        return TaskCloneException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TaskCloneException):
        """
        Dynamic initializer for TaskCloneException.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.TaskCloneException(java.lang.String)"""
        val = __TaskCloneException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.TaskCloneException(java.lang.String,java.lang.Throwable)"""
        val = __TaskCloneException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.TaskCloneException()"""
        val = __TaskCloneException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.TaskCloneException(java.lang.Throwable)"""
        val = __TaskCloneException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.TaskCloneException()"""
        val = __TaskCloneException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.TaskCloneException 
 
 
# CLASS: com.badlogic.gdx.ai.btree.TaskCloner
import com.badlogic.gdx.ai.btree.TaskCloner as __TaskCloner
__TaskCloner = __TaskCloner
from abc import abstractmethod, ABC
 
class TaskCloner(ABC):
    """com.badlogic.gdx.ai.btree.TaskCloner"""
 
    @staticmethod
    def __wrap(java_value: __TaskCloner) -> 'TaskCloner':
        return TaskCloner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TaskCloner):
        """
        Dynamic initializer for TaskCloner.
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
    def cloneTask(self, arg0: 'Task'):
        """public abstract <T> com.badlogic.gdx.ai.btree.Task<T> com.badlogic.gdx.ai.btree.TaskCloner.cloneTask(com.badlogic.gdx.ai.btree.Task<T>)"""
        pass

    @abstractmethod
    def freeTask(self, arg0: 'Task'):
        """public abstract <T> void com.badlogic.gdx.ai.btree.TaskCloner.freeTask(com.badlogic.gdx.ai.btree.Task<T>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.btree.Task
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
from abc import abstractmethod, ABC
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Task(ABC):
    """com.badlogic.gdx.ai.btree.Task"""
 
    @staticmethod
    def __wrap(java_value: __Task) -> 'Task':
        return Task(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Task):
        """
        Dynamic initializer for Task.
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
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(Task, self).getObject())

    @abstractmethod
    def getChild(self, arg0: int):
        """public abstract com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getChild(int)"""
        pass

    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'.__wrap(super(Task, self).getStatus())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def getChildCount(self, ):
        """public abstract int com.badlogic.gdx.ai.btree.Task.getChildCount()"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(Task, self).start()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.Task()"""
        val = __Task()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setControl(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__Task, self).addChild(arg0))

    @abstractmethod
    def run(self, ):
        """public abstract void com.badlogic.gdx.ai.btree.Task.run()"""
        pass

    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setGuard(arg0)

    @abstractmethod
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @abstractmethod
    def childFail(self, arg0: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__Task, self).checkGuard(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Task.reset()"""
        super(Task, self).reset()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.Task()"""
        val = __Task()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def childSuccess(self, arg0: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'.__wrap(super(Task, self).getGuard())

    @overload
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'.__wrap(super(Task, self).cloneTask())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.btree.BehaviorTree
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.btree.BehaviorTree as __BehaviorTree
__BehaviorTree = __BehaviorTree
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BehaviorTree():
    """com.badlogic.gdx.ai.btree.BehaviorTree"""
 
    @staticmethod
    def __wrap(java_value: __BehaviorTree) -> 'BehaviorTree':
        return BehaviorTree(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BehaviorTree):
        """
        Dynamic initializer for BehaviorTree.
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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.BehaviorTree()"""
        val = __BehaviorTree()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'.__wrap(super(Task, self).cloneTask())

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @overload
    def addListener(self, arg0: 'Listener'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.addListener(com.badlogic.gdx.ai.btree.BehaviorTree$Listener<E>)"""
        super(__BehaviorTree, self).addListener(arg0)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(Task, self).start()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BehaviorTree.getChildCount()"""
        return int.__wrap(super(BehaviorTree, self).getChildCount())

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__BehaviorTree, self).childSuccess(arg0)

    @overload
    def notifyChildAdded(self, arg0: 'Task', arg1: int):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.notifyChildAdded(com.badlogic.gdx.ai.btree.Task<E>,int)"""
        super(__BehaviorTree, self).notifyChildAdded(arg0, __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.BehaviorTree(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __BehaviorTree(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BehaviorTree.getChild(int)"""
        return 'Task'.__wrap(super(__BehaviorTree, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.resetTask()"""
        super(BehaviorTree, self).resetTask()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @overload
    def notifyStatusUpdated(self, arg0: 'Task', arg1: 'Status'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.notifyStatusUpdated(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task$Status)"""
        super(__BehaviorTree, self).notifyStatusUpdated(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__Task, self).addChild(arg0))

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.BehaviorTree()"""
        val = __BehaviorTree()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'.__wrap(super(Task, self).getStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.BehaviorTree.getObject()"""
        return object.__wrap(super(BehaviorTree, self).getObject())

    @overload
    def step(self):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.step()"""
        super(BehaviorTree, self).step()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.reset()"""
        super(BehaviorTree, self).reset()

    @overload
    def setObject(self, arg0: object):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.setObject(E)"""
        super(__BehaviorTree, self).setObject(arg0)

    @overload
    def removeListeners(self):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.removeListeners()"""
        super(BehaviorTree, self).removeListeners()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__BehaviorTree, self).childFail(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__Task, self).checkGuard(arg0))

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'.__wrap(super(Task, self).getGuard())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__BehaviorTree, self).childRunning(arg0, arg1)

    @overload
    def removeListener(self, arg0: 'Listener'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.removeListener(com.badlogic.gdx.ai.btree.BehaviorTree$Listener<E>)"""
        super(__BehaviorTree, self).removeListener(arg0)

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setGuard(arg0)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setControl(arg0)

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.run()"""
        super(BehaviorTree, self).run()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Task', arg1: object):
        """public com.badlogic.gdx.ai.btree.BehaviorTree(com.badlogic.gdx.ai.btree.Task<E>,E)"""
        val = __BehaviorTree(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.btree.Decorator
import com.badlogic.gdx.ai.btree.Decorator as __Decorator
__Decorator = __Decorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Decorator(ABC):
    """com.badlogic.gdx.ai.btree.Decorator"""
 
    @staticmethod
    def __wrap(java_value: __Decorator) -> 'Decorator':
        return Decorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Decorator):
        """
        Dynamic initializer for Decorator.
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
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'.__wrap(super(Task, self).cloneTask())

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(Task, self).start()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.Decorator(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __Decorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Decorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Decorator, self).childSuccess(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__Task, self).addChild(arg0))

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'Task'.__wrap(super(__Decorator, self).getChild(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.Decorator()"""
        val = __Decorator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'.__wrap(super(Task, self).getStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.reset()"""
        super(Decorator, self).reset()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.Decorator()"""
        val = __Decorator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(Decorator, self).run()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(Task, self).getObject())

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__Task, self).checkGuard(arg0))

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'.__wrap(super(Task, self).getGuard())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Decorator, self).childFail(arg0)

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setGuard(arg0)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setControl(arg0)

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(Decorator, self).getChildCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.btree.BehaviorTree$Listener
import com.badlogic.gdx.ai.btree.BehaviorTree as __BehaviorTree_Listener
__Listener = __BehaviorTree_Listener.Listener
from abc import abstractmethod, ABC
 
class Listener(ABC):
    """com.badlogic.gdx.ai.btree.BehaviorTree.Listener"""
 
    @staticmethod
    def __wrap(java_value: __Listener) -> 'Listener':
        return Listener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Listener):
        """
        Dynamic initializer for Listener.
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
    def statusUpdated(self, arg0: 'Task', arg1: 'Status'):
        """public abstract void com.badlogic.gdx.ai.btree.BehaviorTree$Listener.statusUpdated(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task$Status)"""
        pass

    @abstractmethod
    def childAdded(self, arg0: 'Task', arg1: int):
        """public abstract void com.badlogic.gdx.ai.btree.BehaviorTree$Listener.childAdded(com.badlogic.gdx.ai.btree.Task<E>,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.btree.LeafTask
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
import com.badlogic.gdx.ai.btree.LeafTask as __LeafTask
__LeafTask = __LeafTask
from abc import abstractmethod, ABC
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LeafTask(ABC):
    """com.badlogic.gdx.ai.btree.LeafTask"""
 
    @staticmethod
    def __wrap(java_value: __LeafTask) -> 'LeafTask':
        return LeafTask(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LeafTask):
        """
        Dynamic initializer for LeafTask.
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
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'.__wrap(super(Task, self).cloneTask())

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__LeafTask, self).childFail(arg0)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(Task, self).start()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def run(self):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.run()"""
        super(LeafTask, self).run()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.LeafTask()"""
        val = __LeafTask()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int.__wrap(super(LeafTask, self).getChildCount())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.LeafTask()"""
        val = __LeafTask()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__Task, self).addChild(arg0))

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'.__wrap(super(Task, self).getStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def execute(self, ):
        """public abstract com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.LeafTask.execute()"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(Task, self).getObject())

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__Task, self).checkGuard(arg0))

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'.__wrap(super(Task, self).getGuard())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Task.reset()"""
        super(Task, self).reset()

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setGuard(arg0)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setControl(arg0)

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'Task'.__wrap(super(__LeafTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__LeafTask, self).childRunning(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.btree.BranchTask
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
from abc import abstractmethod, ABC
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.BranchTask as __BranchTask
__BranchTask = __BranchTask
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BranchTask(ABC):
    """com.badlogic.gdx.ai.btree.BranchTask"""
 
    @staticmethod
    def __wrap(java_value: __BranchTask) -> 'BranchTask':
        return BranchTask(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BranchTask):
        """
        Dynamic initializer for BranchTask.
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
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'.__wrap(super(Task, self).cloneTask())

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(Task, self).start()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int.__wrap(super(BranchTask, self).getChildCount())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__Task, self).addChild(arg0))

    @abstractmethod
    def run(self, ):
        """public abstract void com.badlogic.gdx.ai.btree.Task.run()"""
        pass

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.BranchTask()"""
        val = __BranchTask()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'.__wrap(super(Task, self).getStatus())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.BranchTask(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __BranchTask(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.BranchTask.reset()"""
        super(BranchTask, self).reset()

    @abstractmethod
    def childFail(self, arg0: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.BranchTask()"""
        val = __BranchTask()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(Task, self).getObject())

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__Task, self).checkGuard(arg0))

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'.__wrap(super(Task, self).getGuard())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'Task'.__wrap(super(__BranchTask, self).getChild(__int.valueOf(arg0)))

    @abstractmethod
    def childSuccess(self, arg0: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setGuard(arg0)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setControl(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.btree.Task$Status
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
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
 
class Status():
    """com.badlogic.gdx.ai.btree.Task.Status"""
 
    @staticmethod
    def __wrap(java_value: __Status) -> 'Status':
        return Status(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Status):
        """
        Dynamic initializer for Status.
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

    @staticmethod
    @overload
    def values() -> List['Status']:
        """public static com.badlogic.gdx.ai.btree.Task$Status[] com.badlogic.gdx.ai.btree.Task$Status.values()"""
        return List[Status].__wrap(__Status.values())

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
    def valueOf(arg0: str) -> 'Status':
        """public static com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task$Status.valueOf(java.lang.String)"""
        return Status.__wrap(__Status.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.SingleRunningChildBranch
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.ai.btree.SingleRunningChildBranch as __SingleRunningChildBranch
__SingleRunningChildBranch = __SingleRunningChildBranch
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.BranchTask as __BranchTask
__BranchTask = __BranchTask
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SingleRunningChildBranch(ABC):
    """com.badlogic.gdx.ai.btree.SingleRunningChildBranch"""
 
    @staticmethod
    def __wrap(java_value: __SingleRunningChildBranch) -> 'SingleRunningChildBranch':
        return SingleRunningChildBranch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SingleRunningChildBranch):
        """
        Dynamic initializer for SingleRunningChildBranch.
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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__SingleRunningChildBranch, self).childRunning(arg0, arg1)

    @override
    @overload
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'.__wrap(super(Task, self).cloneTask())

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.SingleRunningChildBranch()"""
        val = __SingleRunningChildBranch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int.__wrap(super(BranchTask, self).getChildCount())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__Task, self).addChild(arg0))

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'.__wrap(super(Task, self).getStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.run()"""
        super(SingleRunningChildBranch, self).run()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(Task, self).getObject())

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__Task, self).checkGuard(arg0))

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'.__wrap(super(Task, self).getGuard())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.SingleRunningChildBranch()"""
        val = __SingleRunningChildBranch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(SingleRunningChildBranch, self).resetTask()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.start()"""
        super(SingleRunningChildBranch, self).start()

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'Task'.__wrap(super(__BranchTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setGuard(arg0)

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.SingleRunningChildBranch(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __SingleRunningChildBranch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setControl(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.reset()"""
        super(SingleRunningChildBranch, self).reset()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__SingleRunningChildBranch, self).childFail(arg0)

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__SingleRunningChildBranch, self).childSuccess(arg0) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.LoopDecorator
import com.badlogic.gdx.ai.btree.Decorator as __Decorator
__Decorator = __Decorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
from builtins import object
import com.badlogic.gdx.ai.btree.LoopDecorator as __LoopDecorator
__LoopDecorator = __LoopDecorator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoopDecorator(ABC):
    """com.badlogic.gdx.ai.btree.LoopDecorator"""
 
    @staticmethod
    def __wrap(java_value: __LoopDecorator) -> 'LoopDecorator':
        return LoopDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoopDecorator):
        """
        Dynamic initializer for LoopDecorator.
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
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'.__wrap(super(Task, self).cloneTask())

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(Task, self).start()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.reset()"""
        super(LoopDecorator, self).reset()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Decorator, self).childSuccess(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.LoopDecorator.condition()"""
        return bool.__wrap(super(LoopDecorator, self).condition())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__LoopDecorator, self).childRunning(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__Task, self).addChild(arg0))

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'Task'.__wrap(super(__Decorator, self).getChild(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.LoopDecorator()"""
        val = __LoopDecorator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'.__wrap(super(Task, self).getStatus())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(LoopDecorator, self).run()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(Task, self).getObject())

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__Task, self).checkGuard(arg0))

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'.__wrap(super(Task, self).getGuard())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Decorator, self).childFail(arg0)

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setGuard(arg0)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Task, self).setControl(arg0)

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(Decorator, self).getChildCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.LoopDecorator()"""
        val = __LoopDecorator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.LoopDecorator(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __LoopDecorator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val
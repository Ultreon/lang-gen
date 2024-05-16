from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.ai.btree.TaskCloner as _TaskCloner
_TaskCloner = _TaskCloner
from abc import abstractmethod, ABC
 
class TaskCloner():
    """com.badlogic.gdx.ai.btree.TaskCloner"""
 
    @staticmethod
    def _wrap(java_value: _TaskCloner) -> 'TaskCloner':
        return TaskCloner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TaskCloner):
        """
        Dynamic initializer for TaskCloner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TaskCloner__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TaskCloner__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.TaskCloner
import com.badlogic.gdx.ai.btree.TaskCloner as _TaskCloner
_TaskCloner = _TaskCloner
from abc import abstractmethod, ABC
 
class TaskCloner():
    """com.badlogic.gdx.ai.btree.TaskCloner"""
 
    @staticmethod
    def _wrap(java_value: _TaskCloner) -> 'TaskCloner':
        return TaskCloner(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TaskCloner):
        """
        Dynamic initializer for TaskCloner.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TaskCloner__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TaskCloner__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.TaskCloner 
 
 
# CLASS: com.badlogic.gdx.ai.btree.Task$Status
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Status():
    """com.badlogic.gdx.ai.btree.Task.Status"""
 
    @staticmethod
    def _wrap(java_value: _Status) -> 'Status':
        return Status(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Status):
        """
        Dynamic initializer for Status.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Status__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Status__wrapper":
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
    def values() -> List['Status']:
        """public static com.badlogic.gdx.ai.btree.Task$Status[] com.badlogic.gdx.ai.btree.Task$Status.values()"""
        return List[Status]._wrap(_Status.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Status':
        """public static com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task$Status.valueOf(java.lang.String)"""
        return Status._wrap(_Status.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.Decorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Decorator as _Decorator
_Decorator = _Decorator
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Decorator():
    """com.badlogic.gdx.ai.btree.Decorator"""
 
    @staticmethod
    def _wrap(java_value: _Decorator) -> 'Decorator':
        return Decorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Decorator):
        """
        Dynamic initializer for Decorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Decorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Decorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(Task, self).getObject())

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(Decorator, self).getChildCount())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setGuard(arg0)

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
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'._wrap(super(Task, self).cloneTask())

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Decorator, self).childFail(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'._wrap(super(Task, self).getStatus())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.Decorator(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _Decorator(arg0)
        self.__wrapper = val

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'Task'._wrap(super(_Decorator, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'._wrap(super(Task, self).getGuard())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.Decorator()"""
        val = _Decorator()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.Decorator()"""
        val = _Decorator()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.reset()"""
        super(Decorator, self).reset()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Decorator, self).childSuccess(arg0)

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(Decorator, self).run()

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setControl(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_Task, self).addChild(arg0))

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Decorator, self).childRunning(arg0, arg1)

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.SingleRunningChildBranch
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.SingleRunningChildBranch as _SingleRunningChildBranch
_SingleRunningChildBranch = _SingleRunningChildBranch
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.BranchTask as _BranchTask
_BranchTask = _BranchTask
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SingleRunningChildBranch():
    """com.badlogic.gdx.ai.btree.SingleRunningChildBranch"""
 
    @staticmethod
    def _wrap(java_value: _SingleRunningChildBranch) -> 'SingleRunningChildBranch':
        return SingleRunningChildBranch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SingleRunningChildBranch):
        """
        Dynamic initializer for SingleRunningChildBranch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SingleRunningChildBranch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SingleRunningChildBranch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(Task, self).getObject())

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
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setGuard(arg0)

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_SingleRunningChildBranch, self).childSuccess(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_SingleRunningChildBranch, self).childRunning(arg0, arg1)

    @override
    @overload
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'._wrap(super(Task, self).cloneTask())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'._wrap(super(Task, self).getStatus())

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_SingleRunningChildBranch, self).childFail(arg0)

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.SingleRunningChildBranch()"""
        val = _SingleRunningChildBranch()
        self.__wrapper = val

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int._wrap(super(BranchTask, self).getChildCount())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'._wrap(super(Task, self).getGuard())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'Task'._wrap(super(_BranchTask, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.run()"""
        super(SingleRunningChildBranch, self).run()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setControl(arg0)

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.SingleRunningChildBranch(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _SingleRunningChildBranch(arg0)
        self.__wrapper = val

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_Task, self).addChild(arg0))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.SingleRunningChildBranch()"""
        val = _SingleRunningChildBranch()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.Task
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
from abc import abstractmethod, ABC
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Task():
    """com.badlogic.gdx.ai.btree.Task"""
 
    @staticmethod
    def _wrap(java_value: _Task) -> 'Task':
        return Task(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Task):
        """
        Dynamic initializer for Task.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Task__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Task__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(Task, self).getObject())

    @abstractmethod
    def getChild(self, arg0: int):
        """public abstract com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getChild(int)"""
        pass

    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.Task()"""
        val = _Task()
        self.__wrapper = val

    @overload
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'._wrap(super(Task, self).cloneTask())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'._wrap(super(Task, self).getGuard())

    @abstractmethod
    def getChildCount(self, ):
        """public abstract int com.badlogic.gdx.ai.btree.Task.getChildCount()"""
        pass

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
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(Task, self).start()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @abstractmethod
    def run(self, ):
        """public abstract void com.badlogic.gdx.ai.btree.Task.run()"""
        pass

    @abstractmethod
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'._wrap(super(Task, self).getStatus())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @abstractmethod
    def childFail(self, arg0: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setControl(arg0)

    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setGuard(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Task.reset()"""
        super(Task, self).reset()

    @abstractmethod
    def childSuccess(self, arg0: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.Task()"""
        val = _Task()
        self.__wrapper = val

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_Task, self).addChild(arg0))

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.BehaviorTree
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.BehaviorTree as _BehaviorTree
_BehaviorTree = _BehaviorTree
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BehaviorTree():
    """com.badlogic.gdx.ai.btree.BehaviorTree"""
 
    @staticmethod
    def _wrap(java_value: _BehaviorTree) -> 'BehaviorTree':
        return BehaviorTree(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BehaviorTree):
        """
        Dynamic initializer for BehaviorTree.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BehaviorTree__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BehaviorTree__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setGuard(arg0)

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

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BehaviorTree.getChild(int)"""
        return 'Task'._wrap(super(_BehaviorTree, self).getChild(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Task', arg1: object):
        """public com.badlogic.gdx.ai.btree.BehaviorTree(com.badlogic.gdx.ai.btree.Task<E>,E)"""
        val = _BehaviorTree(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'._wrap(super(Task, self).cloneTask())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'._wrap(super(Task, self).getStatus())

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.BehaviorTree()"""
        val = _BehaviorTree()
        self.__wrapper = val

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_BehaviorTree, self).childSuccess(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @overload
    def removeListener(self, arg0: 'Listener'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.removeListener(com.badlogic.gdx.ai.btree.BehaviorTree$Listener<E>)"""
        super(_BehaviorTree, self).removeListener(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.BehaviorTree()"""
        val = _BehaviorTree()
        self.__wrapper = val

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_BehaviorTree, self).childRunning(arg0, arg1)

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.BehaviorTree(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _BehaviorTree(arg0)
        self.__wrapper = val

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'._wrap(super(Task, self).getGuard())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @overload
    def step(self):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.step()"""
        super(BehaviorTree, self).step()

    @overload
    def notifyChildAdded(self, arg0: 'Task', arg1: int):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.notifyChildAdded(com.badlogic.gdx.ai.btree.Task<E>,int)"""
        super(_BehaviorTree, self).notifyChildAdded(arg0, _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.reset()"""
        super(BehaviorTree, self).reset()

    @overload
    def removeListeners(self):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.removeListeners()"""
        super(BehaviorTree, self).removeListeners()

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setObject(self, arg0: object):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.setObject(E)"""
        super(_BehaviorTree, self).setObject(arg0)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setControl(arg0)

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BehaviorTree.getChildCount()"""
        return int._wrap(super(BehaviorTree, self).getChildCount())

    @overload
    def addListener(self, arg0: 'Listener'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.addListener(com.badlogic.gdx.ai.btree.BehaviorTree$Listener<E>)"""
        super(_BehaviorTree, self).addListener(arg0)

    @overload
    def notifyStatusUpdated(self, arg0: 'Task', arg1: 'Status'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.notifyStatusUpdated(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task$Status)"""
        super(_BehaviorTree, self).notifyStatusUpdated(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_Task, self).addChild(arg0))

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

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.BehaviorTree.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_BehaviorTree, self).childFail(arg0)

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.BehaviorTree.getObject()"""
        return object._wrap(super(BehaviorTree, self).getObject())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.BehaviorTree$Listener
import com.badlogic.gdx.ai.btree.BehaviorTree as _BehaviorTree_Listener
_Listener = _BehaviorTree_Listener.Listener
from abc import abstractmethod, ABC
 
class Listener():
    """com.badlogic.gdx.ai.btree.BehaviorTree.Listener"""
 
    @staticmethod
    def _wrap(java_value: _Listener) -> 'Listener':
        return Listener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Listener):
        """
        Dynamic initializer for Listener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Listener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Listener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.btree.TaskCloneException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
import com.badlogic.gdx.ai.btree.TaskCloneException as _TaskCloneException
_TaskCloneException = _TaskCloneException
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TaskCloneException():
    """com.badlogic.gdx.ai.btree.TaskCloneException"""
 
    @staticmethod
    def _wrap(java_value: _TaskCloneException) -> 'TaskCloneException':
        return TaskCloneException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TaskCloneException):
        """
        Dynamic initializer for TaskCloneException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TaskCloneException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TaskCloneException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.TaskCloneException()"""
        val = _TaskCloneException()
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.TaskCloneException(java.lang.String)"""
        val = _TaskCloneException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.TaskCloneException(java.lang.String,java.lang.Throwable)"""
        val = _TaskCloneException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def __init__(self, arg0: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.TaskCloneException(java.lang.Throwable)"""
        val = _TaskCloneException(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.TaskCloneException()"""
        val = _TaskCloneException()
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.LoopDecorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Decorator as _Decorator
_Decorator = _Decorator
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.LoopDecorator as _LoopDecorator
_LoopDecorator = _LoopDecorator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoopDecorator():
    """com.badlogic.gdx.ai.btree.LoopDecorator"""
 
    @staticmethod
    def _wrap(java_value: _LoopDecorator) -> 'LoopDecorator':
        return LoopDecorator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoopDecorator):
        """
        Dynamic initializer for LoopDecorator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoopDecorator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoopDecorator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(Task, self).getObject())

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(Task, self).fail()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(Decorator, self).getChildCount())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(Task, self).end()

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setGuard(arg0)

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
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'._wrap(super(Task, self).cloneTask())

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Decorator, self).childFail(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'._wrap(super(Task, self).getStatus())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.LoopDecorator.condition()"""
        return bool._wrap(super(LoopDecorator, self).condition())

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(Task, self).running()

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'Task'._wrap(super(_Decorator, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'._wrap(super(Task, self).getGuard())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.LoopDecorator()"""
        val = _LoopDecorator()
        self.__wrapper = val

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Decorator, self).childSuccess(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.LoopDecorator()"""
        val = _LoopDecorator()
        self.__wrapper = val

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(LoopDecorator, self).run()

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setControl(arg0)

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_LoopDecorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_Task, self).addChild(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.LoopDecorator(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _LoopDecorator(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.BranchTask
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
from abc import abstractmethod, ABC
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.BranchTask as _BranchTask
_BranchTask = _BranchTask
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BranchTask():
    """com.badlogic.gdx.ai.btree.BranchTask"""
 
    @staticmethod
    def _wrap(java_value: _BranchTask) -> 'BranchTask':
        return BranchTask(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BranchTask):
        """
        Dynamic initializer for BranchTask.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BranchTask__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BranchTask__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(Task, self).getObject())

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
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setGuard(arg0)

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
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'._wrap(super(Task, self).cloneTask())

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'._wrap(super(Task, self).getStatus())

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
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int._wrap(super(BranchTask, self).getChildCount())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'._wrap(super(Task, self).getGuard())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

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
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'Task'._wrap(super(_BranchTask, self).getChild(_int.valueOf(arg0)))

    @abstractmethod
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.BranchTask.reset()"""
        super(BranchTask, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def childFail(self, arg0: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setControl(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.BranchTask()"""
        val = _BranchTask()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.BranchTask(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _BranchTask(arg0)
        self.__wrapper = val

    @abstractmethod
    def childSuccess(self, arg0: 'Task'):
        """public abstract void com.badlogic.gdx.ai.btree.Task.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_Task, self).addChild(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.BranchTask()"""
        val = _BranchTask()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.btree.LeafTask
from builtins import str
import com.badlogic.gdx.ai.btree.LeafTask as _LeafTask
_LeafTask = _LeafTask
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
from abc import abstractmethod, ABC
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LeafTask():
    """com.badlogic.gdx.ai.btree.LeafTask"""
 
    @staticmethod
    def _wrap(java_value: _LeafTask) -> 'LeafTask':
        return LeafTask(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LeafTask):
        """
        Dynamic initializer for LeafTask.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LeafTask__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LeafTask__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(Task, self).getObject())

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
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setGuard(arg0)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(Task, self).start()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_LeafTask, self).childFail(arg0)

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int._wrap(super(LeafTask, self).getChildCount())

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

    @override
    @overload
    def cloneTask(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'Task'._wrap(super(Task, self).cloneTask())

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(Task, self).resetTask()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.LeafTask()"""
        val = _LeafTask()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStatus(self) -> 'Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'Status'._wrap(super(Task, self).getStatus())

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
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(Task, self).success()

    @override
    @overload
    def getGuard(self) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'Task'._wrap(super(Task, self).getGuard())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(Task, self).cancel()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def execute(self, ):
        """public abstract com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.LeafTask.execute()"""
        pass

    @overload
    def getChild(self, arg0: int) -> 'Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'Task'._wrap(super(_LeafTask, self).getChild(_int.valueOf(arg0)))

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Task, self).setControl(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Task.reset()"""
        super(Task, self).reset()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_LeafTask, self).childRunning(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_Task, self).addChild(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.LeafTask()"""
        val = _LeafTask()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())
from __future__ import annotations
from overload import overload


 
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
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.BranchTask as _BranchTask
_BranchTask = _BranchTask
import com.badlogic.gdx.ai.btree.branch.RandomSequence as _RandomSequence
_RandomSequence = _RandomSequence
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.ai.btree.branch.Sequence as _Sequence
_Sequence = _Sequence
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RandomSequence():
    """com.badlogic.gdx.ai.btree.branch.RandomSequence"""
 
    @staticmethod
    def _wrap(java_value: _RandomSequence) -> 'RandomSequence':
        return RandomSequence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RandomSequence):
        """
        Dynamic initializer for RandomSequence.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RandomSequence__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RandomSequence__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.branch.RandomSequence.start()"""
        super(RandomSequence, self).start()

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setGuard(arg0)

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'._wrap(super(btree.Task, self).cloneTask())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'._wrap(super(btree.Task, self).getStatus())

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.BranchTask, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_btree.Task, self).addChild(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.reset()"""
        super(btree.SingleRunningChildBranch, self).reset()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Sequence, self).childSuccess(arg0)

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Sequence, self).childFail(arg0)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setControl(arg0)

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
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.SingleRunningChildBranch, self).childRunning(arg0, arg1)

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
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _RandomSequence(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence()"""
        val = _RandomSequence()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = _RandomSequence(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.run()"""
        super(btree.SingleRunningChildBranch, self).run()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int._wrap(super(btree.BranchTask, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence()"""
        val = _RandomSequence()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.RandomSequence
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
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.BranchTask as _BranchTask
_BranchTask = _BranchTask
import com.badlogic.gdx.ai.btree.branch.RandomSequence as _RandomSequence
_RandomSequence = _RandomSequence
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.ai.btree.branch.Sequence as _Sequence
_Sequence = _Sequence
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RandomSequence():
    """com.badlogic.gdx.ai.btree.branch.RandomSequence"""
 
    @staticmethod
    def _wrap(java_value: _RandomSequence) -> 'RandomSequence':
        return RandomSequence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RandomSequence):
        """
        Dynamic initializer for RandomSequence.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RandomSequence__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RandomSequence__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.branch.RandomSequence.start()"""
        super(RandomSequence, self).start()

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setGuard(arg0)

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'._wrap(super(btree.Task, self).cloneTask())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'._wrap(super(btree.Task, self).getStatus())

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.BranchTask, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_btree.Task, self).addChild(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.reset()"""
        super(btree.SingleRunningChildBranch, self).reset()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Sequence, self).childSuccess(arg0)

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Sequence, self).childFail(arg0)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setControl(arg0)

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
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.SingleRunningChildBranch, self).childRunning(arg0, arg1)

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
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _RandomSequence(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence()"""
        val = _RandomSequence()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = _RandomSequence(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.run()"""
        super(btree.SingleRunningChildBranch, self).run()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int._wrap(super(btree.BranchTask, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence()"""
        val = _RandomSequence()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.RandomSequence 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Parallel$Policy
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import com.badlogic.gdx.ai.btree.branch.Parallel as _Parallel_Policy
_Policy = _Parallel_Policy.Policy
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Policy():
    """com.badlogic.gdx.ai.btree.branch.Parallel.Policy"""
 
    @staticmethod
    def _wrap(java_value: _Policy) -> 'Policy':
        return Policy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Policy):
        """
        Dynamic initializer for Policy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Policy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Policy__wrapper":
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
    def values() -> List['Policy']:
        """public static com.badlogic.gdx.ai.btree.branch.Parallel$Policy[] com.badlogic.gdx.ai.btree.branch.Parallel$Policy.values()"""
        return List[Policy]._wrap(_Policy.values())

    @abstractmethod
    def onChildSuccess(self, arg0: 'Parallel'):
        """public abstract java.lang.Boolean com.badlogic.gdx.ai.btree.branch.Parallel$Policy.onChildSuccess(com.badlogic.gdx.ai.btree.branch.Parallel<?>)"""
        pass

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

    @abstractmethod
    def onChildFail(self, arg0: 'Parallel'):
        """public abstract java.lang.Boolean com.badlogic.gdx.ai.btree.branch.Parallel$Policy.onChildFail(com.badlogic.gdx.ai.btree.branch.Parallel<?>)"""
        pass

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Policy':
        """public static com.badlogic.gdx.ai.btree.branch.Parallel$Policy com.badlogic.gdx.ai.btree.branch.Parallel$Policy.valueOf(java.lang.String)"""
        return Policy._wrap(_Policy.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector
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
import com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector as _DynamicGuardSelector
_DynamicGuardSelector = _DynamicGuardSelector
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.BranchTask as _BranchTask
_BranchTask = _BranchTask
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DynamicGuardSelector():
    """com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector"""
 
    @staticmethod
    def _wrap(java_value: _DynamicGuardSelector) -> 'DynamicGuardSelector':
        return DynamicGuardSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DynamicGuardSelector):
        """
        Dynamic initializer for DynamicGuardSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DynamicGuardSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DynamicGuardSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setGuard(arg0)

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'._wrap(super(btree.Task, self).cloneTask())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'._wrap(super(btree.Task, self).getStatus())

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = _DynamicGuardSelector(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector()"""
        val = _DynamicGuardSelector()
        self.__wrapper = val

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.BranchTask, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_btree.Task, self).addChild(arg0))

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(btree.Task, self).start()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.resetTask()"""
        super(DynamicGuardSelector, self).resetTask()

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _DynamicGuardSelector(arg0)
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setControl(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_DynamicGuardSelector, self).childSuccess(arg0)

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_DynamicGuardSelector, self).childRunning(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector()"""
        val = _DynamicGuardSelector()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.reset()"""
        super(DynamicGuardSelector, self).reset()

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.run()"""
        super(DynamicGuardSelector, self).run()

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_DynamicGuardSelector, self).childFail(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int._wrap(super(btree.BranchTask, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Selector
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
import com.badlogic.gdx.ai.btree.branch.Selector as _Selector
_Selector = _Selector
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.SingleRunningChildBranch as _SingleRunningChildBranch
_SingleRunningChildBranch = _SingleRunningChildBranch
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.BranchTask as _BranchTask
_BranchTask = _BranchTask
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Selector():
    """com.badlogic.gdx.ai.btree.branch.Selector"""
 
    @staticmethod
    def _wrap(java_value: _Selector) -> 'Selector':
        return Selector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Selector):
        """
        Dynamic initializer for Selector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Selector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Selector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setGuard(arg0)

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'._wrap(super(btree.Task, self).cloneTask())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Selector(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _Selector(arg0)
        self.__wrapper = val

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'._wrap(super(btree.Task, self).getStatus())

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.BranchTask, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_btree.Task, self).addChild(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Selector, self).childSuccess(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.reset()"""
        super(btree.SingleRunningChildBranch, self).reset()

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setControl(arg0)

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
    def start(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.start()"""
        super(btree.SingleRunningChildBranch, self).start()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.SingleRunningChildBranch, self).childRunning(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.Selector()"""
        val = _Selector()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Selector, self).childFail(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Selector(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = _Selector(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.Selector()"""
        val = _Selector()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.run()"""
        super(btree.SingleRunningChildBranch, self).run()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int._wrap(super(btree.BranchTask, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.RandomSelector
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
import com.badlogic.gdx.ai.btree.branch.Selector as _Selector
_Selector = _Selector
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.SingleRunningChildBranch as _SingleRunningChildBranch
_SingleRunningChildBranch = _SingleRunningChildBranch
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.branch.RandomSelector as _RandomSelector
_RandomSelector = _RandomSelector
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.BranchTask as _BranchTask
_BranchTask = _BranchTask
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RandomSelector():
    """com.badlogic.gdx.ai.btree.branch.RandomSelector"""
 
    @staticmethod
    def _wrap(java_value: _RandomSelector) -> 'RandomSelector':
        return RandomSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RandomSelector):
        """
        Dynamic initializer for RandomSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RandomSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RandomSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setGuard(arg0)

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'._wrap(super(btree.Task, self).cloneTask())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'._wrap(super(btree.Task, self).getStatus())

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.BranchTask, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_btree.Task, self).addChild(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Selector, self).childSuccess(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.RandomSelector()"""
        val = _RandomSelector()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.reset()"""
        super(btree.SingleRunningChildBranch, self).reset()

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setControl(arg0)

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
    def start(self):
        """public void com.badlogic.gdx.ai.btree.branch.RandomSelector.start()"""
        super(RandomSelector, self).start()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSelector(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = _RandomSelector(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.RandomSelector()"""
        val = _RandomSelector()
        self.__wrapper = val

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.SingleRunningChildBranch, self).childRunning(arg0, arg1)

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
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Selector, self).childFail(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.run()"""
        super(btree.SingleRunningChildBranch, self).run()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int._wrap(super(btree.BranchTask, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSelector(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _RandomSelector(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Parallel
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
import com.badlogic.gdx.ai.btree.branch.Parallel as _Parallel
_Parallel = _Parallel
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.BranchTask as _BranchTask
_BranchTask = _BranchTask
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Parallel():
    """com.badlogic.gdx.ai.btree.branch.Parallel"""
 
    @staticmethod
    def _wrap(java_value: _Parallel) -> 'Parallel':
        return Parallel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Parallel):
        """
        Dynamic initializer for Parallel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Parallel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Parallel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setGuard(arg0)

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'._wrap(super(btree.Task, self).cloneTask())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'._wrap(super(btree.Task, self).getStatus())

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.BranchTask, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_btree.Task, self).addChild(arg0))

    @overload
    def __init__(self, arg0: 'Policy', arg1: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Policy,com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _Parallel(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(btree.Task, self).start()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Policy', *arg1: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Policy,com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = _Parallel(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @overload
    def __init__(self, arg0: 'Orchestrator', *arg1: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator,com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = _Parallel(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setControl(arg0)

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
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.resetTask()"""
        super(Parallel, self).resetTask()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Policy'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Policy)"""
        val = _Parallel(arg0)
        self.__wrapper = val

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Parallel, self).childRunning(arg0, arg1)

    @overload
    def __init__(self, arg0: 'Orchestrator', arg1: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator,com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _Parallel(arg0, arg1)
        self.__wrapper = val

    @overload
    def resetAllChildren(self):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.resetAllChildren()"""
        super(Parallel, self).resetAllChildren()

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.run()"""
        super(Parallel, self).run()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @overload
    def __init__(self, arg0: 'Policy', arg1: 'Orchestrator', arg2: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Policy,com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator,com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _Parallel(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _Parallel(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Parallel, self).childFail(arg0)

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.Parallel()"""
        val = _Parallel()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Parallel, self).childSuccess(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.Parallel()"""
        val = _Parallel()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int._wrap(super(btree.BranchTask, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.reset()"""
        super(Parallel, self).reset()

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = _Parallel(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Sequence
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
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.BranchTask as _BranchTask
_BranchTask = _BranchTask
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.ai.btree.branch.Sequence as _Sequence
_Sequence = _Sequence
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Sequence():
    """com.badlogic.gdx.ai.btree.branch.Sequence"""
 
    @staticmethod
    def _wrap(java_value: _Sequence) -> 'Sequence':
        return Sequence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Sequence):
        """
        Dynamic initializer for Sequence.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Sequence__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Sequence__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setGuard(arg0)

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'._wrap(super(btree.Task, self).cloneTask())

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'._wrap(super(btree.Task, self).getStatus())

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.BranchTask, self).getChild(_int.valueOf(arg0)))

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_btree.Task, self).addChild(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.reset()"""
        super(btree.SingleRunningChildBranch, self).reset()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Sequence, self).childSuccess(arg0)

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.Sequence()"""
        val = _Sequence()
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Sequence, self).childFail(arg0)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Task, self).setControl(arg0)

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
    def start(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.start()"""
        super(btree.SingleRunningChildBranch, self).start()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.SingleRunningChildBranch, self).childRunning(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.Sequence()"""
        val = _Sequence()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Sequence(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = _Sequence(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.run()"""
        super(btree.SingleRunningChildBranch, self).run()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int._wrap(super(btree.BranchTask, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Sequence(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = _Sequence(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.branch.Parallel as _Parallel_Orchestrator
_Orchestrator = _Parallel_Orchestrator.Orchestrator
from abc import abstractmethod, ABC
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
 
class Orchestrator():
    """com.badlogic.gdx.ai.btree.branch.Parallel.Orchestrator"""
 
    @staticmethod
    def _wrap(java_value: _Orchestrator) -> 'Orchestrator':
        return Orchestrator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Orchestrator):
        """
        Dynamic initializer for Orchestrator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Orchestrator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Orchestrator__wrapper":
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
    def valueOf(arg0: str) -> 'Orchestrator':
        """public static com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator.valueOf(java.lang.String)"""
        return Orchestrator._wrap(_Orchestrator.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Orchestrator']:
        """public static com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator[] com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator.values()"""
        return List[Orchestrator]._wrap(_Orchestrator.values())

    @abstractmethod
    def execute(self, arg0: 'Parallel'):
        """public abstract void com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator.execute(com.badlogic.gdx.ai.btree.branch.Parallel<?>)"""
        pass
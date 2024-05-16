from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.branch.Selector as __Selector
__Selector = __Selector
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
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.BranchTask as __BranchTask
__BranchTask = __BranchTask
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Selector(ai.__SingleRunningChildBranch, btree.SingleRunningChildBranch):
    """com.badlogic.gdx.ai.btree.branch.Selector"""
 
    @staticmethod
    def __wrap(java_value: __Selector) -> 'Selector':
        return Selector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Selector):
        """
        Dynamic initializer for Selector.
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
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

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
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.BranchTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.start()"""
        super(btree.SingleRunningChildBranch, self).start()

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setControl(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).cloneTask())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Selector(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __Selector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.Selector()"""
        val = __Selector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int.__wrap(super(btree.BranchTask, self).getChildCount())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Selector, self).childSuccess(arg0)

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'.__wrap(super(btree.Task, self).getStatus())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setGuard(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Selector, self).childFail(arg0)

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Selector(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = __Selector(arg0)
        self.__dict__ = val.__dict__
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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.SingleRunningChildBranch, self).childRunning(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.Selector()"""
        val = __Selector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Selector
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.branch.Selector as __Selector
__Selector = __Selector
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
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.BranchTask as __BranchTask
__BranchTask = __BranchTask
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Selector(ai.__SingleRunningChildBranch, btree.SingleRunningChildBranch):
    """com.badlogic.gdx.ai.btree.branch.Selector"""
 
    @staticmethod
    def __wrap(java_value: __Selector) -> 'Selector':
        return Selector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Selector):
        """
        Dynamic initializer for Selector.
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
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

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
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.BranchTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.start()"""
        super(btree.SingleRunningChildBranch, self).start()

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setControl(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).cloneTask())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Selector(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __Selector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.Selector()"""
        val = __Selector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int.__wrap(super(btree.BranchTask, self).getChildCount())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Selector, self).childSuccess(arg0)

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'.__wrap(super(btree.Task, self).getStatus())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setGuard(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Selector, self).childFail(arg0)

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Selector(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = __Selector(arg0)
        self.__dict__ = val.__dict__
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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.SingleRunningChildBranch, self).childRunning(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.Selector()"""
        val = __Selector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Selector 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.RandomSequence
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.branch.RandomSequence as __RandomSequence
__RandomSequence = __RandomSequence
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
import com.badlogic.gdx.ai.btree.branch.Sequence as __Sequence
__Sequence = __Sequence
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.BranchTask as __BranchTask
__BranchTask = __BranchTask
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RandomSequence(__Sequence, Sequence):
    """com.badlogic.gdx.ai.btree.branch.RandomSequence"""
 
    @staticmethod
    def __wrap(java_value: __RandomSequence) -> 'RandomSequence':
        return RandomSequence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RandomSequence):
        """
        Dynamic initializer for RandomSequence.
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
    def start(self):
        """public void com.badlogic.gdx.ai.btree.branch.RandomSequence.start()"""
        super(RandomSequence, self).start()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence()"""
        val = __RandomSequence()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Sequence, self).childFail(arg0)

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = __RandomSequence(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __RandomSequence(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.BranchTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setControl(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).cloneTask())

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int.__wrap(super(btree.BranchTask, self).getChildCount())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.RandomSequence()"""
        val = __RandomSequence()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'.__wrap(super(btree.Task, self).getStatus())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setGuard(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.SingleRunningChildBranch, self).childRunning(arg0, arg1)

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Sequence, self).childSuccess(arg0) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector as __DynamicGuardSelector
__DynamicGuardSelector = __DynamicGuardSelector
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.BranchTask as __BranchTask
__BranchTask = __BranchTask
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DynamicGuardSelector(ai.__BranchTask, btree.BranchTask):
    """com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector"""
 
    @staticmethod
    def __wrap(java_value: __DynamicGuardSelector) -> 'DynamicGuardSelector':
        return DynamicGuardSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DynamicGuardSelector):
        """
        Dynamic initializer for DynamicGuardSelector.
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
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__DynamicGuardSelector, self).childRunning(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector()"""
        val = __DynamicGuardSelector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector()"""
        val = __DynamicGuardSelector()
        self.__dict__ = val.__dict__
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

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.resetTask()"""
        super(DynamicGuardSelector, self).resetTask()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.BranchTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setControl(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).cloneTask())

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = __DynamicGuardSelector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__DynamicGuardSelector, self).childFail(arg0)

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int.__wrap(super(btree.BranchTask, self).getChildCount())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __DynamicGuardSelector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'.__wrap(super(btree.Task, self).getStatus())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

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
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setGuard(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.DynamicGuardSelector.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__DynamicGuardSelector, self).childSuccess(arg0)

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Sequence
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
import com.badlogic.gdx.ai.btree.branch.Sequence as __Sequence
__Sequence = __Sequence
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.BranchTask as __BranchTask
__BranchTask = __BranchTask
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Sequence(ai.__SingleRunningChildBranch, btree.SingleRunningChildBranch):
    """com.badlogic.gdx.ai.btree.branch.Sequence"""
 
    @staticmethod
    def __wrap(java_value: __Sequence) -> 'Sequence':
        return Sequence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Sequence):
        """
        Dynamic initializer for Sequence.
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
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Sequence(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __Sequence(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Sequence(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = __Sequence(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.reset()"""
        super(btree.SingleRunningChildBranch, self).reset()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Sequence, self).childFail(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.BranchTask, self).getChild(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.Sequence()"""
        val = __Sequence()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.start()"""
        super(btree.SingleRunningChildBranch, self).start()

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setControl(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).cloneTask())

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int.__wrap(super(btree.BranchTask, self).getChildCount())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'.__wrap(super(btree.Task, self).getStatus())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setGuard(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.Sequence()"""
        val = __Sequence()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.SingleRunningChildBranch, self).childRunning(arg0, arg1)

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Sequence.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Sequence, self).childSuccess(arg0) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.ai.btree.branch.Parallel as __Parallel_Orchestrator
__Orchestrator = __Parallel_Orchestrator.Orchestrator
from abc import abstractmethod, ABC
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
 
class Orchestrator(ABC, __Enum, Enum):
    """com.badlogic.gdx.ai.btree.branch.Parallel.Orchestrator"""
 
    @staticmethod
    def __wrap(java_value: __Orchestrator) -> 'Orchestrator':
        return Orchestrator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Orchestrator):
        """
        Dynamic initializer for Orchestrator.
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
    def valueOf(arg0: str) -> 'Orchestrator':
        """public static com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator.valueOf(java.lang.String)"""
        return Orchestrator.__wrap(__Orchestrator.valueOf(arg0))

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
    def values() -> List['Orchestrator']:
        """public static com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator[] com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator.values()"""
        return List[Orchestrator].__wrap(__Orchestrator.values())

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

    @abstractmethod
    def execute(self, arg0: 'Parallel'):
        """public abstract void com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator.execute(com.badlogic.gdx.ai.btree.branch.Parallel<?>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.RandomSelector
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.branch.Selector as __Selector
__Selector = __Selector
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
import com.badlogic.gdx.ai.btree.branch.RandomSelector as __RandomSelector
__RandomSelector = __RandomSelector
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.BranchTask as __BranchTask
__BranchTask = __BranchTask
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RandomSelector(__Selector, Selector):
    """com.badlogic.gdx.ai.btree.branch.RandomSelector"""
 
    @staticmethod
    def __wrap(java_value: __RandomSelector) -> 'RandomSelector':
        return RandomSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RandomSelector):
        """
        Dynamic initializer for RandomSelector.
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
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSelector(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __RandomSelector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.reset()"""
        super(btree.SingleRunningChildBranch, self).reset()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.RandomSelector()"""
        val = __RandomSelector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.BranchTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setControl(arg0)

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
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).cloneTask())

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.resetTask()"""
        super(btree.SingleRunningChildBranch, self).resetTask()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.RandomSelector()"""
        val = __RandomSelector()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int.__wrap(super(btree.BranchTask, self).getChildCount())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Selector, self).childSuccess(arg0)

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.RandomSelector(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = __RandomSelector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'.__wrap(super(btree.Task, self).getStatus())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setGuard(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Selector.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Selector, self).childFail(arg0)

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.SingleRunningChildBranch.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.SingleRunningChildBranch, self).childRunning(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Parallel$Policy
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from abc import abstractmethod, ABC
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
import com.badlogic.gdx.ai.btree.branch.Parallel as __Parallel_Policy
__Policy = __Parallel_Policy.Policy
from builtins import int
 
class Policy(ABC, __Enum, Enum):
    """com.badlogic.gdx.ai.btree.branch.Parallel.Policy"""
 
    @staticmethod
    def __wrap(java_value: __Policy) -> 'Policy':
        return Policy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Policy):
        """
        Dynamic initializer for Policy.
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
    def values() -> List['Policy']:
        """public static com.badlogic.gdx.ai.btree.branch.Parallel$Policy[] com.badlogic.gdx.ai.btree.branch.Parallel$Policy.values()"""
        return List[Policy].__wrap(__Policy.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Policy':
        """public static com.badlogic.gdx.ai.btree.branch.Parallel$Policy com.badlogic.gdx.ai.btree.branch.Parallel$Policy.valueOf(java.lang.String)"""
        return Policy.__wrap(__Policy.valueOf(arg0))

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

    @abstractmethod
    def onChildSuccess(self, arg0: 'Parallel'):
        """public abstract java.lang.Boolean com.badlogic.gdx.ai.btree.branch.Parallel$Policy.onChildSuccess(com.badlogic.gdx.ai.btree.branch.Parallel<?>)"""
        pass

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

    @abstractmethod
    def onChildFail(self, arg0: 'Parallel'):
        """public abstract java.lang.Boolean com.badlogic.gdx.ai.btree.branch.Parallel$Policy.onChildFail(com.badlogic.gdx.ai.btree.branch.Parallel<?>)"""
        pass

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.branch.Parallel
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
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.branch.Parallel as __Parallel
__Parallel = __Parallel
import com.badlogic.gdx.ai.btree.BranchTask as __BranchTask
__BranchTask = __BranchTask
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Parallel(ai.__BranchTask, btree.BranchTask):
    """com.badlogic.gdx.ai.btree.branch.Parallel"""
 
    @staticmethod
    def __wrap(java_value: __Parallel) -> 'Parallel':
        return Parallel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Parallel):
        """
        Dynamic initializer for Parallel.
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
    def success(self):
        """public final void com.badlogic.gdx.ai.btree.Task.success()"""
        super(btree.Task, self).success()

    @overload
    def __init__(self, arg0: 'Policy', arg1: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Policy,com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __Parallel(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Policy', *arg1: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Policy,com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = __Parallel(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Parallel, self).childSuccess(arg0)

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
    def __init__(self, *arg0: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = __Parallel(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __Parallel(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.branch.Parallel()"""
        val = __Parallel()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Policy'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Policy)"""
        val = __Parallel(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Parallel, self).childRunning(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Policy', arg1: 'Orchestrator', arg2: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Policy,com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator,com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __Parallel(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.resetTask()"""
        super(Parallel, self).resetTask()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.BranchTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.BranchTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setControl(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.cloneTask()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).cloneTask())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Orchestrator', arg1: 'Array'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator,com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.btree.Task<E>>)"""
        val = __Parallel(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def resetAllChildren(self):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.resetAllChildren()"""
        super(Parallel, self).resetAllChildren()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.run()"""
        super(Parallel, self).run()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.BranchTask.getChildCount()"""
        return int.__wrap(super(btree.BranchTask, self).getChildCount())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.branch.Parallel()"""
        val = __Parallel()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'.__wrap(super(btree.Task, self).getStatus())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setGuard(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Task.setGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setGuard(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

    @overload
    def __init__(self, arg0: 'Orchestrator', *arg1: 'btree.Task'):
        """public com.badlogic.gdx.ai.btree.branch.Parallel(com.badlogic.gdx.ai.btree.branch.Parallel$Orchestrator,com.badlogic.gdx.ai.btree.Task<E>...)"""
        val = __Parallel(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Parallel, self).childFail(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.branch.Parallel.reset()"""
        super(Parallel, self).reset()
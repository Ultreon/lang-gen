from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.ai.btree.leaf.Success as __Success
__Success = __Success
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
import com.badlogic.gdx.ai.btree.LeafTask as __LeafTask
__LeafTask = __LeafTask
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
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Success():
    """com.badlogic.gdx.ai.btree.leaf.Success"""
 
    @staticmethod
    def __wrap(java_value: __Success) -> 'Success':
        return Success(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Success):
        """
        Dynamic initializer for Success.
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
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(btree.Task, self).start()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(btree.Task, self).resetTask()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Task.reset()"""
        super(btree.Task, self).reset()

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

    @override
    @overload
    def execute(self) -> 'btree.Task$Status':
        """public com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.leaf.Success.execute()"""
        return 'btree.Task$Status'.__wrap(super(Success, self).execute())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childRunning(arg0, arg1)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setControl(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.leaf.Success()"""
        val = __Success()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.leaf.Success()"""
        val = __Success()
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
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childFail(arg0)

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.LeafTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int.__wrap(super(btree.LeafTask, self).getChildCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def run(self):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.run()"""
        super(btree.LeafTask, self).run()

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.leaf.Success
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.ai.btree.leaf.Success as __Success
__Success = __Success
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
import com.badlogic.gdx.ai.btree.LeafTask as __LeafTask
__LeafTask = __LeafTask
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
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Success():
    """com.badlogic.gdx.ai.btree.leaf.Success"""
 
    @staticmethod
    def __wrap(java_value: __Success) -> 'Success':
        return Success(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Success):
        """
        Dynamic initializer for Success.
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
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(btree.Task, self).start()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(btree.Task, self).resetTask()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Task.reset()"""
        super(btree.Task, self).reset()

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

    @override
    @overload
    def execute(self) -> 'btree.Task$Status':
        """public com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.leaf.Success.execute()"""
        return 'btree.Task$Status'.__wrap(super(Success, self).execute())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childRunning(arg0, arg1)

    @override
    @overload
    def setControl(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.Task.setControl(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Task, self).setControl(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.leaf.Success()"""
        val = __Success()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.leaf.Success()"""
        val = __Success()
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
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childFail(arg0)

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.LeafTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int.__wrap(super(btree.LeafTask, self).getChildCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def run(self):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.run()"""
        super(btree.LeafTask, self).run()

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.leaf.Success 
 
 
# CLASS: com.badlogic.gdx.ai.btree.leaf.Wait
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.btree.leaf.Wait as __Wait
__Wait = __Wait
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

import com.badlogic.gdx.ai.btree.LeafTask as __LeafTask
__LeafTask = __LeafTask
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Wait():
    """com.badlogic.gdx.ai.btree.leaf.Wait"""
 
    @staticmethod
    def __wrap(java_value: __Wait) -> 'Wait':
        return Wait(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Wait):
        """
        Dynamic initializer for Wait.
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
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(btree.Task, self).resetTask()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.leaf.Wait.start()"""
        super(Wait, self).start()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.leaf.Wait()"""
        val = __Wait()
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
    def __init__(self, arg0: 'FloatDistribution'):
        """public com.badlogic.gdx.ai.btree.leaf.Wait(com.badlogic.gdx.ai.utils.random.FloatDistribution)"""
        val = __Wait(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childRunning(arg0, arg1)

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
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.leaf.Wait.reset()"""
        super(Wait, self).reset()

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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.btree.leaf.Wait(float)"""
        val = __Wait(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def execute(self) -> 'btree.Task$Status':
        """public com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.leaf.Wait.execute()"""
        return 'btree.Task$Status'.__wrap(super(Wait, self).execute())

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
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childFail(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.leaf.Wait()"""
        val = __Wait()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.LeafTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int.__wrap(super(btree.LeafTask, self).getChildCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def run(self):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.run()"""
        super(btree.LeafTask, self).run() 
 
 
# CLASS: com.badlogic.gdx.ai.btree.leaf.Failure
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
import com.badlogic.gdx.ai.btree.leaf.Failure as __Failure
__Failure = __Failure
import com.badlogic.gdx.ai.btree.LeafTask as __LeafTask
__LeafTask = __LeafTask
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
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Failure():
    """com.badlogic.gdx.ai.btree.leaf.Failure"""
 
    @staticmethod
    def __wrap(java_value: __Failure) -> 'Failure':
        return Failure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Failure):
        """
        Dynamic initializer for Failure.
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
    def start(self):
        """public void com.badlogic.gdx.ai.btree.Task.start()"""
        super(btree.Task, self).start()

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.Task.resetTask()"""
        super(btree.Task, self).resetTask()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.leaf.Failure()"""
        val = __Failure()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Task.reset()"""
        super(btree.Task, self).reset()

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childRunning(arg0, arg1)

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

    @override
    @overload
    def execute(self) -> 'btree.Task$Status':
        """public com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.leaf.Failure.execute()"""
        return 'btree.Task$Status'.__wrap(super(Failure, self).execute())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.leaf.Failure()"""
        val = __Failure()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childFail(arg0)

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.LeafTask, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int.__wrap(super(btree.LeafTask, self).getChildCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def run(self):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.run()"""
        super(btree.LeafTask, self).run()
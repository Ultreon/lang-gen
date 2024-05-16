from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.btree.LeafTask as _LeafTask
_LeafTask = _LeafTask
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
try:
    from pygdx.ai.utils import random
except ImportError:
    random = _import_once("pygdx.ai.utils.random")

from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import com.badlogic.gdx.ai.btree.leaf.Wait as _Wait
_Wait = _Wait
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Wait():
    """com.badlogic.gdx.ai.btree.leaf.Wait"""
 
    @staticmethod
    def _wrap(java_value: _Wait) -> 'Wait':
        return Wait(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Wait):
        """
        Dynamic initializer for Wait.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Wait__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Wait__wrapper":
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

    @override
    @overload
    def execute(self) -> 'btree.Task$Status':
        """public com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.leaf.Wait.execute()"""
        return 'btree.Task$Status'._wrap(super(Wait, self).execute())

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
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.leaf.Wait.start()"""
        super(Wait, self).start()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childFail(arg0)

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childRunning(arg0, arg1)

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.btree.leaf.Wait(float)"""
        val = _Wait(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.leaf.Wait()"""
        val = _Wait()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.leaf.Wait.reset()"""
        super(Wait, self).reset()

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
    def __init__(self, arg0: 'FloatDistribution'):
        """public com.badlogic.gdx.ai.btree.leaf.Wait(com.badlogic.gdx.ai.utils.random.FloatDistribution)"""
        val = _Wait(arg0)
        self.__wrapper = val

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.LeafTask, self).getChild(_int.valueOf(arg0)))

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
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int._wrap(super(btree.LeafTask, self).getChildCount())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.leaf.Wait()"""
        val = _Wait()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def run(self):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.run()"""
        super(btree.LeafTask, self).run()

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

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.leaf.Wait
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.btree.LeafTask as _LeafTask
_LeafTask = _LeafTask
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
try:
    from pygdx.ai.utils import random
except ImportError:
    random = _import_once("pygdx.ai.utils.random")

from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import com.badlogic.gdx.ai.btree.leaf.Wait as _Wait
_Wait = _Wait
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Wait():
    """com.badlogic.gdx.ai.btree.leaf.Wait"""
 
    @staticmethod
    def _wrap(java_value: _Wait) -> 'Wait':
        return Wait(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Wait):
        """
        Dynamic initializer for Wait.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Wait__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Wait__wrapper":
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

    @override
    @overload
    def execute(self) -> 'btree.Task$Status':
        """public com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.leaf.Wait.execute()"""
        return 'btree.Task$Status'._wrap(super(Wait, self).execute())

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
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.leaf.Wait.start()"""
        super(Wait, self).start()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childFail(arg0)

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childRunning(arg0, arg1)

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.btree.leaf.Wait(float)"""
        val = _Wait(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.leaf.Wait()"""
        val = _Wait()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.leaf.Wait.reset()"""
        super(Wait, self).reset()

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
    def __init__(self, arg0: 'FloatDistribution'):
        """public com.badlogic.gdx.ai.btree.leaf.Wait(com.badlogic.gdx.ai.utils.random.FloatDistribution)"""
        val = _Wait(arg0)
        self.__wrapper = val

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.LeafTask, self).getChild(_int.valueOf(arg0)))

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
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int._wrap(super(btree.LeafTask, self).getChildCount())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.leaf.Wait()"""
        val = _Wait()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def run(self):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.run()"""
        super(btree.LeafTask, self).run()

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

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.leaf.Wait 
 
 
# CLASS: com.badlogic.gdx.ai.btree.leaf.Failure
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.btree.LeafTask as _LeafTask
_LeafTask = _LeafTask
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
import com.badlogic.gdx.ai.btree.leaf.Failure as _Failure
_Failure = _Failure
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Failure():
    """com.badlogic.gdx.ai.btree.leaf.Failure"""
 
    @staticmethod
    def _wrap(java_value: _Failure) -> 'Failure':
        return Failure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Failure):
        """
        Dynamic initializer for Failure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Failure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Failure__wrapper":
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

    @override
    @overload
    def execute(self) -> 'btree.Task$Status':
        """public com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.leaf.Failure.execute()"""
        return 'btree.Task$Status'._wrap(super(Failure, self).execute())

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
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Task.reset()"""
        super(btree.Task, self).reset()

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.leaf.Failure()"""
        val = _Failure()
        self.__wrapper = val

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childFail(arg0)

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childRunning(arg0, arg1)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

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
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.LeafTask, self).getChild(_int.valueOf(arg0)))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.leaf.Failure()"""
        val = _Failure()
        self.__wrapper = val

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int._wrap(super(btree.LeafTask, self).getChildCount())

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
        """public final void com.badlogic.gdx.ai.btree.LeafTask.run()"""
        super(btree.LeafTask, self).run()

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.leaf.Success
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.btree.LeafTask as _LeafTask
_LeafTask = _LeafTask
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
import com.badlogic.gdx.ai.btree.leaf.Success as _Success
_Success = _Success
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Success():
    """com.badlogic.gdx.ai.btree.leaf.Success"""
 
    @staticmethod
    def _wrap(java_value: _Success) -> 'Success':
        return Success(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Success):
        """
        Dynamic initializer for Success.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Success__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Success__wrapper":
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

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.leaf.Success()"""
        val = _Success()
        self.__wrapper = val

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
    def childSuccess(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childSuccess(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Task.reset()"""
        super(btree.Task, self).reset()

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childFail(arg0)

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public final void com.badlogic.gdx.ai.btree.LeafTask.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LeafTask, self).childRunning(arg0, arg1)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.leaf.Success()"""
        val = _Success()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def execute(self) -> 'btree.Task$Status':
        """public com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.leaf.Success.execute()"""
        return 'btree.Task$Status'._wrap(super(Success, self).execute())

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.LeafTask.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.LeafTask, self).getChild(_int.valueOf(arg0)))

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
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.LeafTask.getChildCount()"""
        return int._wrap(super(btree.LeafTask, self).getChildCount())

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
        """public final void com.badlogic.gdx.ai.btree.LeafTask.run()"""
        super(btree.LeafTask, self).run()

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
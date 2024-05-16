from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
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
import com.badlogic.gdx.ai.btree.decorator.UntilFail as __UntilFail
__UntilFail = __UntilFail
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
 
class UntilFail(ai.__LoopDecorator, btree.LoopDecorator):
    """com.badlogic.gdx.ai.btree.decorator.UntilFail"""
 
    @staticmethod
    def __wrap(java_value: __UntilFail) -> 'UntilFail':
        return UntilFail(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UntilFail):
        """
        Dynamic initializer for UntilFail.
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
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LoopDecorator, self).childRunning(arg0, arg1)

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
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

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
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.UntilFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __UntilFail(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.reset()"""
        super(btree.LoopDecorator, self).reset()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(btree.LoopDecorator, self).run()

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.UntilFail()"""
        val = __UntilFail()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'.__wrap(super(btree.Task, self).getStatus())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.UntilFail()"""
        val = __UntilFail()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilFail.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__UntilFail, self).childFail(arg0)

    @override
    @overload
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.LoopDecorator.condition()"""
        return bool.__wrap(super(btree.LoopDecorator, self).condition())

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilFail.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__UntilFail, self).childSuccess(arg0)

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.UntilFail
from pyquantum_helper import import_once as __import_once__
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
import com.badlogic.gdx.ai.btree.decorator.UntilFail as __UntilFail
__UntilFail = __UntilFail
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
 
class UntilFail(ai.__LoopDecorator, btree.LoopDecorator):
    """com.badlogic.gdx.ai.btree.decorator.UntilFail"""
 
    @staticmethod
    def __wrap(java_value: __UntilFail) -> 'UntilFail':
        return UntilFail(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UntilFail):
        """
        Dynamic initializer for UntilFail.
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
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LoopDecorator, self).childRunning(arg0, arg1)

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
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

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
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.UntilFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __UntilFail(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.reset()"""
        super(btree.LoopDecorator, self).reset()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(btree.LoopDecorator, self).run()

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.UntilFail()"""
        val = __UntilFail()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStatus(self) -> 'btree.Task$Status':
        """public final com.badlogic.gdx.ai.btree.Task$Status com.badlogic.gdx.ai.btree.Task.getStatus()"""
        return 'btree.Task$Status'.__wrap(super(btree.Task, self).getStatus())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.UntilFail()"""
        val = __UntilFail()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilFail.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__UntilFail, self).childFail(arg0)

    @override
    @overload
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.LoopDecorator.condition()"""
        return bool.__wrap(super(btree.LoopDecorator, self).condition())

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilFail.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__UntilFail, self).childSuccess(arg0)

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.UntilFail 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.Invert
from pyquantum_helper import import_once as __import_once__
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
import com.badlogic.gdx.ai.btree.decorator.Invert as __Invert
__Invert = __Invert
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
 
class Invert(ai.__Decorator, btree.Decorator):
    """com.badlogic.gdx.ai.btree.decorator.Invert"""
 
    @staticmethod
    def __wrap(java_value: __Invert) -> 'Invert':
        return Invert(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Invert):
        """
        Dynamic initializer for Invert.
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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.Invert()"""
        val = __Invert()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Invert(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __Invert(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Invert.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Invert, self).childFail(arg0)

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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(btree.Decorator, self).run()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Invert.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Invert, self).childSuccess(arg0)

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
        """public void com.badlogic.gdx.ai.btree.Decorator.reset()"""
        super(btree.Decorator, self).reset()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.Invert()"""
        val = __Invert()
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
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.AlwaysFail
from pyquantum_helper import import_once as __import_once__
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
import com.badlogic.gdx.ai.btree.decorator.AlwaysFail as __AlwaysFail
__AlwaysFail = __AlwaysFail
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
 
class AlwaysFail(ai.__Decorator, btree.Decorator):
    """com.badlogic.gdx.ai.btree.decorator.AlwaysFail"""
 
    @staticmethod
    def __wrap(java_value: __AlwaysFail) -> 'AlwaysFail':
        return AlwaysFail(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AlwaysFail):
        """
        Dynamic initializer for AlwaysFail.
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
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childFail(arg0)

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
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysFail()"""
        val = __AlwaysFail()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childRunning(arg0, arg1)

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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(btree.Decorator, self).run()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysFail()"""
        val = __AlwaysFail()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        """public void com.badlogic.gdx.ai.btree.Decorator.reset()"""
        super(btree.Decorator, self).reset()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.AlwaysFail.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__AlwaysFail, self).childSuccess(arg0)

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

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __AlwaysFail(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.Include
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.Decorator as __Decorator
__Decorator = __Decorator
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.decorator.Include as __Include
__Include = __Include
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
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
 
class Include(ai.__Decorator, btree.Decorator):
    """com.badlogic.gdx.ai.btree.decorator.Include"""
 
    @staticmethod
    def __wrap(java_value: __Include) -> 'Include':
        return Include(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Include):
        """
        Dynamic initializer for Include.
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
    def __init__(self, arg0: str, arg1: bool):
        """public com.badlogic.gdx.ai.btree.decorator.Include(java.lang.String,boolean)"""
        val = __Include(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.Include()"""
        val = __Include()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childFail(arg0)

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

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childRunning(arg0, arg1)

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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(btree.Decorator, self).run()

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.Include()"""
        val = __Include()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.decorator.Include(java.lang.String)"""
        val = __Include(arg0)
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
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Include.reset()"""
        super(Include, self).reset()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Include.start()"""
        super(Include, self).start()

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool.__wrap(super(__btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.decorator.Include.cloneTask()"""
        return 'btree.Task'.__wrap(super(Include, self).cloneTask())

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object.__wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childSuccess(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.Random
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.Decorator as __Decorator
__Decorator = __Decorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.ai.btree.decorator.Random as __Random
__Random = __Random
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

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
 
class Random(ai.__Decorator, btree.Decorator):
    """com.badlogic.gdx.ai.btree.decorator.Random"""
 
    @staticmethod
    def __wrap(java_value: __Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Random):
        """
        Dynamic initializer for Random.
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

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Random(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __Random(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.run()"""
        super(Random, self).run()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.reset()"""
        super(Random, self).reset()

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
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Random, self).childFail(arg0)

    @overload
    def __init__(self, arg0: 'FloatDistribution'):
        """public com.badlogic.gdx.ai.btree.decorator.Random(com.badlogic.gdx.ai.utils.random.FloatDistribution)"""
        val = __Random(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'FloatDistribution', arg1: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Random(com.badlogic.gdx.ai.utils.random.FloatDistribution,com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __Random(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.start()"""
        super(Random, self).start()

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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.Random()"""
        val = __Random()
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
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Random, self).childSuccess(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.Random()"""
        val = __Random()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.Repeat
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.Decorator as __Decorator
__Decorator = __Decorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.decorator.Repeat as __Repeat
__Repeat = __Repeat
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

from builtins import object
import com.badlogic.gdx.ai.btree.LoopDecorator as __LoopDecorator
__LoopDecorator = __LoopDecorator
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
 
class Repeat(ai.__LoopDecorator, btree.LoopDecorator):
    """com.badlogic.gdx.ai.btree.decorator.Repeat"""
 
    @staticmethod
    def __wrap(java_value: __Repeat) -> 'Repeat':
        return Repeat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Repeat):
        """
        Dynamic initializer for Repeat.
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
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LoopDecorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Repeat.start()"""
        super(Repeat, self).start()

    @override
    @overload
    def fail(self):
        """public final void com.badlogic.gdx.ai.btree.Task.fail()"""
        super(btree.Task, self).fail()

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Repeat(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __Repeat(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

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
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Repeat.reset()"""
        super(Repeat, self).reset()

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
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Repeat.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Repeat, self).childSuccess(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'IntegerDistribution', arg1: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Repeat(com.badlogic.gdx.ai.utils.random.IntegerDistribution,com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __Repeat(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(btree.LoopDecorator, self).run()

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'.__wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.decorator.Repeat.condition()"""
        return bool.__wrap(super(Repeat, self).condition())

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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.Repeat()"""
        val = __Repeat()
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
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Repeat.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Repeat, self).childFail(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.Repeat()"""
        val = __Repeat()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.Decorator as __Decorator
__Decorator = __Decorator
import com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard as __SemaphoreGuard
__SemaphoreGuard = __SemaphoreGuard
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
import java.lang.String as __string
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
 
class SemaphoreGuard(ai.__Decorator, btree.Decorator):
    """com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard"""
 
    @staticmethod
    def __wrap(java_value: __SemaphoreGuard) -> 'SemaphoreGuard':
        return SemaphoreGuard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SemaphoreGuard):
        """
        Dynamic initializer for SemaphoreGuard.
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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard()"""
        val = __SemaphoreGuard()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childFail(arg0)

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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.run()"""
        super(SemaphoreGuard, self).run()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard()"""
        val = __SemaphoreGuard()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.end()"""
        super(SemaphoreGuard, self).end()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.start()"""
        super(SemaphoreGuard, self).start()

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childRunning(arg0, arg1)

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
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.resetTask()"""
        super(SemaphoreGuard, self).resetTask()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

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
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.reset()"""
        super(SemaphoreGuard, self).reset()

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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard(java.lang.String)"""
        val = __SemaphoreGuard(arg0)
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
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childSuccess(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard(java.lang.String,com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __SemaphoreGuard(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __SemaphoreGuard(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed
from pyquantum_helper import import_once as __import_once__
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
import com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed as __AlwaysSucceed
__AlwaysSucceed = __AlwaysSucceed
from builtins import int
 
class AlwaysSucceed(ai.__Decorator, btree.Decorator):
    """com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed"""
 
    @staticmethod
    def __wrap(java_value: __AlwaysSucceed) -> 'AlwaysSucceed':
        return AlwaysSucceed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AlwaysSucceed):
        """
        Dynamic initializer for AlwaysSucceed.
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
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed()"""
        val = __AlwaysSucceed()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childRunning(arg0, arg1)

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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(btree.Decorator, self).run()

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
        """public void com.badlogic.gdx.ai.btree.Decorator.reset()"""
        super(btree.Decorator, self).reset()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__AlwaysSucceed, self).childFail(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed()"""
        val = __AlwaysSucceed()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.Decorator, self).childSuccess(arg0)

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __AlwaysSucceed(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.UntilSuccess
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.Decorator as __Decorator
__Decorator = __Decorator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as __Task_Status
__Status = __Task_Status.Status
from builtins import object
import com.badlogic.gdx.ai.btree.decorator.UntilSuccess as __UntilSuccess
__UntilSuccess = __UntilSuccess
import com.badlogic.gdx.ai.btree.LoopDecorator as __LoopDecorator
__LoopDecorator = __LoopDecorator
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
 
class UntilSuccess(ai.__LoopDecorator, btree.LoopDecorator):
    """com.badlogic.gdx.ai.btree.decorator.UntilSuccess"""
 
    @staticmethod
    def __wrap(java_value: __UntilSuccess) -> 'UntilSuccess':
        return UntilSuccess(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UntilSuccess):
        """
        Dynamic initializer for UntilSuccess.
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
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__btree.LoopDecorator, self).childRunning(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.UntilSuccess()"""
        val = __UntilSuccess()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'.__wrap(super(__btree.Decorator, self).getChild(__int.valueOf(arg0)))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.Task.end()"""
        super(btree.Task, self).end()

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.UntilSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = __UntilSuccess(arg0)
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
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int.__wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilSuccess.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__UntilSuccess, self).childFail(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.reset()"""
        super(btree.LoopDecorator, self).reset()

    @overload
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int.__wrap(super(__btree.Task, self).addChild(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.UntilSuccess()"""
        val = __UntilSuccess()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(btree.LoopDecorator, self).run()

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
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilSuccess.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__UntilSuccess, self).childSuccess(arg0)

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
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.LoopDecorator.condition()"""
        return bool.__wrap(super(btree.LoopDecorator, self).condition())
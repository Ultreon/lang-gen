from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
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
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.LoopDecorator as _LoopDecorator
_LoopDecorator = _LoopDecorator
import com.badlogic.gdx.ai.btree.decorator.UntilSuccess as _UntilSuccess
_UntilSuccess = _UntilSuccess
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UntilSuccess():
    """com.badlogic.gdx.ai.btree.decorator.UntilSuccess"""
 
    @staticmethod
    def _wrap(java_value: _UntilSuccess) -> 'UntilSuccess':
        return UntilSuccess(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UntilSuccess):
        """
        Dynamic initializer for UntilSuccess.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UntilSuccess__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UntilSuccess__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.UntilSuccess()"""
        val = _UntilSuccess()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.UntilSuccess()"""
        val = _UntilSuccess()
        self.__wrapper = val

    @override
    @overload
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.LoopDecorator.condition()"""
        return bool._wrap(super(btree.LoopDecorator, self).condition())

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LoopDecorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilSuccess.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_UntilSuccess, self).childSuccess(arg0)

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilSuccess.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_UntilSuccess, self).childFail(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.reset()"""
        super(btree.LoopDecorator, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(btree.LoopDecorator, self).run()

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
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.UntilSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _UntilSuccess(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

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

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.UntilSuccess
from pyquantum_helper import import_once as _import_once
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
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.LoopDecorator as _LoopDecorator
_LoopDecorator = _LoopDecorator
import com.badlogic.gdx.ai.btree.decorator.UntilSuccess as _UntilSuccess
_UntilSuccess = _UntilSuccess
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UntilSuccess():
    """com.badlogic.gdx.ai.btree.decorator.UntilSuccess"""
 
    @staticmethod
    def _wrap(java_value: _UntilSuccess) -> 'UntilSuccess':
        return UntilSuccess(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UntilSuccess):
        """
        Dynamic initializer for UntilSuccess.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UntilSuccess__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UntilSuccess__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.UntilSuccess()"""
        val = _UntilSuccess()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.UntilSuccess()"""
        val = _UntilSuccess()
        self.__wrapper = val

    @override
    @overload
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.LoopDecorator.condition()"""
        return bool._wrap(super(btree.LoopDecorator, self).condition())

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LoopDecorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilSuccess.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_UntilSuccess, self).childSuccess(arg0)

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilSuccess.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_UntilSuccess, self).childFail(arg0)

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.reset()"""
        super(btree.LoopDecorator, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(btree.LoopDecorator, self).run()

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
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.UntilSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _UntilSuccess(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

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

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.UntilSuccess 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed as _AlwaysSucceed
_AlwaysSucceed = _AlwaysSucceed
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AlwaysSucceed():
    """com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed"""
 
    @staticmethod
    def _wrap(java_value: _AlwaysSucceed) -> 'AlwaysSucceed':
        return AlwaysSucceed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AlwaysSucceed):
        """
        Dynamic initializer for AlwaysSucceed.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AlwaysSucceed__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AlwaysSucceed__wrapper":
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed()"""
        val = _AlwaysSucceed()
        self.__wrapper = val

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
        """public void com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_AlwaysSucceed, self).childFail(arg0)

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

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _AlwaysSucceed(arg0)
        self.__wrapper = val

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childSuccess(arg0)

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(btree.Decorator, self).run()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.reset()"""
        super(btree.Decorator, self).reset()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysSucceed()"""
        val = _AlwaysSucceed()
        self.__wrapper = val

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
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.AlwaysFail
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.Task as _Task_Status
_Status = _Task_Status.Status
import com.badlogic.gdx.ai.btree.decorator.AlwaysFail as _AlwaysFail
_AlwaysFail = _AlwaysFail
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Decorator as _Decorator
_Decorator = _Decorator
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
 
class AlwaysFail():
    """com.badlogic.gdx.ai.btree.decorator.AlwaysFail"""
 
    @staticmethod
    def _wrap(java_value: _AlwaysFail) -> 'AlwaysFail':
        return AlwaysFail(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AlwaysFail):
        """
        Dynamic initializer for AlwaysFail.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AlwaysFail__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AlwaysFail__wrapper":
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
        """public void com.badlogic.gdx.ai.btree.decorator.AlwaysFail.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_AlwaysFail, self).childSuccess(arg0)

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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(btree.Decorator, self).run()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.reset()"""
        super(btree.Decorator, self).reset()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childFail(arg0)

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
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _AlwaysFail(arg0)
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysFail()"""
        val = _AlwaysFail()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.AlwaysFail()"""
        val = _AlwaysFail()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.Random
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
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
import com.badlogic.gdx.ai.btree.decorator.Random as _Random
_Random = _Random
import com.badlogic.gdx.ai.btree.Decorator as _Decorator
_Decorator = _Decorator
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
 
class Random():
    """com.badlogic.gdx.ai.btree.decorator.Random"""
 
    @staticmethod
    def _wrap(java_value: _Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Random):
        """
        Dynamic initializer for Random.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Random__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Random__wrapper":
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
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Random, self).childFail(arg0)

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
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.run()"""
        super(Random, self).run()

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
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.reset()"""
        super(Random, self).reset()

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
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Random, self).childSuccess(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Random(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _Random(arg0)
        self.__wrapper = val

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Random.start()"""
        super(Random, self).start()

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.Random()"""
        val = _Random()
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

    @overload
    def __init__(self, arg0: 'FloatDistribution', arg1: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Random(com.badlogic.gdx.ai.utils.random.FloatDistribution,com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _Random(arg0, arg1)
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'FloatDistribution'):
        """public com.badlogic.gdx.ai.btree.decorator.Random(com.badlogic.gdx.ai.utils.random.FloatDistribution)"""
        val = _Random(arg0)
        self.__wrapper = val

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.Random()"""
        val = _Random()
        self.__wrapper = val

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.Include
from pyquantum_helper import import_once as _import_once
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
import java.lang.String as _string
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.decorator.Include as _Include
_Include = _Include
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Include():
    """com.badlogic.gdx.ai.btree.decorator.Include"""
 
    @staticmethod
    def _wrap(java_value: _Include) -> 'Include':
        return Include(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Include):
        """
        Dynamic initializer for Include.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Include__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Include__wrapper":
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
    def addChild(self, arg0: 'Task') -> int:
        """public final int com.badlogic.gdx.ai.btree.Task.addChild(com.badlogic.gdx.ai.btree.Task<E>)"""
        return int._wrap(super(_btree.Task, self).addChild(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.Include()"""
        val = _Include()
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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.decorator.Include(java.lang.String)"""
        val = _Include(arg0)
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.Include()"""
        val = _Include()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childSuccess(arg0)

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(btree.Decorator, self).run()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: bool):
        """public com.badlogic.gdx.ai.btree.decorator.Include(java.lang.String,boolean)"""
        val = _Include(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childFail(arg0)

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
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Include.reset()"""
        super(Include, self).reset()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Include.start()"""
        super(Include, self).start()

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
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def cloneTask(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.decorator.Include.cloneTask()"""
        return 'btree.Task'._wrap(super(Include, self).cloneTask())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.Invert
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.ai.btree.decorator.Invert as _Invert
_Invert = _Invert
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
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Invert():
    """com.badlogic.gdx.ai.btree.decorator.Invert"""
 
    @staticmethod
    def _wrap(java_value: _Invert) -> 'Invert':
        return Invert(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Invert):
        """
        Dynamic initializer for Invert.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Invert__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Invert__wrapper":
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
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Invert(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _Invert(arg0)
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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.run()"""
        super(btree.Decorator, self).run()

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.Decorator.reset()"""
        super(btree.Decorator, self).reset()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.Invert()"""
        val = _Invert()
        self.__wrapper = val

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Invert.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Invert, self).childSuccess(arg0)

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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.Invert()"""
        val = _Invert()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Invert.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Invert, self).childFail(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.UntilFail
from pyquantum_helper import import_once as _import_once
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
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.LoopDecorator as _LoopDecorator
_LoopDecorator = _LoopDecorator
import com.badlogic.gdx.ai.btree.decorator.UntilFail as _UntilFail
_UntilFail = _UntilFail
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UntilFail():
    """com.badlogic.gdx.ai.btree.decorator.UntilFail"""
 
    @staticmethod
    def _wrap(java_value: _UntilFail) -> 'UntilFail':
        return UntilFail(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UntilFail):
        """
        Dynamic initializer for UntilFail.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UntilFail__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UntilFail__wrapper":
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

    @overload
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.UntilFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _UntilFail(arg0)
        self.__wrapper = val

    @override
    @overload
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.LoopDecorator.condition()"""
        return bool._wrap(super(btree.LoopDecorator, self).condition())

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
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LoopDecorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.UntilFail()"""
        val = _UntilFail()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.reset()"""
        super(btree.LoopDecorator, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(btree.LoopDecorator, self).run()

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilFail.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_UntilFail, self).childFail(arg0)

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
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.UntilFail.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_UntilFail, self).childSuccess(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.UntilFail()"""
        val = _UntilFail()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.Repeat
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.ai.btree.decorator.Repeat as _Repeat
_Repeat = _Repeat
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
import com.badlogic.gdx.ai.btree.Decorator as _Decorator
_Decorator = _Decorator
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import com.badlogic.gdx.ai.btree.LoopDecorator as _LoopDecorator
_LoopDecorator = _LoopDecorator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Repeat():
    """com.badlogic.gdx.ai.btree.decorator.Repeat"""
 
    @staticmethod
    def _wrap(java_value: _Repeat) -> 'Repeat':
        return Repeat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Repeat):
        """
        Dynamic initializer for Repeat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Repeat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Repeat__wrapper":
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
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Repeat(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _Repeat(arg0)
        self.__wrapper = val

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
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Repeat.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Repeat, self).childSuccess(arg0)

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
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.decorator.Repeat.reset()"""
        super(Repeat, self).reset()

    @override
    @overload
    def condition(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.decorator.Repeat.condition()"""
        return bool._wrap(super(Repeat, self).condition())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.LoopDecorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.LoopDecorator.run()"""
        super(btree.LoopDecorator, self).run()

    @overload
    def checkGuard(self, arg0: 'Task') -> bool:
        """public boolean com.badlogic.gdx.ai.btree.Task.checkGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        return bool._wrap(super(_btree.Task, self).checkGuard(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'IntegerDistribution', arg1: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.Repeat(com.badlogic.gdx.ai.utils.random.IntegerDistribution,com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _Repeat(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def cancel(self):
        """public final void com.badlogic.gdx.ai.btree.Task.cancel()"""
        super(btree.Task, self).cancel()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.Repeat()"""
        val = _Repeat()
        self.__wrapper = val

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
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.Repeat()"""
        val = _Repeat()
        self.__wrapper = val

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.decorator.Repeat.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Repeat, self).childFail(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard as _SemaphoreGuard
_SemaphoreGuard = _SemaphoreGuard
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
import java.lang.String as _string
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
 
class SemaphoreGuard():
    """com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard"""
 
    @staticmethod
    def _wrap(java_value: _SemaphoreGuard) -> 'SemaphoreGuard':
        return SemaphoreGuard(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SemaphoreGuard):
        """
        Dynamic initializer for SemaphoreGuard.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SemaphoreGuard__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SemaphoreGuard__wrapper":
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
    def __init__(self, arg0: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard(com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _SemaphoreGuard(arg0)
        self.__wrapper = val

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
    def run(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.run()"""
        super(SemaphoreGuard, self).run()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.end()"""
        super(SemaphoreGuard, self).end()

    @override
    @overload
    def getObject(self) -> object:
        """public E com.badlogic.gdx.ai.btree.Task.getObject()"""
        return object._wrap(super(btree.Task, self).getObject())

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.start()"""
        super(SemaphoreGuard, self).start()

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

    @overload
    def __init__(self, arg0: str, arg1: 'Task'):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard(java.lang.String,com.badlogic.gdx.ai.btree.Task<E>)"""
        val = _SemaphoreGuard(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def childSuccess(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childSuccess(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childSuccess(arg0)

    @override
    @overload
    def running(self):
        """public final void com.badlogic.gdx.ai.btree.Task.running()"""
        super(btree.Task, self).running()

    @overload
    def getChild(self, arg0: int) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Decorator.getChild(int)"""
        return 'btree.Task'._wrap(super(_btree.Decorator, self).getChild(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard()"""
        val = _SemaphoreGuard()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def resetTask(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.resetTask()"""
        super(SemaphoreGuard, self).resetTask()

    @override
    @overload
    def childFail(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childFail(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childFail(arg0)

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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard(java.lang.String)"""
        val = _SemaphoreGuard(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard()"""
        val = _SemaphoreGuard()
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.btree.decorator.SemaphoreGuard.reset()"""
        super(SemaphoreGuard, self).reset()

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
    def getChildCount(self) -> int:
        """public int com.badlogic.gdx.ai.btree.Decorator.getChildCount()"""
        return int._wrap(super(btree.Decorator, self).getChildCount())

    @override
    @overload
    def getGuard(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.Task.getGuard()"""
        return 'btree.Task'._wrap(super(btree.Task, self).getGuard())

    @override
    @overload
    def childRunning(self, arg0: 'Task', arg1: 'Task'):
        """public void com.badlogic.gdx.ai.btree.Decorator.childRunning(com.badlogic.gdx.ai.btree.Task<E>,com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_btree.Decorator, self).childRunning(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())
from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.ai.sched.LoadBalancingScheduler as __LoadBalancingScheduler
__LoadBalancingScheduler = __LoadBalancingScheduler
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoadBalancingScheduler(__SchedulerBase, SchedulerBase):
    """com.badlogic.gdx.ai.sched.LoadBalancingScheduler"""
 
    @staticmethod
    def __wrap(java_value: __LoadBalancingScheduler) -> 'LoadBalancingScheduler':
        return LoadBalancingScheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadBalancingScheduler):
        """
        Dynamic initializer for LoadBalancingScheduler.
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        super(__LoadBalancingScheduler, self).addWithAutomaticPhasing(arg0, __int.valueOf(arg1))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        super(__LoadBalancingScheduler, self).add(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.sched.LoadBalancingScheduler(int)"""
        val = __LoadBalancingScheduler(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def run(self, arg0: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.run(long)"""
        super(__LoadBalancingScheduler, self).run(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.sched.LoadBalancingScheduler
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.ai.sched.LoadBalancingScheduler as __LoadBalancingScheduler
__LoadBalancingScheduler = __LoadBalancingScheduler
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoadBalancingScheduler(__SchedulerBase, SchedulerBase):
    """com.badlogic.gdx.ai.sched.LoadBalancingScheduler"""
 
    @staticmethod
    def __wrap(java_value: __LoadBalancingScheduler) -> 'LoadBalancingScheduler':
        return LoadBalancingScheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadBalancingScheduler):
        """
        Dynamic initializer for LoadBalancingScheduler.
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        super(__LoadBalancingScheduler, self).addWithAutomaticPhasing(arg0, __int.valueOf(arg1))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        super(__LoadBalancingScheduler, self).add(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.sched.LoadBalancingScheduler(int)"""
        val = __LoadBalancingScheduler(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def run(self, arg0: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.run(long)"""
        super(__LoadBalancingScheduler, self).run(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.sched.LoadBalancingScheduler 
 
 
# CLASS: com.badlogic.gdx.ai.sched.Schedulable
import com.badlogic.gdx.ai.sched.Schedulable as __Schedulable
__Schedulable = __Schedulable
from abc import abstractmethod, ABC
 
class Schedulable(ABC):
    """com.badlogic.gdx.ai.sched.Schedulable"""
 
    @staticmethod
    def __wrap(java_value: __Schedulable) -> 'Schedulable':
        return Schedulable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Schedulable):
        """
        Dynamic initializer for Schedulable.
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
    def run(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.sched.Schedulable.run(long)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.sched.Scheduler
import com.badlogic.gdx.ai.sched.Schedulable as __Schedulable
__Schedulable = __Schedulable
import com.badlogic.gdx.ai.sched.Scheduler as __Scheduler
__Scheduler = __Scheduler
from abc import abstractmethod, ABC
 
class Scheduler(ABC, __Schedulable, Schedulable):
    """com.badlogic.gdx.ai.sched.Scheduler"""
 
    @staticmethod
    def __wrap(java_value: __Scheduler) -> 'Scheduler':
        return Scheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Scheduler):
        """
        Dynamic initializer for Scheduler.
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
    def run(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.sched.Schedulable.run(long)"""
        pass

    @abstractmethod
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public abstract void com.badlogic.gdx.ai.sched.Scheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        pass

    @abstractmethod
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.ai.sched.Scheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.sched.SchedulerBase
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.sched.Schedulable as __Schedulable
__Schedulable = __Schedulable
import com.badlogic.gdx.ai.sched.Scheduler as __Scheduler
__Scheduler = __Scheduler
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.sched.SchedulerBase as __SchedulerBase
__SchedulerBase = __SchedulerBase
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SchedulerBase(ABC, __Scheduler, Scheduler):
    """com.badlogic.gdx.ai.sched.SchedulerBase"""
 
    @staticmethod
    def __wrap(java_value: __SchedulerBase) -> 'SchedulerBase':
        return SchedulerBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SchedulerBase):
        """
        Dynamic initializer for SchedulerBase.
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

    @abstractmethod
    def run(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.sched.Schedulable.run(long)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public abstract void com.badlogic.gdx.ai.sched.Scheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        pass

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

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.sched.SchedulerBase(int)"""
        val = __SchedulerBase(__int.valueOf(arg0))
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.ai.sched.Scheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.sched.PriorityScheduler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.sched.PriorityScheduler as __PriorityScheduler
__PriorityScheduler = __PriorityScheduler
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
 
class PriorityScheduler(__SchedulerBase, SchedulerBase):
    """com.badlogic.gdx.ai.sched.PriorityScheduler"""
 
    @staticmethod
    def __wrap(java_value: __PriorityScheduler) -> 'PriorityScheduler':
        return PriorityScheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PriorityScheduler):
        """
        Dynamic initializer for PriorityScheduler.
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def run(self, arg0: int):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.run(long)"""
        super(__PriorityScheduler, self).run(__long.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int, arg3: float):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int,float)"""
        super(__PriorityScheduler, self).add(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.sched.PriorityScheduler(int)"""
        val = __PriorityScheduler(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        super(__PriorityScheduler, self).add(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

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
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        super(__PriorityScheduler, self).addWithAutomaticPhasing(arg0, __int.valueOf(arg1))

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
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int, arg2: float):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int,float)"""
        super(__PriorityScheduler, self).addWithAutomaticPhasing(arg0, __int.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.sched.SchedulerBase$SchedulableRecord
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.ai.sched.SchedulerBase as __SchedulerBase_SchedulableRecord
__SchedulableRecord = __SchedulerBase_SchedulableRecord.SchedulableRecord
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SchedulableRecord():
    """com.badlogic.gdx.ai.sched.SchedulerBase.SchedulableRecord"""
 
    @staticmethod
    def __wrap(java_value: __SchedulableRecord) -> 'SchedulableRecord':
        return SchedulableRecord(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SchedulableRecord):
        """
        Dynamic initializer for SchedulableRecord.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))
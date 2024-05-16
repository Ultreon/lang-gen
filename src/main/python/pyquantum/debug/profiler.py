from __future__ import annotations
from overload import overload


 
from builtins import str
import dev.ultreon.quantum.debug.profiler.ProfileData as _ProfileData
_ProfileData = _ProfileData
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import dev.ultreon.quantum.debug.profiler.Profiler as _Profiler
_Profiler = _Profiler
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Profiler():
    """dev.ultreon.quantum.debug.profiler.Profiler"""
 
    @staticmethod
    def _wrap(java_value: _Profiler) -> 'Profiler':
        return Profiler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Profiler):
        """
        Dynamic initializer for Profiler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Profiler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Profiler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def update(self):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.update()"""
        super(Profiler, self).update()

    @overload
    def collect(self) -> 'ProfileData':
        """public dev.ultreon.quantum.debug.profiler.ProfileData dev.ultreon.quantum.debug.profiler.Profiler.collect()"""
        return 'ProfileData'._wrap(super(Profiler, self).collect())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def section(self, arg0: str, arg1: 'Runnable'):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.section(java.lang.String,java.lang.Runnable)"""
        super(_Profiler, self).section(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setProfiling(self, arg0: bool):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.setProfiling(boolean)"""
        super(_Profiler, self).setProfiling(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.profiler.Profiler()"""
        val = _Profiler()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.profiler.Profiler()"""
        val = _Profiler()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isProfiling(self) -> bool:
        """public boolean dev.ultreon.quantum.debug.profiler.Profiler.isProfiling()"""
        return bool._wrap(super(Profiler, self).isProfiling())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.dispose()"""
        super(Profiler, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.Profiler
from builtins import str
import dev.ultreon.quantum.debug.profiler.ProfileData as _ProfileData
_ProfileData = _ProfileData
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import dev.ultreon.quantum.debug.profiler.Profiler as _Profiler
_Profiler = _Profiler
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Profiler():
    """dev.ultreon.quantum.debug.profiler.Profiler"""
 
    @staticmethod
    def _wrap(java_value: _Profiler) -> 'Profiler':
        return Profiler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Profiler):
        """
        Dynamic initializer for Profiler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Profiler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Profiler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def update(self):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.update()"""
        super(Profiler, self).update()

    @overload
    def collect(self) -> 'ProfileData':
        """public dev.ultreon.quantum.debug.profiler.ProfileData dev.ultreon.quantum.debug.profiler.Profiler.collect()"""
        return 'ProfileData'._wrap(super(Profiler, self).collect())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def section(self, arg0: str, arg1: 'Runnable'):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.section(java.lang.String,java.lang.Runnable)"""
        super(_Profiler, self).section(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setProfiling(self, arg0: bool):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.setProfiling(boolean)"""
        super(_Profiler, self).setProfiling(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.profiler.Profiler()"""
        val = _Profiler()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.profiler.Profiler()"""
        val = _Profiler()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isProfiling(self) -> bool:
        """public boolean dev.ultreon.quantum.debug.profiler.Profiler.isProfiling()"""
        return bool._wrap(super(Profiler, self).isProfiling())

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.dispose()"""
        super(Profiler, self).dispose()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.Profiler 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.ProfileData
import java.lang.Thread as Thread
from builtins import str
import dev.ultreon.quantum.debug.profiler.ProfileData as _ProfileData
_ProfileData = _ProfileData
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import dev.ultreon.quantum.debug.profiler.Section as _Section_FinishedSection
_FinishedSection = _Section_FinishedSection.FinishedSection
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import dev.ultreon.quantum.debug.profiler.ThreadSection as _ThreadSection_FinishedThreadSection
_FinishedThreadSection = _ThreadSection_FinishedThreadSection.FinishedThreadSection
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ProfileData():
    """dev.ultreon.quantum.debug.profiler.ProfileData"""
 
    @staticmethod
    def _wrap(java_value: _ProfileData) -> 'ProfileData':
        return ProfileData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProfileData):
        """
        Dynamic initializer for ProfileData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProfileData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProfileData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getThreads(self) -> 'Set':
        """public java.util.Set<java.lang.Thread> dev.ultreon.quantum.debug.profiler.ProfileData.getThreads()"""
        return 'Set'._wrap(super(ProfileData, self).getThreads())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.quantum.debug.profiler.ProfileData(java.util.Map<java.lang.Thread, dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection>)"""
        val = _ProfileData(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getThreadSection(self, arg0: 'Thread') -> 'FinishedThreadSection':
        """public dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection dev.ultreon.quantum.debug.profiler.ProfileData.getThreadSection(java.lang.Thread)"""
        return 'FinishedThreadSection'._wrap(super(_ProfileData, self).getThreadSection(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSection(self, arg0: 'FinishedThreadSection', arg1: str) -> 'FinishedSection':
        """public dev.ultreon.quantum.debug.profiler.Section$FinishedSection dev.ultreon.quantum.debug.profiler.ProfileData.getSection(dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection,java.lang.String)"""
        return 'FinishedSection'._wrap(super(_ProfileData, self).getSection(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.Section
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import dev.ultreon.quantum.debug.profiler.Section as _Section
_Section = _Section
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Section():
    """dev.ultreon.quantum.debug.profiler.Section"""
 
    @staticmethod
    def _wrap(java_value: _Section) -> 'Section':
        return Section(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Section):
        """
        Dynamic initializer for Section.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Section__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Section__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getStart(self) -> int:
        """public long dev.ultreon.quantum.debug.profiler.Section.getStart()"""
        return int._wrap(super(Section, self).getStart())

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.profiler.Section.getName()"""
        return str._wrap(super(Section, self).getName())

    @overload
    def hasCurrent(self) -> bool:
        """public boolean dev.ultreon.quantum.debug.profiler.Section.hasCurrent()"""
        return bool._wrap(super(Section, self).hasCurrent())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getEnd(self) -> int:
        """public long dev.ultreon.quantum.debug.profiler.Section.getEnd()"""
        return int._wrap(super(Section, self).getEnd())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getNanos(self) -> int:
        """public long dev.ultreon.quantum.debug.profiler.Section.getNanos()"""
        return int._wrap(super(Section, self).getNanos())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section> dev.ultreon.quantum.debug.profiler.Section.getData()"""
        return 'Map'._wrap(super(Section, self).getData())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.profiler.Section.toString()"""
        return str._wrap(super(Section, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def collect(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section$FinishedSection> dev.ultreon.quantum.debug.profiler.Section.collect()"""
        return 'Map'._wrap(super(Section, self).collect())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: 'Profiler'):
        """public dev.ultreon.quantum.debug.profiler.Section(java.lang.String,dev.ultreon.quantum.debug.profiler.Profiler)"""
        val = _Section(arg0, arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import dev.ultreon.quantum.debug.profiler.ThreadSection as _ThreadSection_FinishedThreadSection
_FinishedThreadSection = _ThreadSection_FinishedThreadSection.FinishedThreadSection
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FinishedThreadSection():
    """dev.ultreon.quantum.debug.profiler.ThreadSection.FinishedThreadSection"""
 
    @staticmethod
    def _wrap(java_value: _FinishedThreadSection) -> 'FinishedThreadSection':
        return FinishedThreadSection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FinishedThreadSection):
        """
        Dynamic initializer for FinishedThreadSection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FinishedThreadSection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FinishedThreadSection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def create(arg0: 'ThreadSection') -> 'FinishedThreadSection':
        """public static dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection.create(dev.ultreon.quantum.debug.profiler.ThreadSection)"""
        return FinishedThreadSection._wrap(_FinishedThreadSection.create(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section$FinishedSection> dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection.getData()"""
        return 'Map'._wrap(super(FinishedThreadSection, self).getData())

    @overload
    def __init__(self, arg0: 'ThreadSection'):
        """public dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection(dev.ultreon.quantum.debug.profiler.ThreadSection)"""
        val = _FinishedThreadSection(arg0)
        self.__wrapper = val

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.ThreadSection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.debug.profiler.ThreadSection as _ThreadSection
_ThreadSection = _ThreadSection
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThreadSection():
    """dev.ultreon.quantum.debug.profiler.ThreadSection"""
 
    @staticmethod
    def _wrap(java_value: _ThreadSection) -> 'ThreadSection':
        return ThreadSection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadSection):
        """
        Dynamic initializer for ThreadSection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadSection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadSection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Profiler'):
        """public dev.ultreon.quantum.debug.profiler.ThreadSection(dev.ultreon.quantum.debug.profiler.Profiler)"""
        val = _ThreadSection(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section> dev.ultreon.quantum.debug.profiler.ThreadSection.getData()"""
        return 'Map'._wrap(super(ThreadSection, self).getData())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.Section$FinishedSection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.debug.profiler.Section as _Section_FinishedSection
_FinishedSection = _Section_FinishedSection.FinishedSection
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FinishedSection():
    """dev.ultreon.quantum.debug.profiler.Section.FinishedSection"""
 
    @staticmethod
    def _wrap(java_value: _FinishedSection) -> 'FinishedSection':
        return FinishedSection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FinishedSection):
        """
        Dynamic initializer for FinishedSection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FinishedSection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FinishedSection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getNanos(self) -> int:
        """public long dev.ultreon.quantum.debug.profiler.Section$FinishedSection.getNanos()"""
        return int._wrap(super(FinishedSection, self).getNanos())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section$FinishedSection> dev.ultreon.quantum.debug.profiler.Section$FinishedSection.getData()"""
        return 'Map'._wrap(super(FinishedSection, self).getData())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Section'):
        """public dev.ultreon.quantum.debug.profiler.Section$FinishedSection(dev.ultreon.quantum.debug.profiler.Section)"""
        val = _FinishedSection(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.profiler.Section$FinishedSection.getName()"""
        return str._wrap(super(FinishedSection, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())
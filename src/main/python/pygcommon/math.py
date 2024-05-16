from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Double as _double
import com.google.common.math.StatsAccumulator as _StatsAccumulator
_StatsAccumulator = _StatsAccumulator
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import com.google.common.math.Stats as _Stats
_Stats = _Stats
import java.lang.Integer as _int
import java.util.stream.LongStream as LongStream
import java.util.stream.DoubleStream as DoubleStream
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StatsAccumulator():
    """com.google.common.math.StatsAccumulator"""
 
    @staticmethod
    def _wrap(java_value: _StatsAccumulator) -> 'StatsAccumulator':
        return StatsAccumulator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StatsAccumulator):
        """
        Dynamic initializer for StatsAccumulator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StatsAccumulator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StatsAccumulator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def snapshot(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.StatsAccumulator.snapshot()"""
        return 'Stats'._wrap(super(StatsAccumulator, self).snapshot())

    @overload
    def sampleStandardDeviation(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.sampleStandardDeviation()"""
        return float._wrap(super(StatsAccumulator, self).sampleStandardDeviation())

    @overload
    def max(self) -> float:
        """public double com.google.common.math.StatsAccumulator.max()"""
        return float._wrap(super(StatsAccumulator, self).max())

    @overload
    def populationStandardDeviation(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.populationStandardDeviation()"""
        return float._wrap(super(StatsAccumulator, self).populationStandardDeviation())

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.google.common.math.StatsAccumulator()"""
        val = _StatsAccumulator()
        self.__wrapper = val

    @overload
    def addAll(self, values: 'IntStream'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.stream.IntStream)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def addAll(self, values: 'LongStream'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.stream.LongStream)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def count(self) -> int:
        """public long com.google.common.math.StatsAccumulator.count()"""
        return int._wrap(super(StatsAccumulator, self).count())

    @overload
    def addAll(self, values: 'DoubleStream'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.stream.DoubleStream)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def populationVariance(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.populationVariance()"""
        return float._wrap(super(StatsAccumulator, self).populationVariance())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def addAll(self, *values: int):
        """public void com.google.common.math.StatsAccumulator.addAll(long...)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def addAll(self, *values: float):
        """public void com.google.common.math.StatsAccumulator.addAll(double...)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def addAll(self, values: 'Iterable'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.lang.Iterable<? extends java.lang.Number>)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def addAll(self, *values: int):
        """public void com.google.common.math.StatsAccumulator.addAll(int...)"""
        super(_StatsAccumulator, self).addAll(values)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, value: float):
        """public void com.google.common.math.StatsAccumulator.add(double)"""
        super(_StatsAccumulator, self).add(_double.valueOf(value))

    @overload
    def addAll(self, values: 'Iterator'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.Iterator<? extends java.lang.Number>)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def __init__(self):
        """public com.google.common.math.StatsAccumulator()"""
        val = _StatsAccumulator()
        self.__wrapper = val

    @overload
    def addAll(self, values: 'Stats'):
        """public void com.google.common.math.StatsAccumulator.addAll(com.google.common.math.Stats)"""
        super(_StatsAccumulator, self).addAll(values)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def addAll(self, values: 'StatsAccumulator'):
        """public void com.google.common.math.StatsAccumulator.addAll(com.google.common.math.StatsAccumulator)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def sum(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.sum()"""
        return float._wrap(super(StatsAccumulator, self).sum())

    @overload
    def min(self) -> float:
        """public double com.google.common.math.StatsAccumulator.min()"""
        return float._wrap(super(StatsAccumulator, self).min())

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
    def sampleVariance(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.sampleVariance()"""
        return float._wrap(super(StatsAccumulator, self).sampleVariance())

    @overload
    def mean(self) -> float:
        """public double com.google.common.math.StatsAccumulator.mean()"""
        return float._wrap(super(StatsAccumulator, self).mean())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.math.StatsAccumulator
from builtins import str
import java.lang.Double as _double
import com.google.common.math.StatsAccumulator as _StatsAccumulator
_StatsAccumulator = _StatsAccumulator
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import com.google.common.math.Stats as _Stats
_Stats = _Stats
import java.lang.Integer as _int
import java.util.stream.LongStream as LongStream
import java.util.stream.DoubleStream as DoubleStream
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StatsAccumulator():
    """com.google.common.math.StatsAccumulator"""
 
    @staticmethod
    def _wrap(java_value: _StatsAccumulator) -> 'StatsAccumulator':
        return StatsAccumulator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StatsAccumulator):
        """
        Dynamic initializer for StatsAccumulator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StatsAccumulator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StatsAccumulator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def snapshot(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.StatsAccumulator.snapshot()"""
        return 'Stats'._wrap(super(StatsAccumulator, self).snapshot())

    @overload
    def sampleStandardDeviation(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.sampleStandardDeviation()"""
        return float._wrap(super(StatsAccumulator, self).sampleStandardDeviation())

    @overload
    def max(self) -> float:
        """public double com.google.common.math.StatsAccumulator.max()"""
        return float._wrap(super(StatsAccumulator, self).max())

    @overload
    def populationStandardDeviation(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.populationStandardDeviation()"""
        return float._wrap(super(StatsAccumulator, self).populationStandardDeviation())

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.google.common.math.StatsAccumulator()"""
        val = _StatsAccumulator()
        self.__wrapper = val

    @overload
    def addAll(self, values: 'IntStream'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.stream.IntStream)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def addAll(self, values: 'LongStream'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.stream.LongStream)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def count(self) -> int:
        """public long com.google.common.math.StatsAccumulator.count()"""
        return int._wrap(super(StatsAccumulator, self).count())

    @overload
    def addAll(self, values: 'DoubleStream'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.stream.DoubleStream)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def populationVariance(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.populationVariance()"""
        return float._wrap(super(StatsAccumulator, self).populationVariance())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def addAll(self, *values: int):
        """public void com.google.common.math.StatsAccumulator.addAll(long...)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def addAll(self, *values: float):
        """public void com.google.common.math.StatsAccumulator.addAll(double...)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def addAll(self, values: 'Iterable'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.lang.Iterable<? extends java.lang.Number>)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def addAll(self, *values: int):
        """public void com.google.common.math.StatsAccumulator.addAll(int...)"""
        super(_StatsAccumulator, self).addAll(values)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def add(self, value: float):
        """public void com.google.common.math.StatsAccumulator.add(double)"""
        super(_StatsAccumulator, self).add(_double.valueOf(value))

    @overload
    def addAll(self, values: 'Iterator'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.Iterator<? extends java.lang.Number>)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def __init__(self):
        """public com.google.common.math.StatsAccumulator()"""
        val = _StatsAccumulator()
        self.__wrapper = val

    @overload
    def addAll(self, values: 'Stats'):
        """public void com.google.common.math.StatsAccumulator.addAll(com.google.common.math.Stats)"""
        super(_StatsAccumulator, self).addAll(values)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def addAll(self, values: 'StatsAccumulator'):
        """public void com.google.common.math.StatsAccumulator.addAll(com.google.common.math.StatsAccumulator)"""
        super(_StatsAccumulator, self).addAll(values)

    @overload
    def sum(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.sum()"""
        return float._wrap(super(StatsAccumulator, self).sum())

    @overload
    def min(self) -> float:
        """public double com.google.common.math.StatsAccumulator.min()"""
        return float._wrap(super(StatsAccumulator, self).min())

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
    def sampleVariance(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.sampleVariance()"""
        return float._wrap(super(StatsAccumulator, self).sampleVariance())

    @overload
    def mean(self) -> float:
        """public double com.google.common.math.StatsAccumulator.mean()"""
        return float._wrap(super(StatsAccumulator, self).mean())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.math.StatsAccumulator 
 
 
# CLASS: com.google.common.math.Quantiles$Scale
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.math.Quantiles as _Quantiles_Scale
_Scale = _Quantiles_Scale.Scale
import com.google.common.math.Quantiles as _Quantiles_ScaleAndIndex
_ScaleAndIndex = _Quantiles_ScaleAndIndex.ScaleAndIndex
from builtins import bool
import com.google.common.math.Quantiles as _Quantiles_ScaleAndIndexes
_ScaleAndIndexes = _Quantiles_ScaleAndIndexes.ScaleAndIndexes
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Scale():
    """com.google.common.math.Quantiles.Scale"""
 
    @staticmethod
    def _wrap(java_value: _Scale) -> 'Scale':
        return Scale(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Scale):
        """
        Dynamic initializer for Scale.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Scale__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Scale__wrapper":
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def index(self, index: int) -> 'ScaleAndIndex':
        """public com.google.common.math.Quantiles$ScaleAndIndex com.google.common.math.Quantiles$Scale.index(int)"""
        return 'ScaleAndIndex'._wrap(super(_Scale, self).index(_int.valueOf(index)))

    @overload
    def indexes(self, indexes: 'Collection') -> 'ScaleAndIndexes':
        """public com.google.common.math.Quantiles$ScaleAndIndexes com.google.common.math.Quantiles$Scale.indexes(java.util.Collection<java.lang.Integer>)"""
        return 'ScaleAndIndexes'._wrap(super(_Scale, self).indexes(indexes))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def indexes(self, *indexes: int) -> 'ScaleAndIndexes':
        """public com.google.common.math.Quantiles$ScaleAndIndexes com.google.common.math.Quantiles$Scale.indexes(int...)"""
        return 'ScaleAndIndexes'._wrap(super(_Scale, self).indexes(indexes))

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
 
 
# CLASS: com.google.common.math.Quantiles$ScaleAndIndex
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.math.Quantiles as _Quantiles_ScaleAndIndex
_ScaleAndIndex = _Quantiles_ScaleAndIndex.ScaleAndIndex
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScaleAndIndex():
    """com.google.common.math.Quantiles.ScaleAndIndex"""
 
    @staticmethod
    def _wrap(java_value: _ScaleAndIndex) -> 'ScaleAndIndex':
        return ScaleAndIndex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScaleAndIndex):
        """
        Dynamic initializer for ScaleAndIndex.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScaleAndIndex__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScaleAndIndex__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def compute(self, *dataset: int) -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.compute(long...)"""
        return float._wrap(super(_ScaleAndIndex, self).compute(dataset))

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

    @overload
    def compute(self, *dataset: int) -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.compute(int...)"""
        return float._wrap(super(_ScaleAndIndex, self).compute(dataset))

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
    def computeInPlace(self, *dataset: float) -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.computeInPlace(double...)"""
        return float._wrap(super(_ScaleAndIndex, self).computeInPlace(dataset))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compute(self, dataset: 'Collection') -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.compute(java.util.Collection<? extends java.lang.Number>)"""
        return float._wrap(super(_ScaleAndIndex, self).compute(dataset))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compute(self, *dataset: float) -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.compute(double...)"""
        return float._wrap(super(_ScaleAndIndex, self).compute(dataset))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.math.PairedStatsAccumulator
import com.google.common.math.LinearTransformation as _LinearTransformation
_LinearTransformation = _LinearTransformation
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.google.common.math.PairedStats as _PairedStats
_PairedStats = _PairedStats
import com.google.common.math.Stats as _Stats
_Stats = _Stats
import java.lang.Integer as _int
import com.google.common.math.PairedStatsAccumulator as _PairedStatsAccumulator
_PairedStatsAccumulator = _PairedStatsAccumulator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PairedStatsAccumulator():
    """com.google.common.math.PairedStatsAccumulator"""
 
    @staticmethod
    def _wrap(java_value: _PairedStatsAccumulator) -> 'PairedStatsAccumulator':
        return PairedStatsAccumulator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PairedStatsAccumulator):
        """
        Dynamic initializer for PairedStatsAccumulator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PairedStatsAccumulator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PairedStatsAccumulator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.google.common.math.PairedStatsAccumulator()"""
        val = _PairedStatsAccumulator()
        self.__wrapper = val

    @overload
    def add(self, x: float, y: float):
        """public void com.google.common.math.PairedStatsAccumulator.add(double,double)"""
        super(_PairedStatsAccumulator, self).add(_double.valueOf(x), _double.valueOf(y))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def leastSquaresFit(self) -> 'LinearTransformation':
        """public final com.google.common.math.LinearTransformation com.google.common.math.PairedStatsAccumulator.leastSquaresFit()"""
        return 'LinearTransformation'._wrap(super(PairedStatsAccumulator, self).leastSquaresFit())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def sampleCovariance(self) -> float:
        """public final double com.google.common.math.PairedStatsAccumulator.sampleCovariance()"""
        return float._wrap(super(PairedStatsAccumulator, self).sampleCovariance())

    @overload
    def yStats(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.PairedStatsAccumulator.yStats()"""
        return 'Stats'._wrap(super(PairedStatsAccumulator, self).yStats())

    @overload
    def populationCovariance(self) -> float:
        """public double com.google.common.math.PairedStatsAccumulator.populationCovariance()"""
        return float._wrap(super(PairedStatsAccumulator, self).populationCovariance())

    @overload
    def pearsonsCorrelationCoefficient(self) -> float:
        """public final double com.google.common.math.PairedStatsAccumulator.pearsonsCorrelationCoefficient()"""
        return float._wrap(super(PairedStatsAccumulator, self).pearsonsCorrelationCoefficient())

    @overload
    def xStats(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.PairedStatsAccumulator.xStats()"""
        return 'Stats'._wrap(super(PairedStatsAccumulator, self).xStats())

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
    def count(self) -> int:
        """public long com.google.common.math.PairedStatsAccumulator.count()"""
        return int._wrap(super(PairedStatsAccumulator, self).count())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.google.common.math.PairedStatsAccumulator()"""
        val = _PairedStatsAccumulator()
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
    def addAll(self, values: 'PairedStats'):
        """public void com.google.common.math.PairedStatsAccumulator.addAll(com.google.common.math.PairedStats)"""
        super(_PairedStatsAccumulator, self).addAll(values)

    @overload
    def snapshot(self) -> 'PairedStats':
        """public com.google.common.math.PairedStats com.google.common.math.PairedStatsAccumulator.snapshot()"""
        return 'PairedStats'._wrap(super(PairedStatsAccumulator, self).snapshot())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.math.BigDecimalMath
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.google.common.math.BigDecimalMath as _BigDecimalMath
_BigDecimalMath = _BigDecimalMath
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.math.RoundingMode as RoundingMode
import java.math.BigDecimal as BigDecimal
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BigDecimalMath():
    """com.google.common.math.BigDecimalMath"""
 
    @staticmethod
    def _wrap(java_value: _BigDecimalMath) -> 'BigDecimalMath':
        return BigDecimalMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BigDecimalMath):
        """
        Dynamic initializer for BigDecimalMath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BigDecimalMath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BigDecimalMath__wrapper":
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
    def roundToDouble(x: 'BigDecimal', mode: 'RoundingMode') -> float:
        """public static double com.google.common.math.BigDecimalMath.roundToDouble(java.math.BigDecimal,java.math.RoundingMode)"""
        return float._wrap(_BigDecimalMath.roundToDouble(x, mode))

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
 
 
# CLASS: com.google.common.math.Stats
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.stream.Collector as Collector
import java.util.Iterator as Iterator
import java.util.stream.Collector as _Collector
_Collector = _Collector
from typing import List
import com.google.common.math.Stats as _Stats
_Stats = _Stats
import java.lang.Integer as _int
import java.util.stream.LongStream as LongStream
import java.util.stream.DoubleStream as DoubleStream
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Stats():
    """com.google.common.math.Stats"""
 
    @staticmethod
    def _wrap(java_value: _Stats) -> 'Stats':
        return Stats(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Stats):
        """
        Dynamic initializer for Stats.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Stats__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Stats__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def meanOf(values: 'Iterator') -> float:
        """public static double com.google.common.math.Stats.meanOf(java.util.Iterator<? extends java.lang.Number>)"""
        return float._wrap(_Stats.meanOf(values))

    @staticmethod
    @overload
    def meanOf(values: 'Iterable') -> float:
        """public static double com.google.common.math.Stats.meanOf(java.lang.Iterable<? extends java.lang.Number>)"""
        return float._wrap(_Stats.meanOf(values))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.math.Stats.toString()"""
        return str._wrap(super(Stats, self).toString())

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.math.Stats.equals(java.lang.Object)"""
        return bool._wrap(super(_Stats, self).equals(obj))

    @staticmethod
    @overload
    def meanOf(*values: float) -> float:
        """public static double com.google.common.math.Stats.meanOf(double...)"""
        return float._wrap(_Stats.meanOf(values))

    @overload
    def toByteArray(self) -> List[int]:
        """public byte[] com.google.common.math.Stats.toByteArray()"""
        return List[int]._wrap(super(Stats, self).toByteArray())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def of(*values: float) -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(double...)"""
        return Stats._wrap(_Stats.of(values))

    @overload
    def sampleVariance(self) -> float:
        """public double com.google.common.math.Stats.sampleVariance()"""
        return float._wrap(super(Stats, self).sampleVariance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def max(self) -> float:
        """public double com.google.common.math.Stats.max()"""
        return float._wrap(super(Stats, self).max())

    @staticmethod
    @overload
    def fromByteArray(byteArray: bytes) -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.fromByteArray(byte[])"""
        return Stats._wrap(_Stats.fromByteArray(bytes))

    @overload
    def populationStandardDeviation(self) -> float:
        """public double com.google.common.math.Stats.populationStandardDeviation()"""
        return float._wrap(super(Stats, self).populationStandardDeviation())

    @staticmethod
    @overload
    def of(*values: int) -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(int...)"""
        return Stats._wrap(_Stats.of(values))

    @staticmethod
    @overload
    def toStats() -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Number, com.google.common.math.StatsAccumulator, com.google.common.math.Stats> com.google.common.math.Stats.toStats()"""
        return Collector._wrap(_Stats.toStats())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.math.Stats.hashCode()"""
        return int._wrap(super(Stats, self).hashCode())

    @staticmethod
    @overload
    def of(values: 'LongStream') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.util.stream.LongStream)"""
        return Stats._wrap(_Stats.of(values))

    @staticmethod
    @overload
    def of(values: 'Iterable') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.lang.Iterable<? extends java.lang.Number>)"""
        return Stats._wrap(_Stats.of(values))

    @overload
    def sum(self) -> float:
        """public double com.google.common.math.Stats.sum()"""
        return float._wrap(super(Stats, self).sum())

    @overload
    def populationVariance(self) -> float:
        """public double com.google.common.math.Stats.populationVariance()"""
        return float._wrap(super(Stats, self).populationVariance())

    @staticmethod
    @overload
    def meanOf(*values: int) -> float:
        """public static double com.google.common.math.Stats.meanOf(int...)"""
        return float._wrap(_Stats.meanOf(values))

    @overload
    def sampleStandardDeviation(self) -> float:
        """public double com.google.common.math.Stats.sampleStandardDeviation()"""
        return float._wrap(super(Stats, self).sampleStandardDeviation())

    @staticmethod
    @overload
    def of(values: 'Iterator') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.util.Iterator<? extends java.lang.Number>)"""
        return Stats._wrap(_Stats.of(values))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def mean(self) -> float:
        """public double com.google.common.math.Stats.mean()"""
        return float._wrap(super(Stats, self).mean())

    @overload
    def min(self) -> float:
        """public double com.google.common.math.Stats.min()"""
        return float._wrap(super(Stats, self).min())

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

    @staticmethod
    @overload
    def of(*values: int) -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(long...)"""
        return Stats._wrap(_Stats.of(values))

    @staticmethod
    @overload
    def meanOf(*values: int) -> float:
        """public static double com.google.common.math.Stats.meanOf(long...)"""
        return float._wrap(_Stats.meanOf(values))

    @overload
    def count(self) -> int:
        """public long com.google.common.math.Stats.count()"""
        return int._wrap(super(Stats, self).count())

    @staticmethod
    @overload
    def of(values: 'IntStream') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.util.stream.IntStream)"""
        return Stats._wrap(_Stats.of(values))

    @staticmethod
    @overload
    def of(values: 'DoubleStream') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.util.stream.DoubleStream)"""
        return Stats._wrap(_Stats.of(values)) 
 
 
# CLASS: com.google.common.math.PairedStats
from builtins import str
import com.google.common.math.LinearTransformation as _LinearTransformation
_LinearTransformation = _LinearTransformation
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import com.google.common.math.PairedStats as _PairedStats
_PairedStats = _PairedStats
import com.google.common.math.Stats as _Stats
_Stats = _Stats
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PairedStats():
    """com.google.common.math.PairedStats"""
 
    @staticmethod
    def _wrap(java_value: _PairedStats) -> 'PairedStats':
        return PairedStats(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PairedStats):
        """
        Dynamic initializer for PairedStats.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PairedStats__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PairedStats__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def count(self) -> int:
        """public long com.google.common.math.PairedStats.count()"""
        return int._wrap(super(PairedStats, self).count())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.math.PairedStats.hashCode()"""
        return int._wrap(super(PairedStats, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def populationCovariance(self) -> float:
        """public double com.google.common.math.PairedStats.populationCovariance()"""
        return float._wrap(super(PairedStats, self).populationCovariance())

    @overload
    def sampleCovariance(self) -> float:
        """public double com.google.common.math.PairedStats.sampleCovariance()"""
        return float._wrap(super(PairedStats, self).sampleCovariance())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.math.PairedStats.equals(java.lang.Object)"""
        return bool._wrap(super(_PairedStats, self).equals(obj))

    @overload
    def toByteArray(self) -> List[int]:
        """public byte[] com.google.common.math.PairedStats.toByteArray()"""
        return List[int]._wrap(super(PairedStats, self).toByteArray())

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
    def pearsonsCorrelationCoefficient(self) -> float:
        """public double com.google.common.math.PairedStats.pearsonsCorrelationCoefficient()"""
        return float._wrap(super(PairedStats, self).pearsonsCorrelationCoefficient())

    @overload
    def yStats(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.PairedStats.yStats()"""
        return 'Stats'._wrap(super(PairedStats, self).yStats())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.math.PairedStats.toString()"""
        return str._wrap(super(PairedStats, self).toString())

    @staticmethod
    @overload
    def fromByteArray(byteArray: bytes) -> 'PairedStats':
        """public static com.google.common.math.PairedStats com.google.common.math.PairedStats.fromByteArray(byte[])"""
        return PairedStats._wrap(_PairedStats.fromByteArray(bytes))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def xStats(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.PairedStats.xStats()"""
        return 'Stats'._wrap(super(PairedStats, self).xStats())

    @overload
    def leastSquaresFit(self) -> 'LinearTransformation':
        """public com.google.common.math.LinearTransformation com.google.common.math.PairedStats.leastSquaresFit()"""
        return 'LinearTransformation'._wrap(super(PairedStats, self).leastSquaresFit()) 
 
 
# CLASS: com.google.common.math.LongMath
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.google.common.math.LongMath as _LongMath
_LongMath = _LongMath
import java.lang.Integer as _int
import java.math.RoundingMode as RoundingMode
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LongMath():
    """com.google.common.math.LongMath"""
 
    @staticmethod
    def _wrap(java_value: _LongMath) -> 'LongMath':
        return LongMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongMath):
        """
        Dynamic initializer for LongMath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongMath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongMath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def checkedMultiply(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.checkedMultiply(long,long)"""
        return int._wrap(_LongMath.checkedMultiply(_long.valueOf(a), _long.valueOf(b)))

    @staticmethod
    @overload
    def saturatedAdd(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.saturatedAdd(long,long)"""
        return int._wrap(_LongMath.saturatedAdd(_long.valueOf(a), _long.valueOf(b)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def checkedSubtract(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.checkedSubtract(long,long)"""
        return int._wrap(_LongMath.checkedSubtract(_long.valueOf(a), _long.valueOf(b)))

    @staticmethod
    @overload
    def isPowerOfTwo(x: int) -> bool:
        """public static boolean com.google.common.math.LongMath.isPowerOfTwo(long)"""
        return bool._wrap(_LongMath.isPowerOfTwo(_long.valueOf(x)))

    @staticmethod
    @overload
    def mean(x: int, y: int) -> int:
        """public static long com.google.common.math.LongMath.mean(long,long)"""
        return int._wrap(_LongMath.mean(_long.valueOf(x), _long.valueOf(y)))

    @staticmethod
    @overload
    def saturatedPow(b: int, k: int) -> int:
        """public static long com.google.common.math.LongMath.saturatedPow(long,int)"""
        return int._wrap(_LongMath.saturatedPow(_long.valueOf(b), _int.valueOf(k)))

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
    def saturatedSubtract(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.saturatedSubtract(long,long)"""
        return int._wrap(_LongMath.saturatedSubtract(_long.valueOf(a), _long.valueOf(b)))

    @staticmethod
    @overload
    def isPrime(n: int) -> bool:
        """public static boolean com.google.common.math.LongMath.isPrime(long)"""
        return bool._wrap(_LongMath.isPrime(_long.valueOf(n)))

    @staticmethod
    @overload
    def mod(x: int, m: int) -> int:
        """public static int com.google.common.math.LongMath.mod(long,int)"""
        return int._wrap(_LongMath.mod(_long.valueOf(x), _int.valueOf(m)))

    @staticmethod
    @overload
    def mod(x: int, m: int) -> int:
        """public static long com.google.common.math.LongMath.mod(long,long)"""
        return int._wrap(_LongMath.mod(_long.valueOf(x), _long.valueOf(m)))

    @staticmethod
    @overload
    def pow(b: int, k: int) -> int:
        """public static long com.google.common.math.LongMath.pow(long,int)"""
        return int._wrap(_LongMath.pow(_long.valueOf(b), _int.valueOf(k)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def binomial(n: int, k: int) -> int:
        """public static long com.google.common.math.LongMath.binomial(int,int)"""
        return int._wrap(_LongMath.binomial(_int.valueOf(n), _int.valueOf(k)))

    @staticmethod
    @overload
    def ceilingPowerOfTwo(x: int) -> int:
        """public static long com.google.common.math.LongMath.ceilingPowerOfTwo(long)"""
        return int._wrap(_LongMath.ceilingPowerOfTwo(_long.valueOf(x)))

    @staticmethod
    @overload
    def saturatedMultiply(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.saturatedMultiply(long,long)"""
        return int._wrap(_LongMath.saturatedMultiply(_long.valueOf(a), _long.valueOf(b)))

    @staticmethod
    @overload
    def log2(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.LongMath.log2(long,java.math.RoundingMode)"""
        return int._wrap(_LongMath.log2(_long.valueOf(x), mode))

    @staticmethod
    @overload
    def checkedPow(b: int, k: int) -> int:
        """public static long com.google.common.math.LongMath.checkedPow(long,int)"""
        return int._wrap(_LongMath.checkedPow(_long.valueOf(b), _int.valueOf(k)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def sqrt(x: int, mode: 'RoundingMode') -> int:
        """public static long com.google.common.math.LongMath.sqrt(long,java.math.RoundingMode)"""
        return int._wrap(_LongMath.sqrt(_long.valueOf(x), mode))

    @staticmethod
    @overload
    def gcd(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.gcd(long,long)"""
        return int._wrap(_LongMath.gcd(_long.valueOf(a), _long.valueOf(b)))

    @staticmethod
    @overload
    def factorial(n: int) -> int:
        """public static long com.google.common.math.LongMath.factorial(int)"""
        return int._wrap(_LongMath.factorial(_int.valueOf(n)))

    @staticmethod
    @overload
    def checkedAdd(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.checkedAdd(long,long)"""
        return int._wrap(_LongMath.checkedAdd(_long.valueOf(a), _long.valueOf(b)))

    @staticmethod
    @overload
    def roundToDouble(x: int, mode: 'RoundingMode') -> float:
        """public static double com.google.common.math.LongMath.roundToDouble(long,java.math.RoundingMode)"""
        return float._wrap(_LongMath.roundToDouble(_long.valueOf(x), mode))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def log10(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.LongMath.log10(long,java.math.RoundingMode)"""
        return int._wrap(_LongMath.log10(_long.valueOf(x), mode))

    @staticmethod
    @overload
    def floorPowerOfTwo(x: int) -> int:
        """public static long com.google.common.math.LongMath.floorPowerOfTwo(long)"""
        return int._wrap(_LongMath.floorPowerOfTwo(_long.valueOf(x)))

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

    @staticmethod
    @overload
    def divide(p: int, q: int, mode: 'RoundingMode') -> int:
        """public static long com.google.common.math.LongMath.divide(long,long,java.math.RoundingMode)"""
        return int._wrap(_LongMath.divide(_long.valueOf(p), _long.valueOf(q), mode))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.math.Quantiles$ScaleAndIndexes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
from builtins import float
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import com.google.common.math.Quantiles as _Quantiles_ScaleAndIndexes
_ScaleAndIndexes = _Quantiles_ScaleAndIndexes.ScaleAndIndexes
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScaleAndIndexes():
    """com.google.common.math.Quantiles.ScaleAndIndexes"""
 
    @staticmethod
    def _wrap(java_value: _ScaleAndIndexes) -> 'ScaleAndIndexes':
        return ScaleAndIndexes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScaleAndIndexes):
        """
        Dynamic initializer for ScaleAndIndexes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScaleAndIndexes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScaleAndIndexes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def compute(self, *dataset: int) -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.compute(long...)"""
        return 'Map'._wrap(super(_ScaleAndIndexes, self).compute(dataset))

    @overload
    def computeInPlace(self, *dataset: float) -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.computeInPlace(double...)"""
        return 'Map'._wrap(super(_ScaleAndIndexes, self).computeInPlace(dataset))

    @overload
    def compute(self, *dataset: float) -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.compute(double...)"""
        return 'Map'._wrap(super(_ScaleAndIndexes, self).compute(dataset))

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

    @overload
    def compute(self, *dataset: int) -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.compute(int...)"""
        return 'Map'._wrap(super(_ScaleAndIndexes, self).compute(dataset))

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
    def compute(self, dataset: 'Collection') -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.compute(java.util.Collection<? extends java.lang.Number>)"""
        return 'Map'._wrap(super(_ScaleAndIndexes, self).compute(dataset))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.math.BigIntegerMath
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.math.BigIntegerMath as _BigIntegerMath
_BigIntegerMath = _BigIntegerMath
from builtins import float
import java.lang.String as _String
_String = _String
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import java.math.RoundingMode as RoundingMode
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BigIntegerMath():
    """com.google.common.math.BigIntegerMath"""
 
    @staticmethod
    def _wrap(java_value: _BigIntegerMath) -> 'BigIntegerMath':
        return BigIntegerMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BigIntegerMath):
        """
        Dynamic initializer for BigIntegerMath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BigIntegerMath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BigIntegerMath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def factorial(factorial) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.factorial(int)"""
        return _transform(__int.valueOf(n).BigIntegerMath(n: int)).'BigInteger'Value()

    @staticmethod
    @overload
    def isPowerOfTwo(x: 'BigInteger') -> bool:
        """public static boolean com.google.common.math.BigIntegerMath.isPowerOfTwo(java.math.BigInteger)"""
        return bool._wrap(_BigIntegerMath.isPowerOfTwo(x))

    @staticmethod
    @overload
    def log10(x: 'BigInteger', mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.BigIntegerMath.log10(java.math.BigInteger,java.math.RoundingMode)"""
        return int._wrap(_BigIntegerMath.log10(x, mode))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def roundToDouble(x: 'BigInteger', mode: 'RoundingMode') -> float:
        """public static double com.google.common.math.BigIntegerMath.roundToDouble(java.math.BigInteger,java.math.RoundingMode)"""
        return float._wrap(_BigIntegerMath.roundToDouble(x, mode))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def floorPowerOfTwo(floorPowerOfTwo) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.floorPowerOfTwo(java.math.BigInteger)"""
        return _transform(_x.BigIntegerMath(x: 'BigInteger')).'BigInteger'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def ceilingPowerOfTwo(ceilingPowerOfTwo) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.ceilingPowerOfTwo(java.math.BigInteger)"""
        return _transform(_x.BigIntegerMath(x: 'BigInteger')).'BigInteger'Value()

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
    def divide(divide) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.divide(java.math.BigInteger,java.math.BigInteger,java.math.RoundingMode)"""
        return _transform(_p, q, mode.BigIntegerMath(p: 'BigInteger', q: 'BigInteger', mode: 'RoundingMode')).'BigInteger'Value()

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

    @staticmethod
    @overload
    def binomial(binomial) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.binomial(int,int)"""
        return _transform(__int.valueOf(n), _int.valueOf(k).BigIntegerMath(n: int, k: int)).'BigInteger'Value()

    @staticmethod
    @overload
    def log2(x: 'BigInteger', mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.BigIntegerMath.log2(java.math.BigInteger,java.math.RoundingMode)"""
        return int._wrap(_BigIntegerMath.log2(x, mode))

    @staticmethod
    @overload
    def sqrt(sqrt) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.sqrt(java.math.BigInteger,java.math.RoundingMode)"""
        return _transform(_x, mode.BigIntegerMath(x: 'BigInteger', mode: 'RoundingMode')).'BigInteger'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.math.Quantiles
from builtins import str
from pyquantum_helper import override
import com.google.common.math.Quantiles as _Quantiles
_Quantiles = _Quantiles
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.math.Quantiles as _Quantiles_Scale
_Scale = _Quantiles_Scale.Scale
import com.google.common.math.Quantiles as _Quantiles_ScaleAndIndex
_ScaleAndIndex = _Quantiles_ScaleAndIndex.ScaleAndIndex
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Quantiles():
    """com.google.common.math.Quantiles"""
 
    @staticmethod
    def _wrap(java_value: _Quantiles) -> 'Quantiles':
        return Quantiles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Quantiles):
        """
        Dynamic initializer for Quantiles.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Quantiles__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Quantiles__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.google.common.math.Quantiles()"""
        val = _Quantiles()
        self.__wrapper = val

    @staticmethod
    @overload
    def quartiles() -> 'Scale':
        """public static com.google.common.math.Quantiles$Scale com.google.common.math.Quantiles.quartiles()"""
        return Scale._wrap(_Quantiles.quartiles())

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
    def __init__(self):
        """public com.google.common.math.Quantiles()"""
        val = _Quantiles()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def percentiles() -> 'Scale':
        """public static com.google.common.math.Quantiles$Scale com.google.common.math.Quantiles.percentiles()"""
        return Scale._wrap(_Quantiles.percentiles())

    @staticmethod
    @overload
    def median() -> 'ScaleAndIndex':
        """public static com.google.common.math.Quantiles$ScaleAndIndex com.google.common.math.Quantiles.median()"""
        return ScaleAndIndex._wrap(_Quantiles.median())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def scale(scale: int) -> 'Scale':
        """public static com.google.common.math.Quantiles$Scale com.google.common.math.Quantiles.scale(int)"""
        return Scale._wrap(_Quantiles.scale(_int.valueOf(scale)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.math.IntMath
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.math.IntMath as _IntMath
_IntMath = _IntMath
import java.lang.Integer as _int
import java.math.RoundingMode as RoundingMode
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntMath():
    """com.google.common.math.IntMath"""
 
    @staticmethod
    def _wrap(java_value: _IntMath) -> 'IntMath':
        return IntMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntMath):
        """
        Dynamic initializer for IntMath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntMath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntMath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isPowerOfTwo(x: int) -> bool:
        """public static boolean com.google.common.math.IntMath.isPowerOfTwo(int)"""
        return bool._wrap(_IntMath.isPowerOfTwo(_int.valueOf(x)))

    @staticmethod
    @overload
    def divide(p: int, q: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.IntMath.divide(int,int,java.math.RoundingMode)"""
        return int._wrap(_IntMath.divide(_int.valueOf(p), _int.valueOf(q), mode))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def mod(x: int, m: int) -> int:
        """public static int com.google.common.math.IntMath.mod(int,int)"""
        return int._wrap(_IntMath.mod(_int.valueOf(x), _int.valueOf(m)))

    @staticmethod
    @overload
    def saturatedSubtract(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.saturatedSubtract(int,int)"""
        return int._wrap(_IntMath.saturatedSubtract(_int.valueOf(a), _int.valueOf(b)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def pow(b: int, k: int) -> int:
        """public static int com.google.common.math.IntMath.pow(int,int)"""
        return int._wrap(_IntMath.pow(_int.valueOf(b), _int.valueOf(k)))

    @staticmethod
    @overload
    def binomial(n: int, k: int) -> int:
        """public static int com.google.common.math.IntMath.binomial(int,int)"""
        return int._wrap(_IntMath.binomial(_int.valueOf(n), _int.valueOf(k)))

    @staticmethod
    @overload
    def sqrt(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.IntMath.sqrt(int,java.math.RoundingMode)"""
        return int._wrap(_IntMath.sqrt(_int.valueOf(x), mode))

    @staticmethod
    @overload
    def gcd(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.gcd(int,int)"""
        return int._wrap(_IntMath.gcd(_int.valueOf(a), _int.valueOf(b)))

    @staticmethod
    @overload
    def mean(x: int, y: int) -> int:
        """public static int com.google.common.math.IntMath.mean(int,int)"""
        return int._wrap(_IntMath.mean(_int.valueOf(x), _int.valueOf(y)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def log10(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.IntMath.log10(int,java.math.RoundingMode)"""
        return int._wrap(_IntMath.log10(_int.valueOf(x), mode))

    @staticmethod
    @overload
    def floorPowerOfTwo(x: int) -> int:
        """public static int com.google.common.math.IntMath.floorPowerOfTwo(int)"""
        return int._wrap(_IntMath.floorPowerOfTwo(_int.valueOf(x)))

    @staticmethod
    @overload
    def ceilingPowerOfTwo(x: int) -> int:
        """public static int com.google.common.math.IntMath.ceilingPowerOfTwo(int)"""
        return int._wrap(_IntMath.ceilingPowerOfTwo(_int.valueOf(x)))

    @staticmethod
    @overload
    def saturatedPow(b: int, k: int) -> int:
        """public static int com.google.common.math.IntMath.saturatedPow(int,int)"""
        return int._wrap(_IntMath.saturatedPow(_int.valueOf(b), _int.valueOf(k)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def checkedMultiply(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.checkedMultiply(int,int)"""
        return int._wrap(_IntMath.checkedMultiply(_int.valueOf(a), _int.valueOf(b)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkedPow(b: int, k: int) -> int:
        """public static int com.google.common.math.IntMath.checkedPow(int,int)"""
        return int._wrap(_IntMath.checkedPow(_int.valueOf(b), _int.valueOf(k)))

    @staticmethod
    @overload
    def checkedSubtract(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.checkedSubtract(int,int)"""
        return int._wrap(_IntMath.checkedSubtract(_int.valueOf(a), _int.valueOf(b)))

    @staticmethod
    @overload
    def factorial(n: int) -> int:
        """public static int com.google.common.math.IntMath.factorial(int)"""
        return int._wrap(_IntMath.factorial(_int.valueOf(n)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def checkedAdd(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.checkedAdd(int,int)"""
        return int._wrap(_IntMath.checkedAdd(_int.valueOf(a), _int.valueOf(b)))

    @staticmethod
    @overload
    def log2(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.IntMath.log2(int,java.math.RoundingMode)"""
        return int._wrap(_IntMath.log2(_int.valueOf(x), mode))

    @staticmethod
    @overload
    def saturatedMultiply(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.saturatedMultiply(int,int)"""
        return int._wrap(_IntMath.saturatedMultiply(_int.valueOf(a), _int.valueOf(b)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def isPrime(n: int) -> bool:
        """public static boolean com.google.common.math.IntMath.isPrime(int)"""
        return bool._wrap(_IntMath.isPrime(_int.valueOf(n)))

    @staticmethod
    @overload
    def saturatedAdd(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.saturatedAdd(int,int)"""
        return int._wrap(_IntMath.saturatedAdd(_int.valueOf(a), _int.valueOf(b)))

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
 
 
# CLASS: com.google.common.math.LinearTransformation$LinearTransformationBuilder
import com.google.common.math.LinearTransformation as _LinearTransformation_LinearTransformationBuilder
_LinearTransformationBuilder = _LinearTransformation_LinearTransformationBuilder.LinearTransformationBuilder
import com.google.common.math.LinearTransformation as _LinearTransformation
_LinearTransformation = _LinearTransformation
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinearTransformationBuilder():
    """com.google.common.math.LinearTransformation.LinearTransformationBuilder"""
 
    @staticmethod
    def _wrap(java_value: _LinearTransformationBuilder) -> 'LinearTransformationBuilder':
        return LinearTransformationBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinearTransformationBuilder):
        """
        Dynamic initializer for LinearTransformationBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinearTransformationBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinearTransformationBuilder__wrapper":
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

    @overload
    def withSlope(self, slope: float) -> 'LinearTransformation':
        """public com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation$LinearTransformationBuilder.withSlope(double)"""
        return 'LinearTransformation'._wrap(super(_LinearTransformationBuilder, self).withSlope(_double.valueOf(slope)))

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
    def and(self, x2: float, y2: float) -> 'LinearTransformation':
        """public com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation$LinearTransformationBuilder.and(double,double)"""
        return 'LinearTransformation'._wrap(super(_LinearTransformationBuilder, self).and(_double.valueOf(x2), _double.valueOf(y2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.math.DoubleMath
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import java.math.RoundingMode as RoundingMode
from builtins import bool
import com.google.common.math.DoubleMath as _DoubleMath
_DoubleMath = _DoubleMath
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DoubleMath():
    """com.google.common.math.DoubleMath"""
 
    @staticmethod
    def _wrap(java_value: _DoubleMath) -> 'DoubleMath':
        return DoubleMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleMath):
        """
        Dynamic initializer for DoubleMath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleMath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleMath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mean(values: 'Iterable') -> float:
        """public static double com.google.common.math.DoubleMath.mean(java.lang.Iterable<? extends java.lang.Number>)"""
        return float._wrap(_DoubleMath.mean(values))

    @staticmethod
    @overload
    def isPowerOfTwo(x: float) -> bool:
        """public static boolean com.google.common.math.DoubleMath.isPowerOfTwo(double)"""
        return bool._wrap(_DoubleMath.isPowerOfTwo(_double.valueOf(x)))

    @staticmethod
    @overload
    def fuzzyCompare(a: float, b: float, tolerance: float) -> int:
        """public static int com.google.common.math.DoubleMath.fuzzyCompare(double,double,double)"""
        return int._wrap(_DoubleMath.fuzzyCompare(_double.valueOf(a), _double.valueOf(b), _double.valueOf(tolerance)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def mean(values: 'Iterator') -> float:
        """public static double com.google.common.math.DoubleMath.mean(java.util.Iterator<? extends java.lang.Number>)"""
        return float._wrap(_DoubleMath.mean(values))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def fuzzyEquals(a: float, b: float, tolerance: float) -> bool:
        """public static boolean com.google.common.math.DoubleMath.fuzzyEquals(double,double,double)"""
        return bool._wrap(_DoubleMath.fuzzyEquals(_double.valueOf(a), _double.valueOf(b), _double.valueOf(tolerance)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def mean(*values: int) -> float:
        """public static double com.google.common.math.DoubleMath.mean(long...)"""
        return float._wrap(_DoubleMath.mean(values))

    @staticmethod
    @overload
    def mean(*values: float) -> float:
        """public static double com.google.common.math.DoubleMath.mean(double...)"""
        return float._wrap(_DoubleMath.mean(values))

    @staticmethod
    @overload
    def isMathematicalInteger(x: float) -> bool:
        """public static boolean com.google.common.math.DoubleMath.isMathematicalInteger(double)"""
        return bool._wrap(_DoubleMath.isMathematicalInteger(_double.valueOf(x)))

    @staticmethod
    @overload
    def log2(x: float) -> float:
        """public static double com.google.common.math.DoubleMath.log2(double)"""
        return float._wrap(_DoubleMath.log2(_double.valueOf(x)))

    @staticmethod
    @overload
    def roundToLong(x: float, mode: 'RoundingMode') -> int:
        """public static long com.google.common.math.DoubleMath.roundToLong(double,java.math.RoundingMode)"""
        return int._wrap(_DoubleMath.roundToLong(_double.valueOf(x), mode))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def roundToInt(x: float, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.DoubleMath.roundToInt(double,java.math.RoundingMode)"""
        return int._wrap(_DoubleMath.roundToInt(_double.valueOf(x), mode))

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

    @staticmethod
    @overload
    def log2(x: float, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.DoubleMath.log2(double,java.math.RoundingMode)"""
        return int._wrap(_DoubleMath.log2(_double.valueOf(x), mode))

    @staticmethod
    @overload
    def roundToBigInteger(roundToBigInteger) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.DoubleMath.roundToBigInteger(double,java.math.RoundingMode)"""
        return _transform(__double.valueOf(x), mode.DoubleMath(x: float, mode: 'RoundingMode')).'BigInteger'Value()

    @staticmethod
    @overload
    def factorial(n: int) -> float:
        """public static double com.google.common.math.DoubleMath.factorial(int)"""
        return float._wrap(_DoubleMath.factorial(_int.valueOf(n)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def mean(*values: int) -> float:
        """public static double com.google.common.math.DoubleMath.mean(int...)"""
        return float._wrap(_DoubleMath.mean(values))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.math.LinearTransformation
import com.google.common.math.LinearTransformation as _LinearTransformation
_LinearTransformation = _LinearTransformation
import com.google.common.math.LinearTransformation as _LinearTransformation_LinearTransformationBuilder
_LinearTransformationBuilder = _LinearTransformation_LinearTransformationBuilder.LinearTransformationBuilder
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinearTransformation():
    """com.google.common.math.LinearTransformation"""
 
    @staticmethod
    def _wrap(java_value: _LinearTransformation) -> 'LinearTransformation':
        return LinearTransformation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinearTransformation):
        """
        Dynamic initializer for LinearTransformation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinearTransformation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinearTransformation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def isHorizontal(self, ):
        """public abstract boolean com.google.common.math.LinearTransformation.isHorizontal()"""
        pass

    @staticmethod
    @overload
    def vertical(x: float) -> 'LinearTransformation':
        """public static com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation.vertical(double)"""
        return LinearTransformation._wrap(_LinearTransformation.vertical(_double.valueOf(x)))

    @abstractmethod
    def slope(self, ):
        """public abstract double com.google.common.math.LinearTransformation.slope()"""
        pass

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

    @staticmethod
    @overload
    def mapping(x1: float, y1: float) -> 'LinearTransformationBuilder':
        """public static com.google.common.math.LinearTransformation$LinearTransformationBuilder com.google.common.math.LinearTransformation.mapping(double,double)"""
        return LinearTransformationBuilder._wrap(_LinearTransformation.mapping(_double.valueOf(x1), _double.valueOf(y1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.google.common.math.LinearTransformation()"""
        val = _LinearTransformation()
        self.__wrapper = val

    @abstractmethod
    def transform(self, x: float):
        """public abstract double com.google.common.math.LinearTransformation.transform(double)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @abstractmethod
    def inverse(self, ):
        """public abstract com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation.inverse()"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def forNaN() -> 'LinearTransformation':
        """public static com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation.forNaN()"""
        return LinearTransformation._wrap(_LinearTransformation.forNaN())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def horizontal(y: float) -> 'LinearTransformation':
        """public static com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation.horizontal(double)"""
        return LinearTransformation._wrap(_LinearTransformation.horizontal(_double.valueOf(y)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.google.common.math.LinearTransformation()"""
        val = _LinearTransformation()
        self.__wrapper = val

    @abstractmethod
    def isVertical(self, ):
        """public abstract boolean com.google.common.math.LinearTransformation.isVertical()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())
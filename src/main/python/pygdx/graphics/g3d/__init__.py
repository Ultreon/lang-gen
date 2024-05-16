from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

 
class Shader(ABC):
    """com.badlogic.gdx.graphics.g3d.Shader"""
 
    @staticmethod
    def __wrap(java_value: __Shader) -> 'Shader':
        return Shader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Shader):
        """
        Dynamic initializer for Shader.
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
    def compareTo(self, arg0: 'Shader'):
        """public abstract int com.badlogic.gdx.graphics.g3d.Shader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.end()"""
        pass

    @abstractmethod
    def init(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.init()"""
        pass

    @abstractmethod
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        pass

    @abstractmethod
    def render(self, arg0: 'Renderable'):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def canRender(self, arg0: 'Renderable'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.Shader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Shader
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.Shader as __Shader
__Shader = __Shader
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

 
class Shader(ABC):
    """com.badlogic.gdx.graphics.g3d.Shader"""
 
    @staticmethod
    def __wrap(java_value: __Shader) -> 'Shader':
        return Shader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Shader):
        """
        Dynamic initializer for Shader.
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
    def compareTo(self, arg0: 'Shader'):
        """public abstract int com.badlogic.gdx.graphics.g3d.Shader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.end()"""
        pass

    @abstractmethod
    def init(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.init()"""
        pass

    @abstractmethod
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        pass

    @abstractmethod
    def render(self, arg0: 'Renderable'):
        """public abstract void com.badlogic.gdx.graphics.g3d.Shader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def canRender(self, arg0: 'Renderable'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.Shader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Shader 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.Mesh as __Mesh
__Mesh = __Mesh
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.ModelCache as __ModelCache_TightMeshPool
__TightMeshPool = __ModelCache_TightMeshPool.TightMeshPool
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class TightMeshPool():
    """com.badlogic.gdx.graphics.g3d.ModelCache.TightMeshPool"""
 
    @staticmethod
    def __wrap(java_value: __TightMeshPool) -> 'TightMeshPool':
        return TightMeshPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TightMeshPool):
        """
        Dynamic initializer for TightMeshPool.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool()"""
        val = __TightMeshPool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool.flush()"""
        super(TightMeshPool, self).flush()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool.dispose()"""
        super(TightMeshPool, self).dispose()

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool()"""
        val = __TightMeshPool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def obtain(self, arg0: 'VertexAttributes', arg1: int, arg2: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.ModelCache$TightMeshPool.obtain(com.badlogic.gdx.graphics.VertexAttributes,int,int)"""
        return 'graphics.Mesh'.__wrap(super(__TightMeshPool, self).obtain(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Environment
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.ToDoubleFunction as ToDoubleFunction
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Iterable as Iterable
import com.badlogic.gdx.graphics.g3d.Environment as __Environment
__Environment = __Environment
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.Attributes as __Attributes
__Attributes = __Attributes
try:
    from pygdx.graphics.g3d import environment
except ImportError:
    environment = __import_once__("pygdx.graphics.g3d.environment")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Environment():
    """com.badlogic.gdx.graphics.g3d.Environment"""
 
    @staticmethod
    def __wrap(java_value: __Environment) -> 'Environment':
        return Environment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Environment):
        """
        Dynamic initializer for Environment.
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
    def set(self, arg0: 'Attribute', arg1: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0, arg1)

    @overload
    def same(self, arg0: 'Attributes') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return bool.__wrap(super(__Attributes, self).same(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Environment()"""
        val = __Environment()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attributes.equals(java.lang.Object)"""
        return bool.__wrap(super(__Attributes, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public final java.util.Iterator<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.iterator()"""
        return 'Iterator'.__wrap(super(Attributes, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: 'Array', arg1: int) -> 'utils.Array':
        """public final com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.get(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>,long)"""
        return 'utils.Array'.__wrap(super(__Attributes, self).get(arg0, __long.valueOf(arg1)))

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.has(long)"""
        return bool.__wrap(super(__Attributes, self).has(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute', arg3: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0, arg1, arg2, arg3)

    @overload
    def add(self, arg0: 'BaseLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.BaseLight)"""
        return 'Environment'.__wrap(super(__Environment, self).add(arg0))

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.Attributes.clear()"""
        super(Attributes, self).clear()

    @overload
    def compare(self, arg0: 'Attribute', arg1: 'Attribute') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.Attributes.compare(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__Attributes, self).compare(arg0, arg1))

    @override
    @overload
    def remove(self, arg0: int):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.remove(long)"""
        super(__Attributes, self).remove(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.hashCode()"""
        return int.__wrap(super(Attributes, self).hashCode())

    @overload
    def get(self, arg0: int) -> 'Attribute':
        """public final com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.Attributes.get(long)"""
        return 'Attribute'.__wrap(super(__Attributes, self).get(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def set(self, arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0)

    @overload
    def add(self, arg0: 'DirectionalLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return 'Environment'.__wrap(super(__Environment, self).add(arg0))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.size()"""
        return int.__wrap(super(Attributes, self).size())

    @overload
    def compareTo(self, arg0: 'Attributes') -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.compareTo(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return int.__wrap(super(__Attributes, self).compareTo(arg0))

    @overload
    def remove(self, *arg0: 'environment.BaseLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.BaseLight...)"""
        return 'Environment'.__wrap(super(__Environment, self).remove(arg0))

    @overload
    def remove(self, arg0: 'PointLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.PointLight)"""
        return 'Environment'.__wrap(super(__Environment, self).remove(arg0))

    @overload
    def remove(self, arg0: 'DirectionalLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return 'Environment'.__wrap(super(__Environment, self).remove(arg0))

    @override
    @overload
    def getMask(self) -> int:
        """public final long com.badlogic.gdx.graphics.g3d.Attributes.getMask()"""
        return int.__wrap(super(Attributes, self).getMask())

    @overload
    def get(self, arg0: 'Class', arg1: int) -> 'Attribute':
        """public final <T extends com.badlogic.gdx.graphics.g3d.Attribute> T com.badlogic.gdx.graphics.g3d.Attributes.get(java.lang.Class<T>,long)"""
        return 'Attribute'.__wrap(super(__Attributes, self).get(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def sort(self):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.sort()"""
        super(Attributes, self).sort()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def add(self, arg0: 'Array') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.environment.BaseLight>)"""
        return 'Environment'.__wrap(super(__Environment, self).add(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Environment()"""
        val = __Environment()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def set(self, *arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute...)"""
        super(__Attributes, self).set(arg0)

    @overload
    def remove(self, arg0: 'Array') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.environment.BaseLight>)"""
        return 'Environment'.__wrap(super(__Environment, self).remove(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def add(self, arg0: 'SpotLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.SpotLight)"""
        return 'Environment'.__wrap(super(__Environment, self).add(arg0))

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0, arg1, arg2)

    @overload
    def add(self, *arg0: 'environment.BaseLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.BaseLight...)"""
        return 'Environment'.__wrap(super(__Environment, self).add(arg0))

    @override
    @overload
    def set(self, arg0: 'Iterable'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        super(__Attributes, self).set(arg0)

    @override
    @overload
    def attributesHash(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.attributesHash()"""
        return int.__wrap(super(Attributes, self).attributesHash())

    @overload
    def same(self, arg0: 'Attributes', arg1: bool) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes,boolean)"""
        return bool.__wrap(super(__Attributes, self).same(arg0, __boolean.valueOf(arg1)))

    @overload
    def remove(self, arg0: 'SpotLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.SpotLight)"""
        return 'Environment'.__wrap(super(__Environment, self).remove(arg0))

    @overload
    def add(self, arg0: 'PointLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.add(com.badlogic.gdx.graphics.g3d.environment.PointLight)"""
        return 'Environment'.__wrap(super(__Environment, self).add(arg0))

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
    def remove(self, arg0: 'BaseLight') -> 'Environment':
        """public com.badlogic.gdx.graphics.g3d.Environment com.badlogic.gdx.graphics.g3d.Environment.remove(com.badlogic.gdx.graphics.g3d.environment.BaseLight)"""
        return 'Environment'.__wrap(super(__Environment, self).remove(arg0))

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelBatch$RenderablePool
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.FlushablePool as __FlushablePool
__FlushablePool = __FlushablePool
import com.badlogic.gdx.graphics.g3d.Renderable as __Renderable
__Renderable = __Renderable
import com.badlogic.gdx.graphics.g3d.ModelBatch as __ModelBatch_RenderablePool
__RenderablePool = __ModelBatch_RenderablePool.RenderablePool
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RenderablePool():
    """com.badlogic.gdx.graphics.g3d.ModelBatch.RenderablePool"""
 
    @staticmethod
    def __wrap(java_value: __RenderablePool) -> 'RenderablePool':
        return RenderablePool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderablePool):
        """
        Dynamic initializer for RenderablePool.
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
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(utils.Pool, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(__utils.Pool, self).fill(__int.valueOf(arg0))

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int.__wrap(super(utils.Pool, self).getFree())

    @override
    @overload
    def obtain(self) -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.ModelBatch$RenderablePool.obtain()"""
        return 'Renderable'.__wrap(super(RenderablePool, self).obtain())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.FlushablePool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__utils.FlushablePool, self).freeAll(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def free(self, arg0: object):
        """public void com.badlogic.gdx.utils.FlushablePool.free(T)"""
        super(__utils.FlushablePool, self).free(arg0)

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

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.utils.FlushablePool.flush()"""
        super(utils.FlushablePool, self).flush() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelInstance
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.graphics.g3d.Renderable as __Renderable
__Renderable = __Renderable
import com.badlogic.gdx.graphics.g3d.model.Node as __Node
__Node = __Node
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import com.badlogic.gdx.graphics.g3d.Material as __Material
__Material = __Material
from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.ModelInstance as __ModelInstance
__ModelInstance = __ModelInstance
import java.lang.Object as __object
import java.lang.Iterable as Iterable
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import com.badlogic.gdx.graphics.g3d.model.Animation as __Animation
__Animation = __Animation
import java.lang.Long as __long
import java.lang.Float as __float
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class ModelInstance():
    """com.badlogic.gdx.graphics.g3d.ModelInstance"""
 
    @staticmethod
    def __wrap(java_value: __ModelInstance) -> 'ModelInstance':
        return ModelInstance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelInstance):
        """
        Dynamic initializer for ModelInstance.
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
    def __init__(self, arg0: 'Model', arg1: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.utils.Array<java.lang.String>)"""
        val = __ModelInstance(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.ModelInstance.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'.__wrap(super(__ModelInstance, self).calculateBoundingBox(arg0))

    @overload
    def getAnimation(self, arg0: str) -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation com.badlogic.gdx.graphics.g3d.ModelInstance.getAnimation(java.lang.String)"""
        return 'model.Animation'.__wrap(super(__ModelInstance, self).getAnimation(arg0))

    @overload
    def calculateTransforms(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.calculateTransforms()"""
        super(ModelInstance, self).calculateTransforms()

    @overload
    def getRenderable(self, arg0: 'Renderable') -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.ModelInstance.getRenderable(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'Renderable'.__wrap(super(__ModelInstance, self).getRenderable(arg0))

    @overload
    def __init__(self, arg0: 'Model', arg1: str, arg2: bool, arg3: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,java.lang.String,boolean,boolean)"""
        val = __ModelInstance(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Model', arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,float,float,float)"""
        val = __ModelInstance(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMaterial(self, arg0: str) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.ModelInstance.getMaterial(java.lang.String)"""
        return 'Material'.__wrap(super(__ModelInstance, self).getMaterial(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: str, arg3: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String,boolean)"""
        val = __ModelInstance(arg0, arg1, arg2, __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Model', arg1: str, arg2: bool, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,java.lang.String,boolean,boolean,boolean)"""
        val = __ModelInstance(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__ModelInstance, self).getRenderables(arg0, arg1)

    @overload
    def copyAnimations(self, arg0: 'Iterable', arg1: bool):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.copyAnimations(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.model.Animation>,boolean)"""
        super(__ModelInstance, self).copyAnimations(arg0, __boolean.valueOf(arg1))

    @overload
    def copy(self) -> 'ModelInstance':
        """public com.badlogic.gdx.graphics.g3d.ModelInstance com.badlogic.gdx.graphics.g3d.ModelInstance.copy()"""
        return 'ModelInstance'.__wrap(super(ModelInstance, self).copy())

    @overload
    def copyAnimations(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.copyAnimations(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.model.Animation>)"""
        super(__ModelInstance, self).copyAnimations(arg0)

    @overload
    def getAnimation(self, arg0: str, arg1: bool) -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation com.badlogic.gdx.graphics.g3d.ModelInstance.getAnimation(java.lang.String,boolean)"""
        return 'model.Animation'.__wrap(super(__ModelInstance, self).getAnimation(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ModelInstance', arg1: 'Matrix4', arg2: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.ModelInstance,com.badlogic.gdx.math.Matrix4,boolean)"""
        val = __ModelInstance(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def copyAnimation(self, arg0: 'Animation'):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.copyAnimation(com.badlogic.gdx.graphics.g3d.model.Animation)"""
        super(__ModelInstance, self).copyAnimation(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Model', *arg1: str):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,java.lang.String...)"""
        val = __ModelInstance(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.utils.Array<java.lang.String>)"""
        val = __ModelInstance(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getNode(self, arg0: str, arg1: bool, arg2: bool) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.ModelInstance.getNode(java.lang.String,boolean,boolean)"""
        return 'model.Node'.__wrap(super(__ModelInstance, self).getNode(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: str, arg3: bool, arg4: bool, arg5: bool, arg6: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String,boolean,boolean,boolean,boolean)"""
        val = __ModelInstance(arg0, arg1, arg2, __boolean.valueOf(arg3), __boolean.valueOf(arg4), __boolean.valueOf(arg5), __boolean.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', *arg2: str):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String...)"""
        val = __ModelInstance(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ModelInstance', arg1: 'Matrix4'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.ModelInstance,com.badlogic.gdx.math.Matrix4)"""
        val = __ModelInstance(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRenderable(self, arg0: 'Renderable', arg1: 'Node', arg2: 'NodePart') -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.ModelInstance.getRenderable(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.model.Node,com.badlogic.gdx.graphics.g3d.model.NodePart)"""
        return 'Renderable'.__wrap(super(__ModelInstance, self).getRenderable(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: str, arg3: bool, arg4: bool, arg5: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String,boolean,boolean,boolean)"""
        val = __ModelInstance(arg0, arg1, arg2, __boolean.valueOf(arg3), __boolean.valueOf(arg4), __boolean.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.ModelInstance.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'.__wrap(super(__ModelInstance, self).extendBoundingBox(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Vector3'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Vector3)"""
        val = __ModelInstance(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRenderable(self, arg0: 'Renderable', arg1: 'Node') -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.ModelInstance.getRenderable(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.model.Node)"""
        return 'Renderable'.__wrap(super(__ModelInstance, self).getRenderable(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4)"""
        val = __ModelInstance(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getNode(self, arg0: str) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.ModelInstance.getNode(java.lang.String)"""
        return 'model.Node'.__wrap(super(__ModelInstance, self).getNode(arg0))

    @overload
    def copyAnimation(self, arg0: 'Animation', arg1: bool):
        """public void com.badlogic.gdx.graphics.g3d.ModelInstance.copyAnimation(com.badlogic.gdx.graphics.g3d.model.Animation,boolean)"""
        super(__ModelInstance, self).copyAnimation(arg0, __boolean.valueOf(arg1))

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
    def __init__(self, arg0: 'Model', arg1: str, arg2: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,java.lang.String,boolean)"""
        val = __ModelInstance(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMaterial(self, arg0: str, arg1: bool) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.ModelInstance.getMaterial(java.lang.String,boolean)"""
        return 'Material'.__wrap(super(__ModelInstance, self).getMaterial(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: str, arg3: bool, arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,java.lang.String,boolean,boolean)"""
        val = __ModelInstance(arg0, arg1, arg2, __boolean.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Model', arg1: 'Matrix4', arg2: 'Array', arg3: bool):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model,com.badlogic.gdx.math.Matrix4,com.badlogic.gdx.utils.Array<java.lang.String>,boolean)"""
        val = __ModelInstance(arg0, arg1, arg2, __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ModelInstance'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.ModelInstance)"""
        val = __ModelInstance(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Model'):
        """public com.badlogic.gdx.graphics.g3d.ModelInstance(com.badlogic.gdx.graphics.g3d.Model)"""
        val = __ModelInstance(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getNode(self, arg0: str, arg1: bool) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.ModelInstance.getNode(java.lang.String,boolean)"""
        return 'model.Node'.__wrap(super(__ModelInstance, self).getNode(arg0, __boolean.valueOf(arg1))) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Renderable
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.Renderable as __Renderable
__Renderable = __Renderable
from builtins import int
 
class Renderable():
    """com.badlogic.gdx.graphics.g3d.Renderable"""
 
    @staticmethod
    def __wrap(java_value: __Renderable) -> 'Renderable':
        return Renderable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Renderable):
        """
        Dynamic initializer for Renderable.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Renderable()"""
        val = __Renderable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Renderable()"""
        val = __Renderable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def set(self, arg0: 'Renderable') -> 'Renderable':
        """public com.badlogic.gdx.graphics.g3d.Renderable com.badlogic.gdx.graphics.g3d.Renderable.set(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return 'Renderable'.__wrap(super(__Renderable, self).set(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Model
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
import com.badlogic.gdx.graphics.g3d.model.Node as __Node
__Node = __Node
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import com.badlogic.gdx.graphics.g3d.Material as __Material
__Material = __Material
from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Iterable as Iterable
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import com.badlogic.gdx.graphics.g3d.model.Animation as __Animation
__Animation = __Animation
import java.lang.Long as __long
try:
    from pygdx.graphics.g3d import model
except ImportError:
    model = __import_once__("pygdx.graphics.g3d.model")

import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx.graphics.g3d.model import data
except ImportError:
    data = __import_once__("pygdx.graphics.g3d.model.data")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class Model():
    """com.badlogic.gdx.graphics.g3d.Model"""
 
    @staticmethod
    def __wrap(java_value: __Model) -> 'Model':
        return Model(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Model):
        """
        Dynamic initializer for Model.
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
    def getManagedDisposables(self) -> 'Iterable':
        """public java.lang.Iterable<com.badlogic.gdx.utils.Disposable> com.badlogic.gdx.graphics.g3d.Model.getManagedDisposables()"""
        return 'Iterable'.__wrap(super(Model, self).getManagedDisposables())

    @overload
    def getAnimation(self, arg0: str) -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation com.badlogic.gdx.graphics.g3d.Model.getAnimation(java.lang.String)"""
        return 'model.Animation'.__wrap(super(__Model, self).getAnimation(arg0))

    @overload
    def __init__(self, arg0: 'ModelData'):
        """public com.badlogic.gdx.graphics.g3d.Model(com.badlogic.gdx.graphics.g3d.model.data.ModelData)"""
        val = __Model(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getNode(self, arg0: str) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.Model.getNode(java.lang.String)"""
        return 'model.Node'.__wrap(super(__Model, self).getNode(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAnimation(self, arg0: str, arg1: bool) -> 'model.Animation':
        """public com.badlogic.gdx.graphics.g3d.model.Animation com.badlogic.gdx.graphics.g3d.Model.getAnimation(java.lang.String,boolean)"""
        return 'model.Animation'.__wrap(super(__Model, self).getAnimation(arg0, __boolean.valueOf(arg1)))

    @overload
    def calculateTransforms(self):
        """public void com.badlogic.gdx.graphics.g3d.Model.calculateTransforms()"""
        super(Model, self).calculateTransforms()

    @overload
    def getNode(self, arg0: str, arg1: bool, arg2: bool) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.Model.getNode(java.lang.String,boolean,boolean)"""
        return 'model.Node'.__wrap(super(__Model, self).getNode(arg0, __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Model()"""
        val = __Model()
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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def manageDisposable(self, arg0: 'Disposable'):
        """public void com.badlogic.gdx.graphics.g3d.Model.manageDisposable(com.badlogic.gdx.utils.Disposable)"""
        super(__Model, self).manageDisposable(arg0)

    @overload
    def getMaterial(self, arg0: str) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.Model.getMaterial(java.lang.String)"""
        return 'Material'.__wrap(super(__Model, self).getMaterial(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.Model.dispose()"""
        super(Model, self).dispose()

    @overload
    def getNode(self, arg0: str, arg1: bool) -> 'model.Node':
        """public com.badlogic.gdx.graphics.g3d.model.Node com.badlogic.gdx.graphics.g3d.Model.getNode(java.lang.String,boolean)"""
        return 'model.Node'.__wrap(super(__Model, self).getNode(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'ModelData', arg1: 'TextureProvider'):
        """public com.badlogic.gdx.graphics.g3d.Model(com.badlogic.gdx.graphics.g3d.model.data.ModelData,com.badlogic.gdx.graphics.g3d.utils.TextureProvider)"""
        val = __Model(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.Model.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'.__wrap(super(__Model, self).calculateBoundingBox(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getMaterial(self, arg0: str, arg1: bool) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.Model.getMaterial(java.lang.String,boolean)"""
        return 'Material'.__wrap(super(__Model, self).getMaterial(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Model()"""
        val = __Model()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.Model.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'collision.BoundingBox'.__wrap(super(__Model, self).extendBoundingBox(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache$MeshPool
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.ModelCache as __ModelCache_MeshPool
__MeshPool = __ModelCache_MeshPool.MeshPool
from abc import abstractmethod, ABC
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
 
class MeshPool(ABC):
    """com.badlogic.gdx.graphics.g3d.ModelCache.MeshPool"""
 
    @staticmethod
    def __wrap(java_value: __MeshPool) -> 'MeshPool':
        return MeshPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MeshPool):
        """
        Dynamic initializer for MeshPool.
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
    def obtain(self, arg0: 'VertexAttributes', arg1: int, arg2: int):
        """public abstract com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.ModelCache$MeshPool.obtain(com.badlogic.gdx.graphics.VertexAttributes,int,int)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.ModelCache$MeshPool.flush()"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache$Sorter
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
import com.badlogic.gdx.graphics.g3d.ModelCache as __ModelCache_Sorter
__Sorter = __ModelCache_Sorter.Sorter
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class Sorter():
    """com.badlogic.gdx.graphics.g3d.ModelCache.Sorter"""
 
    @staticmethod
    def __wrap(java_value: __Sorter) -> 'Sorter':
        return Sorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Sorter):
        """
        Dynamic initializer for Sorter.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$Sorter()"""
        val = __Sorter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$Sorter()"""
        val = __Sorter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compare(self, arg0: 'Renderable', arg1: 'Renderable') -> int:
        """public int com.badlogic.gdx.graphics.g3d.ModelCache$Sorter.compare(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Renderable)"""
        return int.__wrap(super(__Sorter, self).compare(arg0, arg1))

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
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @override
    @overload
    def sort(self, arg0: 'Camera', arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$Sorter.sort(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__Sorter, self).sort(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelBatch
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import com.badlogic.gdx.graphics.g3d.ModelBatch as __ModelBatch
__ModelBatch = __ModelBatch
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.utils.ShaderProvider as __ShaderProvider
__ShaderProvider = __ShaderProvider
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

import com.badlogic.gdx.graphics.g3d.utils.RenderContext as __RenderContext
__RenderContext = __RenderContext
import com.badlogic.gdx.graphics.g3d.utils.RenderableSorter as __RenderableSorter
__RenderableSorter = __RenderableSorter
from builtins import int
 
class ModelBatch():
    """com.badlogic.gdx.graphics.g3d.ModelBatch"""
 
    @staticmethod
    def __wrap(java_value: __ModelBatch) -> 'ModelBatch':
        return ModelBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelBatch):
        """
        Dynamic initializer for ModelBatch.
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
 
    @overload
    def render(self, arg0: 'Iterable', arg1: 'Environment'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelBatch.render(java.lang.Iterable<T>,com.badlogic.gdx.graphics.g3d.Environment)"""
        super(__ModelBatch, self).render(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def render(self, arg0: 'Iterable', arg1: 'Environment', arg2: 'Shader'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelBatch.render(java.lang.Iterable<T>,com.badlogic.gdx.graphics.g3d.Environment,com.badlogic.gdx.graphics.g3d.Shader)"""
        super(__ModelBatch, self).render(arg0, arg1, arg2)

    @overload
    def begin(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.begin(com.badlogic.gdx.graphics.Camera)"""
        super(__ModelBatch, self).begin(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch()"""
        val = __ModelBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def render(self, arg0: 'RenderableProvider', arg1: 'Environment', arg2: 'Shader'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.RenderableProvider,com.badlogic.gdx.graphics.g3d.Environment,com.badlogic.gdx.graphics.g3d.Shader)"""
        super(__ModelBatch, self).render(arg0, arg1, arg2)

    @overload
    def render(self, arg0: 'RenderableProvider', arg1: 'Shader'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.RenderableProvider,com.badlogic.gdx.graphics.g3d.Shader)"""
        super(__ModelBatch, self).render(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def ownsRenderContext(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.ModelBatch.ownsRenderContext()"""
        return bool.__wrap(super(ModelBatch, self).ownsRenderContext())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def render(self, arg0: 'Iterable'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelBatch.render(java.lang.Iterable<T>)"""
        super(__ModelBatch, self).render(arg0)

    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__ModelBatch, self).render(arg0)

    @overload
    def __init__(self, arg0: 'RenderContext', arg1: 'ShaderProvider'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderContext,com.badlogic.gdx.graphics.g3d.utils.ShaderProvider)"""
        val = __ModelBatch(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRenderContext(self) -> 'utils.RenderContext':
        """public com.badlogic.gdx.graphics.g3d.utils.RenderContext com.badlogic.gdx.graphics.g3d.ModelBatch.getRenderContext()"""
        return 'utils.RenderContext'.__wrap(super(ModelBatch, self).getRenderContext())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(java.lang.String,java.lang.String)"""
        val = __ModelBatch(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getShaderProvider(self) -> 'utils.ShaderProvider':
        """public com.badlogic.gdx.graphics.g3d.utils.ShaderProvider com.badlogic.gdx.graphics.g3d.ModelBatch.getShaderProvider()"""
        return 'utils.ShaderProvider'.__wrap(super(ModelBatch, self).getShaderProvider())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.dispose()"""
        super(ModelBatch, self).dispose()

    @overload
    def render(self, arg0: 'RenderableProvider', arg1: 'Environment'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.RenderableProvider,com.badlogic.gdx.graphics.g3d.Environment)"""
        super(__ModelBatch, self).render(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'RenderContext'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        val = __ModelBatch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__ModelBatch, self).setCamera(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch()"""
        val = __ModelBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.graphics.g3d.ModelBatch.getCamera()"""
        return 'graphics.Camera'.__wrap(super(ModelBatch, self).getCamera())

    @overload
    def render(self, arg0: 'Iterable', arg1: 'Shader'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelBatch.render(java.lang.Iterable<T>,com.badlogic.gdx.graphics.g3d.Shader)"""
        super(__ModelBatch, self).render(arg0, arg1)

    @overload
    def __init__(self, arg0: 'RenderContext', arg1: 'RenderableSorter'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderContext,com.badlogic.gdx.graphics.g3d.utils.RenderableSorter)"""
        val = __ModelBatch(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.flush()"""
        super(ModelBatch, self).flush()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'RenderableSorter'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderableSorter)"""
        val = __ModelBatch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRenderableSorter(self) -> 'utils.RenderableSorter':
        """public com.badlogic.gdx.graphics.g3d.utils.RenderableSorter com.badlogic.gdx.graphics.g3d.ModelBatch.getRenderableSorter()"""
        return 'utils.RenderableSorter'.__wrap(super(ModelBatch, self).getRenderableSorter())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __ModelBatch(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def render(self, arg0: 'RenderableProvider'):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.render(com.badlogic.gdx.graphics.g3d.RenderableProvider)"""
        super(__ModelBatch, self).render(arg0)

    @overload
    def __init__(self, arg0: 'ShaderProvider'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.ShaderProvider)"""
        val = __ModelBatch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelBatch.end()"""
        super(ModelBatch, self).end()

    @overload
    def __init__(self, arg0: 'ShaderProvider', arg1: 'RenderableSorter'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.ShaderProvider,com.badlogic.gdx.graphics.g3d.utils.RenderableSorter)"""
        val = __ModelBatch(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'RenderContext', arg1: 'ShaderProvider', arg2: 'RenderableSorter'):
        """public com.badlogic.gdx.graphics.g3d.ModelBatch(com.badlogic.gdx.graphics.g3d.utils.RenderContext,com.badlogic.gdx.graphics.g3d.utils.ShaderProvider,com.badlogic.gdx.graphics.g3d.utils.RenderableSorter)"""
        val = __ModelBatch(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.ModelCache as __ModelCache
__ModelCache = __ModelCache
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class ModelCache():
    """com.badlogic.gdx.graphics.g3d.ModelCache"""
 
    @staticmethod
    def __wrap(java_value: __ModelCache) -> 'ModelCache':
        return ModelCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelCache):
        """
        Dynamic initializer for ModelCache.
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
 
    @overload
    def add(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.add(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__ModelCache, self).add(arg0)

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__ModelCache, self).getRenderables(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.begin()"""
        super(ModelCache, self).begin()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def begin(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.begin(com.badlogic.gdx.graphics.Camera)"""
        super(__ModelCache, self).begin(arg0)

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.end()"""
        super(ModelCache, self).end()

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'RenderableProvider'):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.add(com.badlogic.gdx.graphics.g3d.RenderableProvider)"""
        super(__ModelCache, self).add(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache.dispose()"""
        super(ModelCache, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'RenderableSorter', arg1: 'MeshPool'):
        """public com.badlogic.gdx.graphics.g3d.ModelCache(com.badlogic.gdx.graphics.g3d.utils.RenderableSorter,com.badlogic.gdx.graphics.g3d.ModelCache$MeshPool)"""
        val = __ModelCache(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Iterable'):
        """public <T extends com.badlogic.gdx.graphics.g3d.RenderableProvider> void com.badlogic.gdx.graphics.g3d.ModelCache.add(java.lang.Iterable<T>)"""
        super(__ModelCache, self).add(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelCache()"""
        val = __ModelCache()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelCache()"""
        val = __ModelCache()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Material
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.ToDoubleFunction as ToDoubleFunction
import com.badlogic.gdx.graphics.g3d.Material as __Material
__Material = __Material
from builtins import bool
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Iterable as Iterable
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.Attributes as __Attributes
__Attributes = __Attributes
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Material():
    """com.badlogic.gdx.graphics.g3d.Material"""
 
    @staticmethod
    def __wrap(java_value: __Material) -> 'Material':
        return Material(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Material):
        """
        Dynamic initializer for Material.
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
    def set(self, arg0: 'Attribute', arg1: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0, arg1)

    @overload
    def same(self, arg0: 'Attributes') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return bool.__wrap(super(__Attributes, self).same(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Material.hashCode()"""
        return int.__wrap(super(Material, self).hashCode())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public final java.util.Iterator<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.iterator()"""
        return 'Iterator'.__wrap(super(Attributes, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: 'Array', arg1: int) -> 'utils.Array':
        """public final com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.get(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>,long)"""
        return 'utils.Array'.__wrap(super(__Attributes, self).get(arg0, __long.valueOf(arg1)))

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.has(long)"""
        return bool.__wrap(super(__Attributes, self).has(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute', arg3: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, arg0: str, arg1: 'Material'):
        """public com.badlogic.gdx.graphics.g3d.Material(java.lang.String,com.badlogic.gdx.graphics.g3d.Material)"""
        val = __Material(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.Attributes.clear()"""
        super(Attributes, self).clear()

    @overload
    def compare(self, arg0: 'Attribute', arg1: 'Attribute') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.Attributes.compare(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__Attributes, self).compare(arg0, arg1))

    @override
    @overload
    def remove(self, arg0: int):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.remove(long)"""
        super(__Attributes, self).remove(__long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'Attribute':
        """public final com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.Attributes.get(long)"""
        return 'Attribute'.__wrap(super(__Attributes, self).get(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, *arg1: 'Attribute'):
        """public com.badlogic.gdx.graphics.g3d.Material(java.lang.String,com.badlogic.gdx.graphics.g3d.Attribute...)"""
        val = __Material(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def set(self, arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0)

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.Material(java.lang.String,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        val = __Material(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.size()"""
        return int.__wrap(super(Attributes, self).size())

    @overload
    def compareTo(self, arg0: 'Attributes') -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.compareTo(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return int.__wrap(super(__Attributes, self).compareTo(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Material()"""
        val = __Material()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Material.equals(java.lang.Object)"""
        return bool.__wrap(super(__Material, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Material'):
        """public com.badlogic.gdx.graphics.g3d.Material(com.badlogic.gdx.graphics.g3d.Material)"""
        val = __Material(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMask(self) -> int:
        """public final long com.badlogic.gdx.graphics.g3d.Attributes.getMask()"""
        return int.__wrap(super(Attributes, self).getMask())

    @overload
    def get(self, arg0: 'Class', arg1: int) -> 'Attribute':
        """public final <T extends com.badlogic.gdx.graphics.g3d.Attribute> T com.badlogic.gdx.graphics.g3d.Attributes.get(java.lang.Class<T>,long)"""
        return 'Attribute'.__wrap(super(__Attributes, self).get(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def sort(self):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.sort()"""
        super(Attributes, self).sort()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.Material(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        val = __Material(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def set(self, *arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute...)"""
        super(__Attributes, self).set(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def copy(self) -> 'Material':
        """public com.badlogic.gdx.graphics.g3d.Material com.badlogic.gdx.graphics.g3d.Material.copy()"""
        return 'Material'.__wrap(super(Material, self).copy())

    @override
    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0, arg1, arg2)

    @override
    @overload
    def set(self, arg0: 'Iterable'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        super(__Attributes, self).set(arg0)

    @override
    @overload
    def attributesHash(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.attributesHash()"""
        return int.__wrap(super(Attributes, self).attributesHash())

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.graphics.g3d.Material(java.lang.String)"""
        val = __Material(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def same(self, arg0: 'Attributes', arg1: bool) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes,boolean)"""
        return bool.__wrap(super(__Attributes, self).same(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Material()"""
        val = __Material()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def __init__(self, *arg0: 'Attribute'):
        """public com.badlogic.gdx.graphics.g3d.Material(com.badlogic.gdx.graphics.g3d.Attribute...)"""
        val = __Material(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Attribute
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import bool
import java.lang.Comparable as __Comparable
__Comparable = __Comparable
from builtins import int
 
class Attribute(ABC):
    """com.badlogic.gdx.graphics.g3d.Attribute"""
 
    @staticmethod
    def __wrap(java_value: __Attribute) -> 'Attribute':
        return Attribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Attribute):
        """
        Dynamic initializer for Attribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__Attribute, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.Attribute.copy()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(Attribute, self).toString())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def compareTo(self, arg0: object):
        """public abstract int java.lang.Comparable.compareTo(T)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attribute.hashCode()"""
        return int.__wrap(super(Attribute, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.Attributes
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import java.util.function.Consumer as Consumer
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.ToDoubleFunction as ToDoubleFunction
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import bool
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Iterable as Iterable
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.Attributes as __Attributes
__Attributes = __Attributes
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Attributes():
    """com.badlogic.gdx.graphics.g3d.Attributes"""
 
    @staticmethod
    def __wrap(java_value: __Attributes) -> 'Attributes':
        return Attributes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Attributes):
        """
        Dynamic initializer for Attributes.
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
    def same(self, arg0: 'Attributes') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return bool.__wrap(super(__Attributes, self).same(arg0))

    @overload
    def set(self, *arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute...)"""
        super(__Attributes, self).set(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attributes.equals(java.lang.Object)"""
        return bool.__wrap(super(__Attributes, self).equals(arg0))

    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0, arg1)

    @overload
    def set(self, arg0: 'Iterable'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(java.lang.Iterable<com.badlogic.gdx.graphics.g3d.Attribute>)"""
        super(__Attributes, self).set(arg0)

    @overload
    def attributesHash(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.attributesHash()"""
        return int.__wrap(super(Attributes, self).attributesHash())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public final java.util.Iterator<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.iterator()"""
        return 'Iterator'.__wrap(super(Attributes, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.Attributes()"""
        val = __Attributes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: 'Array', arg1: int) -> 'utils.Array':
        """public final com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute> com.badlogic.gdx.graphics.g3d.Attributes.get(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Attribute>,long)"""
        return 'utils.Array'.__wrap(super(__Attributes, self).get(arg0, __long.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute', arg3: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0, arg1, arg2, arg3)

    @overload
    def sort(self):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.sort()"""
        super(Attributes, self).sort()

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.has(long)"""
        return bool.__wrap(super(__Attributes, self).has(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def remove(self, arg0: int):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.remove(long)"""
        super(__Attributes, self).remove(__long.valueOf(arg0))

    @overload
    def compare(self, arg0: 'Attribute', arg1: 'Attribute') -> int:
        """public final int com.badlogic.gdx.graphics.g3d.Attributes.compare(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__Attributes, self).compare(arg0, arg1))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.Attributes.clear()"""
        super(Attributes, self).clear()

    @overload
    def set(self, arg0: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0)

    @overload
    def getMask(self) -> int:
        """public final long com.badlogic.gdx.graphics.g3d.Attributes.getMask()"""
        return int.__wrap(super(Attributes, self).getMask())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.hashCode()"""
        return int.__wrap(super(Attributes, self).hashCode())

    @overload
    def get(self, arg0: int) -> 'Attribute':
        """public final com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.Attributes.get(long)"""
        return 'Attribute'.__wrap(super(__Attributes, self).get(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.size()"""
        return int.__wrap(super(Attributes, self).size())

    @overload
    def set(self, arg0: 'Attribute', arg1: 'Attribute', arg2: 'Attribute'):
        """public final void com.badlogic.gdx.graphics.g3d.Attributes.set(com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute,com.badlogic.gdx.graphics.g3d.Attribute)"""
        super(__Attributes, self).set(arg0, arg1, arg2)

    @overload
    def same(self, arg0: 'Attributes', arg1: bool) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.Attributes.same(com.badlogic.gdx.graphics.g3d.Attributes,boolean)"""
        return bool.__wrap(super(__Attributes, self).same(arg0, __boolean.valueOf(arg1)))

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def compareTo(self, arg0: 'Attributes') -> int:
        """public int com.badlogic.gdx.graphics.g3d.Attributes.compareTo(com.badlogic.gdx.graphics.g3d.Attributes)"""
        return int.__wrap(super(__Attributes, self).compareTo(arg0))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

    @overload
    def get(self, arg0: 'Class', arg1: int) -> 'Attribute':
        """public final <T extends com.badlogic.gdx.graphics.g3d.Attribute> T com.badlogic.gdx.graphics.g3d.Attributes.get(java.lang.Class<T>,long)"""
        return 'Attribute'.__wrap(super(__Attributes, self).get(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.Attributes()"""
        val = __Attributes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.Mesh as __Mesh
__Mesh = __Mesh
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.ModelCache as __ModelCache_SimpleMeshPool
__SimpleMeshPool = __ModelCache_SimpleMeshPool.SimpleMeshPool
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class SimpleMeshPool():
    """com.badlogic.gdx.graphics.g3d.ModelCache.SimpleMeshPool"""
 
    @staticmethod
    def __wrap(java_value: __SimpleMeshPool) -> 'SimpleMeshPool':
        return SimpleMeshPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleMeshPool):
        """
        Dynamic initializer for SimpleMeshPool.
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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool.dispose()"""
        super(SimpleMeshPool, self).dispose()

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool()"""
        val = __SimpleMeshPool()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool()"""
        val = __SimpleMeshPool()
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

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool.flush()"""
        super(SimpleMeshPool, self).flush()

    @overload
    def obtain(self, arg0: 'VertexAttributes', arg1: int, arg2: int) -> 'graphics.Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.g3d.ModelCache$SimpleMeshPool.obtain(com.badlogic.gdx.graphics.VertexAttributes,int,int)"""
        return 'graphics.Mesh'.__wrap(super(__SimpleMeshPool, self).obtain(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.RenderableProvider
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g3d.RenderableProvider as __RenderableProvider
__RenderableProvider = __RenderableProvider
from abc import abstractmethod, ABC
 
class RenderableProvider(ABC):
    """com.badlogic.gdx.graphics.g3d.RenderableProvider"""
 
    @staticmethod
    def __wrap(java_value: __RenderableProvider) -> 'RenderableProvider':
        return RenderableProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderableProvider):
        """
        Dynamic initializer for RenderableProvider.
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
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public abstract void com.badlogic.gdx.graphics.g3d.RenderableProvider.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass
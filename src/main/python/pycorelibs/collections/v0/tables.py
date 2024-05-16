from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.collections.v0.tables.AbstractTable as __AbstractTable_SimpleCell
__SimpleCell = __AbstractTable_SimpleCell.SimpleCell
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SimpleCell(__Cell, Cell):
    """dev.ultreon.libs.collections.v0.tables.AbstractTable.SimpleCell"""
 
    @staticmethod
    def __wrap(java_value: __SimpleCell) -> 'SimpleCell':
        return SimpleCell(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleCell):
        """
        Dynamic initializer for SimpleCell.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.hashCode()"""
        return int.__wrap(super(SimpleCell, self).hashCode())

    @override
    @overload
    def getValue(self) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getValue()"""
        return object.__wrap(super(SimpleCell, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getColumn(self) -> object:
        """public C dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getColumn()"""
        return object.__wrap(super(SimpleCell, self).getColumn())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell(R,C,V)"""
        val = __SimpleCell(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.toString()"""
        return str.__wrap(super(SimpleCell, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.equals(java.lang.Object)"""
        return bool.__wrap(super(__SimpleCell, self).equals(arg0))

    @override
    @overload
    def getRow(self) -> object:
        """public R dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getRow()"""
        return object.__wrap(super(SimpleCell, self).getRow())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.collections.v0.tables.AbstractTable as __AbstractTable_SimpleCell
__SimpleCell = __AbstractTable_SimpleCell.SimpleCell
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SimpleCell(__Cell, Cell):
    """dev.ultreon.libs.collections.v0.tables.AbstractTable.SimpleCell"""
 
    @staticmethod
    def __wrap(java_value: __SimpleCell) -> 'SimpleCell':
        return SimpleCell(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleCell):
        """
        Dynamic initializer for SimpleCell.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.hashCode()"""
        return int.__wrap(super(SimpleCell, self).hashCode())

    @override
    @overload
    def getValue(self) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getValue()"""
        return object.__wrap(super(SimpleCell, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getColumn(self) -> object:
        """public C dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getColumn()"""
        return object.__wrap(super(SimpleCell, self).getColumn())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell(R,C,V)"""
        val = __SimpleCell(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.toString()"""
        return str.__wrap(super(SimpleCell, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.equals(java.lang.Object)"""
        return bool.__wrap(super(__SimpleCell, self).equals(arg0))

    @override
    @overload
    def getRow(self) -> object:
        """public R dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getRow()"""
        return object.__wrap(super(SimpleCell, self).getRow())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.Table$Index
import dev.ultreon.libs.collections.v0.tables.Table as __Table_Index
__Index = __Table_Index.Index
from abc import abstractmethod, ABC
 
class Index(ABC):
    """dev.ultreon.libs.collections.v0.tables.Table.Index"""
 
    @staticmethod
    def __wrap(java_value: __Index) -> 'Index':
        return Index(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Index):
        """
        Dynamic initializer for Index.
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
    def getRow(self, ):
        """public abstract R dev.ultreon.libs.collections.v0.tables.Table$Index.getRow()"""
        pass

    @abstractmethod
    def getColumn(self, ):
        """public abstract C dev.ultreon.libs.collections.v0.tables.Table$Index.getColumn()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.AbstractTable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Set as __Set
__Set = __Set
import java.util.Collection as Collection
from builtins import object
from abc import abstractmethod, ABC
import dev.ultreon.libs.collections.v0.tables.Table as __Table
__Table = __Table
import dev.ultreon.libs.collections.v0.tables.Table as __Table_Index
__Index = __Table_Index.Index
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.collections.v0.tables.AbstractTable as __AbstractTable
__AbstractTable = __AbstractTable
import java.lang.String as __String
__String = __String
import dev.ultreon.libs.collections.v0.tables.Table as __Table_Cell
__Cell = __Table_Cell.Cell
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class AbstractTable(ABC, __Table, Table):
    """dev.ultreon.libs.collections.v0.tables.AbstractTable"""
 
    @staticmethod
    def __wrap(java_value: __AbstractTable) -> 'AbstractTable':
        return AbstractTable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractTable):
        """
        Dynamic initializer for AbstractTable.
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
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable()"""
        val = __AbstractTable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def rowSet(self) -> 'Set':
        """public java.util.Set<R> dev.ultreon.libs.collections.v0.tables.AbstractTable.rowSet()"""
        return 'Set'.__wrap(super(AbstractTable, self).rowSet())

    @overload
    def put(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.put(R,C,V)"""
        return object.__wrap(super(__AbstractTable, self).put(arg0, arg1, arg2))

    @override
    @overload
    def toRowMap(self) -> 'Map':
        """public java.util.Map<R, java.util.Map<C, V>> dev.ultreon.libs.collections.v0.tables.AbstractTable.toRowMap()"""
        return 'Map'.__wrap(super(AbstractTable, self).toRowMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def containsRow(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsRow(R)"""
        return bool.__wrap(super(__AbstractTable, self).containsRow(arg0))

    @overload
    def rowSet(self, arg0: object) -> 'Set':
        """public java.util.Set<R> dev.ultreon.libs.collections.v0.tables.AbstractTable.rowSet(C)"""
        return 'Set'.__wrap(super(__AbstractTable, self).rowSet(arg0))

    @override
    @overload
    def columnSet(self) -> 'Set':
        """public java.util.Set<C> dev.ultreon.libs.collections.v0.tables.AbstractTable.columnSet()"""
        return 'Set'.__wrap(super(AbstractTable, self).columnSet())

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.libs.collections.v0.tables.AbstractTable.values()"""
        return 'Collection'.__wrap(super(AbstractTable, self).values())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.containsValue(V)"""
        return bool.__wrap(super(__Table, self).containsValue(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.getOrDefault(R,C,V)"""
        return object.__wrap(super(__AbstractTable, self).getOrDefault(arg0, arg1, arg2))

    @overload
    def column(self, arg0: object) -> 'Map':
        """public java.util.Map<R, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.column(C)"""
        return 'Map'.__wrap(super(__AbstractTable, self).column(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putIfPresent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfPresent(R,C,V)"""
        return object.__wrap(super(__Table, self).putIfPresent(arg0, arg1, arg2))

    @override
    @overload
    def rowSize(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable.rowSize()"""
        return int.__wrap(super(AbstractTable, self).rowSize())

    @override
    @overload
    def toColumnMap(self) -> 'Map':
        """public java.util.Map<C, java.util.Map<R, V>> dev.ultreon.libs.collections.v0.tables.AbstractTable.toColumnMap()"""
        return 'Map'.__wrap(super(AbstractTable, self).toColumnMap())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def get(self, arg0: 'Index') -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.get(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return object.__wrap(super(__AbstractTable, self).get(arg0))

    @overload
    def row(self, arg0: object) -> 'Map':
        """public java.util.Map<C, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.row(R)"""
        return 'Map'.__wrap(super(__AbstractTable, self).row(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.isEmpty()"""
        return bool.__wrap(super(AbstractTable, self).isEmpty())

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
    def clear(self):
        """public void dev.ultreon.libs.collections.v0.tables.AbstractTable.clear()"""
        super(AbstractTable, self).clear()

    @staticmethod
    @overload
    def cell(arg0: object, arg1: object, arg2: object) -> 'Cell':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table$Cell<R, C, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.cell(R,C,V)"""
        return Cell.__wrap(__AbstractTable.cell(arg0, arg1, arg2))

    @abstractmethod
    def cellSet(self, ):
        """public abstract java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Cell<R, C, V>> dev.ultreon.libs.collections.v0.tables.Table.cellSet()"""
        pass

    @overload
    def contains(self, arg0: 'Index') -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.contains(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return bool.__wrap(super(__AbstractTable, self).contains(arg0))

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.get(R,C)"""
        return object.__wrap(super(__AbstractTable, self).get(arg0, arg1))

    @overload
    def contains(self, arg0: object, arg1: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.contains(R,C)"""
        return bool.__wrap(super(__AbstractTable, self).contains(arg0, arg1))

    @override
    @overload
    def toMap(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.toMap()"""
        return 'Map'.__wrap(super(AbstractTable, self).toMap())

    @staticmethod
    @overload
    def index(arg0: object, arg1: object) -> 'Index':
        """public static <R,C> dev.ultreon.libs.collections.v0.tables.Table$Index<R, C> dev.ultreon.libs.collections.v0.tables.AbstractTable.index(R,C)"""
        return Index.__wrap(__AbstractTable.index(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable()"""
        val = __AbstractTable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def containsAll(self, arg0: 'Table') -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsAll(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return bool.__wrap(super(__AbstractTable, self).containsAll(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfAbsent(R,C,V)"""
        return object.__wrap(super(__Table, self).putIfAbsent(arg0, arg1, arg2))

    @overload
    def containsColumn(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsColumn(C)"""
        return bool.__wrap(super(__AbstractTable, self).containsColumn(arg0))

    @override
    @overload
    def columnSize(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable.columnSize()"""
        return int.__wrap(super(AbstractTable, self).columnSize())

    @overload
    def columnSet(self, arg0: object) -> 'Set':
        """public java.util.Set<C> dev.ultreon.libs.collections.v0.tables.AbstractTable.columnSet(R)"""
        return 'Set'.__wrap(super(__AbstractTable, self).columnSet(arg0))

    @override
    @overload
    def indexSet(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>> dev.ultreon.libs.collections.v0.tables.AbstractTable.indexSet()"""
        return 'Set'.__wrap(super(AbstractTable, self).indexSet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def remove(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.remove(R,C)"""
        return object.__wrap(super(__AbstractTable, self).remove(arg0, arg1)) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.collections.v0.tables.AbstractTable as __AbstractTable_SimpleIndex
__SimpleIndex = __AbstractTable_SimpleIndex.SimpleIndex
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SimpleIndex(__Index, Index):
    """dev.ultreon.libs.collections.v0.tables.AbstractTable.SimpleIndex"""
 
    @staticmethod
    def __wrap(java_value: __SimpleIndex) -> 'SimpleIndex':
        return SimpleIndex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleIndex):
        """
        Dynamic initializer for SimpleIndex.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.hashCode()"""
        return int.__wrap(super(SimpleIndex, self).hashCode())

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
    def __init__(self, arg0: object, arg1: object):
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex(R,C)"""
        val = __SimpleIndex(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRow(self) -> object:
        """public R dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.getRow()"""
        return object.__wrap(super(SimpleIndex, self).getRow())

    @override
    @overload
    def getColumn(self) -> object:
        """public C dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.getColumn()"""
        return object.__wrap(super(SimpleIndex, self).getColumn())

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
        """public java.lang.String dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.toString()"""
        return str.__wrap(super(SimpleIndex, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.equals(java.lang.Object)"""
        return bool.__wrap(super(__SimpleIndex, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.HashTable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Set as __Set
__Set = __Set
import java.util.Collection as Collection
import dev.ultreon.libs.collections.v0.tables.HashTable as __HashTable
__HashTable = __HashTable
from builtins import object
import dev.ultreon.libs.collections.v0.tables.Table as __Table
__Table = __Table
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Set as Set
import dev.ultreon.libs.collections.v0.tables.Table as __Table_Index
__Index = __Table_Index.Index
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.collections.v0.tables.AbstractTable as __AbstractTable
__AbstractTable = __AbstractTable
import java.lang.String as __String
__String = __String
import dev.ultreon.libs.collections.v0.tables.Table as __Table_Cell
__Cell = __Table_Cell.Cell
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class HashTable(__AbstractTable, AbstractTable):
    """dev.ultreon.libs.collections.v0.tables.HashTable"""
 
    @staticmethod
    def __wrap(java_value: __HashTable) -> 'HashTable':
        return HashTable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HashTable):
        """
        Dynamic initializer for HashTable.
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
    def row(self, arg0: object) -> 'Map':
        """public java.util.Map<C, V> dev.ultreon.libs.collections.v0.tables.HashTable.row(R)"""
        return 'Map'.__wrap(super(__HashTable, self).row(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.tables.HashTable()"""
        val = __HashTable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def rowSet(self, arg0: object) -> 'Set':
        """public java.util.Set<R> dev.ultreon.libs.collections.v0.tables.HashTable.rowSet(C)"""
        return 'Set'.__wrap(super(__HashTable, self).rowSet(arg0))

    @overload
    def __init__(self, arg0: 'Table'):
        """public dev.ultreon.libs.collections.v0.tables.HashTable(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        val = __HashTable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.tables.HashTable.toString()"""
        return str.__wrap(super(HashTable, self).toString())

    @overload
    def containsRow(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsRow(R)"""
        return bool.__wrap(super(__AbstractTable, self).containsRow(arg0))

    @overload
    def getOrDefault(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.HashTable.getOrDefault(R,C,V)"""
        return object.__wrap(super(__HashTable, self).getOrDefault(arg0, arg1, arg2))

    @override
    @overload
    def rowSize(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.HashTable.rowSize()"""
        return int.__wrap(super(HashTable, self).rowSize())

    @staticmethod
    @overload
    def ofRowMap(arg0: 'Map') -> 'HashTable':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.HashTable<R, C, V> dev.ultreon.libs.collections.v0.tables.HashTable.ofRowMap(java.util.Map<R, java.util.Map<C, V>>)"""
        return HashTable.__wrap(__HashTable.ofRowMap(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.containsValue(V)"""
        return bool.__wrap(super(__Table, self).containsValue(arg0))

    @overload
    def column(self, arg0: object) -> 'Map':
        """public java.util.Map<R, V> dev.ultreon.libs.collections.v0.tables.HashTable.column(C)"""
        return 'Map'.__wrap(super(__HashTable, self).column(arg0))

    @overload
    def columnSet(self, arg0: object) -> 'Set':
        """public java.util.Set<C> dev.ultreon.libs.collections.v0.tables.HashTable.columnSet(R)"""
        return 'Set'.__wrap(super(__HashTable, self).columnSet(arg0))

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.libs.collections.v0.tables.HashTable.clear()"""
        super(HashTable, self).clear()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.tables.HashTable()"""
        val = __HashTable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putIfPresent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfPresent(R,C,V)"""
        return object.__wrap(super(__Table, self).putIfPresent(arg0, arg1, arg2))

    @overload
    def contains(self, arg0: object, arg1: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.HashTable.contains(R,C)"""
        return bool.__wrap(super(__HashTable, self).contains(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def rowSet(self) -> 'Set':
        """public java.util.Set<R> dev.ultreon.libs.collections.v0.tables.HashTable.rowSet()"""
        return 'Set'.__wrap(super(HashTable, self).rowSet())

    @override
    @overload
    def indexSet(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>> dev.ultreon.libs.collections.v0.tables.HashTable.indexSet()"""
        return 'Set'.__wrap(super(HashTable, self).indexSet())

    @overload
    def get(self, arg0: 'Index') -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.get(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return object.__wrap(super(__AbstractTable, self).get(arg0))

    @override
    @overload
    def cellSet(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Cell<R, C, V>> dev.ultreon.libs.collections.v0.tables.HashTable.cellSet()"""
        return 'Set'.__wrap(super(HashTable, self).cellSet())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def ofColumnMap(arg0: 'Map') -> 'HashTable':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.HashTable<R, C, V> dev.ultreon.libs.collections.v0.tables.HashTable.ofColumnMap(java.util.Map<C, java.util.Map<R, V>>)"""
        return HashTable.__wrap(__HashTable.ofColumnMap(arg0))

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.HashTable.get(R,C)"""
        return object.__wrap(super(__HashTable, self).get(arg0, arg1))

    @override
    @overload
    def toColumnMap(self) -> 'Map':
        """public java.util.Map<C, java.util.Map<R, V>> dev.ultreon.libs.collections.v0.tables.HashTable.toColumnMap()"""
        return 'Map'.__wrap(super(HashTable, self).toColumnMap())

    @override
    @overload
    def columnSet(self) -> 'Set':
        """public java.util.Set<C> dev.ultreon.libs.collections.v0.tables.HashTable.columnSet()"""
        return 'Set'.__wrap(super(HashTable, self).columnSet())

    @staticmethod
    @overload
    def cell(arg0: object, arg1: object, arg2: object) -> 'Cell':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table$Cell<R, C, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.cell(R,C,V)"""
        return Cell.__wrap(__AbstractTable.cell(arg0, arg1, arg2))

    @override
    @overload
    def toMap(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>, V> dev.ultreon.libs.collections.v0.tables.HashTable.toMap()"""
        return 'Map'.__wrap(super(HashTable, self).toMap())

    @overload
    def contains(self, arg0: 'Index') -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.contains(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return bool.__wrap(super(__AbstractTable, self).contains(arg0))

    @staticmethod
    @overload
    def index(arg0: object, arg1: object) -> 'Index':
        """public static <R,C> dev.ultreon.libs.collections.v0.tables.Table$Index<R, C> dev.ultreon.libs.collections.v0.tables.AbstractTable.index(R,C)"""
        return Index.__wrap(__AbstractTable.index(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def put(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.HashTable.put(R,C,V)"""
        return object.__wrap(super(__HashTable, self).put(arg0, arg1, arg2))

    @override
    @overload
    def columnSize(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.HashTable.columnSize()"""
        return int.__wrap(super(HashTable, self).columnSize())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def remove(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.HashTable.remove(R,C)"""
        return object.__wrap(super(__HashTable, self).remove(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.HashTable.isEmpty()"""
        return bool.__wrap(super(HashTable, self).isEmpty())

    @overload
    def containsAll(self, arg0: 'Table') -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsAll(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return bool.__wrap(super(__AbstractTable, self).containsAll(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.libs.collections.v0.tables.HashTable.values()"""
        return 'Collection'.__wrap(super(HashTable, self).values())

    @staticmethod
    @overload
    def of(arg0: 'Table') -> 'HashTable':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.HashTable<R, C, V> dev.ultreon.libs.collections.v0.tables.HashTable.of(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return HashTable.__wrap(__HashTable.of(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfAbsent(R,C,V)"""
        return object.__wrap(super(__Table, self).putIfAbsent(arg0, arg1, arg2))

    @overload
    def containsColumn(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsColumn(C)"""
        return bool.__wrap(super(__AbstractTable, self).containsColumn(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toRowMap(self) -> 'Map':
        """public java.util.Map<R, java.util.Map<C, V>> dev.ultreon.libs.collections.v0.tables.HashTable.toRowMap()"""
        return 'Map'.__wrap(super(HashTable, self).toRowMap()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.Table$Cell
import dev.ultreon.libs.collections.v0.tables.Table as __Table_Cell
__Cell = __Table_Cell.Cell
from abc import abstractmethod, ABC
 
class Cell(ABC, __Index, Index):
    """dev.ultreon.libs.collections.v0.tables.Table.Cell"""
 
    @staticmethod
    def __wrap(java_value: __Cell) -> 'Cell':
        return Cell(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Cell):
        """
        Dynamic initializer for Cell.
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
    def getRow(self, ):
        """public abstract R dev.ultreon.libs.collections.v0.tables.Table$Cell.getRow()"""
        pass

    @abstractmethod
    def getValue(self, ):
        """public abstract V dev.ultreon.libs.collections.v0.tables.Table$Cell.getValue()"""
        pass

    @abstractmethod
    def getColumn(self, ):
        """public abstract C dev.ultreon.libs.collections.v0.tables.Table$Cell.getColumn()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.Tables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.collections.v0.tables.Tables as __Tables
__Tables = __Tables
import dev.ultreon.libs.collections.v0.tables.Table as __Table
__Table = __Table
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Tables():
    """dev.ultreon.libs.collections.v0.tables.Tables"""
 
    @staticmethod
    def __wrap(java_value: __Tables) -> 'Tables':
        return Tables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Tables):
        """
        Dynamic initializer for Tables.
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
    def unmodifiableTable(arg0: 'Table') -> 'Table':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table<R, C, V> dev.ultreon.libs.collections.v0.tables.Tables.unmodifiableTable(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return Table.__wrap(__Tables.unmodifiableTable(arg0))

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

    @staticmethod
    @overload
    def hashTableOf(arg0: 'Table') -> 'Table':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table<R, C, V> dev.ultreon.libs.collections.v0.tables.Tables.hashTableOf(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return Table.__wrap(__Tables.hashTableOf(arg0))

    @staticmethod
    @overload
    def emptyTable() -> 'Table':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table<R, C, V> dev.ultreon.libs.collections.v0.tables.Tables.emptyTable()"""
        return Table.__wrap(__Tables.emptyTable())

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
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.Table
import java.lang.Object as __object
import java.lang.Object as __Object
__Object = __Object
from abc import abstractmethod, ABC
from builtins import object
from builtins import bool
import dev.ultreon.libs.collections.v0.tables.Table as __Table
__Table = __Table
 
class Table(ABC):
    """dev.ultreon.libs.collections.v0.tables.Table"""
 
    @staticmethod
    def __wrap(java_value: __Table) -> 'Table':
        return Table(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Table):
        """
        Dynamic initializer for Table.
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
    def row(self, arg0: object):
        """public abstract java.util.Map<C, V> dev.ultreon.libs.collections.v0.tables.Table.row(R)"""
        pass

    @abstractmethod
    def toRowMap(self, ):
        """public abstract java.util.Map<R, java.util.Map<C, V>> dev.ultreon.libs.collections.v0.tables.Table.toRowMap()"""
        pass

    @staticmethod
    @overload
    def copyOf(arg0: 'Table') -> 'Table':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table<R, C, V> dev.ultreon.libs.collections.v0.tables.Table.copyOf(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return Table.__wrap(__Table.copyOf(arg0))

    @abstractmethod
    def columnSet(self, arg0: object):
        """public abstract java.util.Set<C> dev.ultreon.libs.collections.v0.tables.Table.columnSet(R)"""
        pass

    @overload
    def contains(self, arg0: 'Index') -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.contains(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return bool.__wrap(super(__Table, self).contains(arg0))

    @abstractmethod
    def columnSize(self, ):
        """public abstract int dev.ultreon.libs.collections.v0.tables.Table.columnSize()"""
        pass

    @overload
    def get(self, arg0: 'Index') -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.get(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return object.__wrap(super(__Table, self).get(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.containsValue(V)"""
        return bool.__wrap(super(__Table, self).containsValue(arg0))

    @abstractmethod
    def rowSize(self, ):
        """public abstract int dev.ultreon.libs.collections.v0.tables.Table.rowSize()"""
        pass

    @abstractmethod
    def get(self, arg0: object, arg1: object):
        """public abstract V dev.ultreon.libs.collections.v0.tables.Table.get(R,C)"""
        pass

    @overload
    def putIfPresent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfPresent(R,C,V)"""
        return object.__wrap(super(__Table, self).putIfPresent(arg0, arg1, arg2))

    @abstractmethod
    def indexSet(self, ):
        """public abstract java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>> dev.ultreon.libs.collections.v0.tables.Table.indexSet()"""
        pass

    @abstractmethod
    def getOrDefault(self, arg0: object, arg1: object, arg2: object):
        """public abstract V dev.ultreon.libs.collections.v0.tables.Table.getOrDefault(R,C,V)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Table'):
        """public abstract boolean dev.ultreon.libs.collections.v0.tables.Table.containsAll(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void dev.ultreon.libs.collections.v0.tables.Table.clear()"""
        pass

    @abstractmethod
    def column(self, arg0: object):
        """public abstract java.util.Map<R, V> dev.ultreon.libs.collections.v0.tables.Table.column(C)"""
        pass

    @overload
    def containsColumn(self, arg0: object) -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.containsColumn(C)"""
        return bool.__wrap(super(__Table, self).containsColumn(arg0))

    @abstractmethod
    def cellSet(self, ):
        """public abstract java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Cell<R, C, V>> dev.ultreon.libs.collections.v0.tables.Table.cellSet()"""
        pass

    @abstractmethod
    def contains(self, arg0: object, arg1: object):
        """public abstract boolean dev.ultreon.libs.collections.v0.tables.Table.contains(R,C)"""
        pass

    @overload
    def containsRow(self, arg0: object) -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.containsRow(R)"""
        return bool.__wrap(super(__Table, self).containsRow(arg0))

    @abstractmethod
    def put(self, arg0: object, arg1: object, arg2: object):
        """public abstract V dev.ultreon.libs.collections.v0.tables.Table.put(R,C,V)"""
        pass

    @abstractmethod
    def toMap(self, ):
        """public abstract java.util.Map<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>, V> dev.ultreon.libs.collections.v0.tables.Table.toMap()"""
        pass

    @abstractmethod
    def toColumnMap(self, ):
        """public abstract java.util.Map<C, java.util.Map<R, V>> dev.ultreon.libs.collections.v0.tables.Table.toColumnMap()"""
        pass

    @abstractmethod
    def columnSet(self, ):
        """public abstract java.util.Set<C> dev.ultreon.libs.collections.v0.tables.Table.columnSet()"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfAbsent(R,C,V)"""
        return object.__wrap(super(__Table, self).putIfAbsent(arg0, arg1, arg2))

    @abstractmethod
    def remove(self, arg0: object, arg1: object):
        """public abstract V dev.ultreon.libs.collections.v0.tables.Table.remove(R,C)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> dev.ultreon.libs.collections.v0.tables.Table.values()"""
        pass

    @abstractmethod
    def rowSet(self, arg0: object):
        """public abstract java.util.Set<R> dev.ultreon.libs.collections.v0.tables.Table.rowSet(C)"""
        pass

    @abstractmethod
    def rowSet(self, ):
        """public abstract java.util.Set<R> dev.ultreon.libs.collections.v0.tables.Table.rowSet()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean dev.ultreon.libs.collections.v0.tables.Table.isEmpty()"""
        pass
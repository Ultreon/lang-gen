from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
import dev.ultreon.libs.collections.v0.tables.AbstractTable as _AbstractTable_SimpleCell
_SimpleCell = _AbstractTable_SimpleCell.SimpleCell
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleCell():
    """dev.ultreon.libs.collections.v0.tables.AbstractTable.SimpleCell"""
 
    @staticmethod
    def _wrap(java_value: _SimpleCell) -> 'SimpleCell':
        return SimpleCell(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleCell):
        """
        Dynamic initializer for SimpleCell.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleCell__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleCell__wrapper":
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

    @override
    @overload
    def getValue(self) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getValue()"""
        return object._wrap(super(SimpleCell, self).getValue())

    @override
    @overload
    def getColumn(self) -> object:
        """public C dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getColumn()"""
        return object._wrap(super(SimpleCell, self).getColumn())

    @override
    @overload
    def getRow(self) -> object:
        """public R dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getRow()"""
        return object._wrap(super(SimpleCell, self).getRow())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.equals(java.lang.Object)"""
        return bool._wrap(super(_SimpleCell, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.hashCode()"""
        return int._wrap(super(SimpleCell, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell(R,C,V)"""
        val = _SimpleCell(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.toString()"""
        return str._wrap(super(SimpleCell, self).toString())

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
import dev.ultreon.libs.collections.v0.tables.AbstractTable as _AbstractTable_SimpleCell
_SimpleCell = _AbstractTable_SimpleCell.SimpleCell
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleCell():
    """dev.ultreon.libs.collections.v0.tables.AbstractTable.SimpleCell"""
 
    @staticmethod
    def _wrap(java_value: _SimpleCell) -> 'SimpleCell':
        return SimpleCell(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleCell):
        """
        Dynamic initializer for SimpleCell.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleCell__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleCell__wrapper":
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

    @override
    @overload
    def getValue(self) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getValue()"""
        return object._wrap(super(SimpleCell, self).getValue())

    @override
    @overload
    def getColumn(self) -> object:
        """public C dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getColumn()"""
        return object._wrap(super(SimpleCell, self).getColumn())

    @override
    @overload
    def getRow(self) -> object:
        """public R dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.getRow()"""
        return object._wrap(super(SimpleCell, self).getRow())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.equals(java.lang.Object)"""
        return bool._wrap(super(_SimpleCell, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.hashCode()"""
        return int._wrap(super(SimpleCell, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell(R,C,V)"""
        val = _SimpleCell(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell.toString()"""
        return str._wrap(super(SimpleCell, self).toString())

 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleCell 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.Table$Cell
import dev.ultreon.libs.collections.v0.tables.Table as _Table_Cell
_Cell = _Table_Cell.Cell
from abc import abstractmethod, ABC
 
class Cell():
    """dev.ultreon.libs.collections.v0.tables.Table.Cell"""
 
    @staticmethod
    def _wrap(java_value: _Cell) -> 'Cell':
        return Cell(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Cell):
        """
        Dynamic initializer for Cell.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Cell__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Cell__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.AbstractTable
from builtins import str
import dev.ultreon.libs.collections.v0.tables.Table as _Table_Index
_Index = _Table_Index.Index
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.util.Set as _Set
_Set = _Set
import dev.ultreon.libs.collections.v0.tables.AbstractTable as _AbstractTable
_AbstractTable = _AbstractTable
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.libs.collections.v0.tables.Table as _Table
_Table = _Table
import dev.ultreon.libs.collections.v0.tables.Table as _Table_Cell
_Cell = _Table_Cell.Cell
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractTable():
    """dev.ultreon.libs.collections.v0.tables.AbstractTable"""
 
    @staticmethod
    def _wrap(java_value: _AbstractTable) -> 'AbstractTable':
        return AbstractTable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractTable):
        """
        Dynamic initializer for AbstractTable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractTable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractTable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def putIfPresent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfPresent(R,C,V)"""
        return object._wrap(super(_Table, self).putIfPresent(arg0, arg1, arg2))

    @override
    @overload
    def toRowMap(self) -> 'Map':
        """public java.util.Map<R, java.util.Map<C, V>> dev.ultreon.libs.collections.v0.tables.AbstractTable.toRowMap()"""
        return 'Map'._wrap(super(AbstractTable, self).toRowMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable()"""
        val = _AbstractTable()
        self.__wrapper = val

    @overload
    def get(self, arg0: 'Index') -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.get(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return object._wrap(super(_AbstractTable, self).get(arg0))

    @overload
    def columnSet(self, arg0: object) -> 'Set':
        """public java.util.Set<C> dev.ultreon.libs.collections.v0.tables.AbstractTable.columnSet(R)"""
        return 'Set'._wrap(super(_AbstractTable, self).columnSet(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.libs.collections.v0.tables.AbstractTable.values()"""
        return 'Collection'._wrap(super(AbstractTable, self).values())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putIfAbsent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfAbsent(R,C,V)"""
        return object._wrap(super(_Table, self).putIfAbsent(arg0, arg1, arg2))

    @overload
    def put(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.put(R,C,V)"""
        return object._wrap(super(_AbstractTable, self).put(arg0, arg1, arg2))

    @override
    @overload
    def indexSet(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>> dev.ultreon.libs.collections.v0.tables.AbstractTable.indexSet()"""
        return 'Set'._wrap(super(AbstractTable, self).indexSet())

    @staticmethod
    @overload
    def cell(arg0: object, arg1: object, arg2: object) -> 'Cell':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table$Cell<R, C, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.cell(R,C,V)"""
        return Cell._wrap(_AbstractTable.cell(arg0, arg1, arg2))

    @overload
    def row(self, arg0: object) -> 'Map':
        """public java.util.Map<C, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.row(R)"""
        return 'Map'._wrap(super(_AbstractTable, self).row(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def containsAll(self, arg0: 'Table') -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsAll(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return bool._wrap(super(_AbstractTable, self).containsAll(arg0))

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.get(R,C)"""
        return object._wrap(super(_AbstractTable, self).get(arg0, arg1))

    @override
    @overload
    def clear(self):
        """public void dev.ultreon.libs.collections.v0.tables.AbstractTable.clear()"""
        super(AbstractTable, self).clear()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.isEmpty()"""
        return bool._wrap(super(AbstractTable, self).isEmpty())

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.containsValue(V)"""
        return bool._wrap(super(_Table, self).containsValue(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def index(arg0: object, arg1: object) -> 'Index':
        """public static <R,C> dev.ultreon.libs.collections.v0.tables.Table$Index<R, C> dev.ultreon.libs.collections.v0.tables.AbstractTable.index(R,C)"""
        return Index._wrap(_AbstractTable.index(arg0, arg1))

    @override
    @overload
    def rowSet(self) -> 'Set':
        """public java.util.Set<R> dev.ultreon.libs.collections.v0.tables.AbstractTable.rowSet()"""
        return 'Set'._wrap(super(AbstractTable, self).rowSet())

    @abstractmethod
    def cellSet(self, ):
        """public abstract java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Cell<R, C, V>> dev.ultreon.libs.collections.v0.tables.Table.cellSet()"""
        pass

    @overload
    def contains(self, arg0: object, arg1: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.contains(R,C)"""
        return bool._wrap(super(_AbstractTable, self).contains(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def column(self, arg0: object) -> 'Map':
        """public java.util.Map<R, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.column(C)"""
        return 'Map'._wrap(super(_AbstractTable, self).column(arg0))

    @overload
    def remove(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.remove(R,C)"""
        return object._wrap(super(_AbstractTable, self).remove(arg0, arg1))

    @override
    @overload
    def toMap(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.toMap()"""
        return 'Map'._wrap(super(AbstractTable, self).toMap())

    @overload
    def containsColumn(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsColumn(C)"""
        return bool._wrap(super(_AbstractTable, self).containsColumn(arg0))

    @overload
    def rowSet(self, arg0: object) -> 'Set':
        """public java.util.Set<R> dev.ultreon.libs.collections.v0.tables.AbstractTable.rowSet(C)"""
        return 'Set'._wrap(super(_AbstractTable, self).rowSet(arg0))

    @override
    @overload
    def columnSet(self) -> 'Set':
        """public java.util.Set<C> dev.ultreon.libs.collections.v0.tables.AbstractTable.columnSet()"""
        return 'Set'._wrap(super(AbstractTable, self).columnSet())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable()"""
        val = _AbstractTable()
        self.__wrapper = val

    @overload
    def containsRow(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsRow(R)"""
        return bool._wrap(super(_AbstractTable, self).containsRow(arg0))

    @override
    @overload
    def toColumnMap(self) -> 'Map':
        """public java.util.Map<C, java.util.Map<R, V>> dev.ultreon.libs.collections.v0.tables.AbstractTable.toColumnMap()"""
        return 'Map'._wrap(super(AbstractTable, self).toColumnMap())

    @override
    @overload
    def columnSize(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable.columnSize()"""
        return int._wrap(super(AbstractTable, self).columnSize())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getOrDefault(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.getOrDefault(R,C,V)"""
        return object._wrap(super(_AbstractTable, self).getOrDefault(arg0, arg1, arg2))

    @override
    @overload
    def rowSize(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable.rowSize()"""
        return int._wrap(super(AbstractTable, self).rowSize())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: 'Index') -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.contains(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return bool._wrap(super(_AbstractTable, self).contains(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.Table
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.libs.collections.v0.tables.Table as _Table
_Table = _Table
import java.lang.Object as _object
from abc import abstractmethod, ABC
from builtins import object
from builtins import bool
 
class Table():
    """dev.ultreon.libs.collections.v0.tables.Table"""
 
    @staticmethod
    def _wrap(java_value: _Table) -> 'Table':
        return Table(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Table):
        """
        Dynamic initializer for Table.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Table__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Table__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def putIfPresent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfPresent(R,C,V)"""
        return object._wrap(super(_Table, self).putIfPresent(arg0, arg1, arg2))

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
        return Table._wrap(_Table.copyOf(arg0))

    @abstractmethod
    def columnSet(self, arg0: object):
        """public abstract java.util.Set<C> dev.ultreon.libs.collections.v0.tables.Table.columnSet(R)"""
        pass

    @overload
    def contains(self, arg0: 'Index') -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.contains(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return bool._wrap(super(_Table, self).contains(arg0))

    @overload
    def containsColumn(self, arg0: object) -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.containsColumn(C)"""
        return bool._wrap(super(_Table, self).containsColumn(arg0))

    @abstractmethod
    def columnSize(self, ):
        """public abstract int dev.ultreon.libs.collections.v0.tables.Table.columnSize()"""
        pass

    @abstractmethod
    def rowSize(self, ):
        """public abstract int dev.ultreon.libs.collections.v0.tables.Table.rowSize()"""
        pass

    @abstractmethod
    def get(self, arg0: object, arg1: object):
        """public abstract V dev.ultreon.libs.collections.v0.tables.Table.get(R,C)"""
        pass

    @overload
    def putIfAbsent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfAbsent(R,C,V)"""
        return object._wrap(super(_Table, self).putIfAbsent(arg0, arg1, arg2))

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

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.containsValue(V)"""
        return bool._wrap(super(_Table, self).containsValue(arg0))

    @abstractmethod
    def column(self, arg0: object):
        """public abstract java.util.Map<R, V> dev.ultreon.libs.collections.v0.tables.Table.column(C)"""
        pass

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
        return bool._wrap(super(_Table, self).containsRow(arg0))

    @overload
    def get(self, arg0: 'Index') -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.get(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return object._wrap(super(_Table, self).get(arg0))

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
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.Tables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.libs.collections.v0.tables.Table as _Table
_Table = _Table
import dev.ultreon.libs.collections.v0.tables.Tables as _Tables
_Tables = _Tables
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Tables():
    """dev.ultreon.libs.collections.v0.tables.Tables"""
 
    @staticmethod
    def _wrap(java_value: _Tables) -> 'Tables':
        return Tables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Tables):
        """
        Dynamic initializer for Tables.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Tables__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Tables__wrapper":
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
    def unmodifiableTable(arg0: 'Table') -> 'Table':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table<R, C, V> dev.ultreon.libs.collections.v0.tables.Tables.unmodifiableTable(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return Table._wrap(_Tables.unmodifiableTable(arg0))

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

    @staticmethod
    @overload
    def emptyTable() -> 'Table':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table<R, C, V> dev.ultreon.libs.collections.v0.tables.Tables.emptyTable()"""
        return Table._wrap(_Tables.emptyTable())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def hashTableOf(arg0: 'Table') -> 'Table':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table<R, C, V> dev.ultreon.libs.collections.v0.tables.Tables.hashTableOf(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return Table._wrap(_Tables.hashTableOf(arg0))

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
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.HashTable
from builtins import str
import dev.ultreon.libs.collections.v0.tables.Table as _Table_Index
_Index = _Table_Index.Index
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import dev.ultreon.libs.collections.v0.tables.AbstractTable as _AbstractTable
_AbstractTable = _AbstractTable
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.libs.collections.v0.tables.Table as _Table
_Table = _Table
import dev.ultreon.libs.collections.v0.tables.HashTable as _HashTable
_HashTable = _HashTable
import dev.ultreon.libs.collections.v0.tables.Table as _Table_Cell
_Cell = _Table_Cell.Cell
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashTable():
    """dev.ultreon.libs.collections.v0.tables.HashTable"""
 
    @staticmethod
    def _wrap(java_value: _HashTable) -> 'HashTable':
        return HashTable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashTable):
        """
        Dynamic initializer for HashTable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashTable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashTable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def putIfPresent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfPresent(R,C,V)"""
        return object._wrap(super(_Table, self).putIfPresent(arg0, arg1, arg2))

    @overload
    def columnSet(self, arg0: object) -> 'Set':
        """public java.util.Set<C> dev.ultreon.libs.collections.v0.tables.HashTable.columnSet(R)"""
        return 'Set'._wrap(super(_HashTable, self).columnSet(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getOrDefault(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.HashTable.getOrDefault(R,C,V)"""
        return object._wrap(super(_HashTable, self).getOrDefault(arg0, arg1, arg2))

    @override
    @overload
    def rowSize(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.HashTable.rowSize()"""
        return int._wrap(super(HashTable, self).rowSize())

    @overload
    def get(self, arg0: 'Index') -> object:
        """public V dev.ultreon.libs.collections.v0.tables.AbstractTable.get(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return object._wrap(super(_AbstractTable, self).get(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.collections.v0.tables.HashTable()"""
        val = _HashTable()
        self.__wrapper = val

    @override
    @overload
    def toColumnMap(self) -> 'Map':
        """public java.util.Map<C, java.util.Map<R, V>> dev.ultreon.libs.collections.v0.tables.HashTable.toColumnMap()"""
        return 'Map'._wrap(super(HashTable, self).toColumnMap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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

    @staticmethod
    @overload
    def ofColumnMap(arg0: 'Map') -> 'HashTable':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.HashTable<R, C, V> dev.ultreon.libs.collections.v0.tables.HashTable.ofColumnMap(java.util.Map<C, java.util.Map<R, V>>)"""
        return HashTable._wrap(_HashTable.ofColumnMap(arg0))

    @overload
    def rowSet(self, arg0: object) -> 'Set':
        """public java.util.Set<R> dev.ultreon.libs.collections.v0.tables.HashTable.rowSet(C)"""
        return 'Set'._wrap(super(_HashTable, self).rowSet(arg0))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object, arg2: object) -> object:
        """public default V dev.ultreon.libs.collections.v0.tables.Table.putIfAbsent(R,C,V)"""
        return object._wrap(super(_Table, self).putIfAbsent(arg0, arg1, arg2))

    @overload
    def get(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.HashTable.get(R,C)"""
        return object._wrap(super(_HashTable, self).get(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.HashTable.remove(R,C)"""
        return object._wrap(super(_HashTable, self).remove(arg0, arg1))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> dev.ultreon.libs.collections.v0.tables.HashTable.values()"""
        return 'Collection'._wrap(super(HashTable, self).values())

    @staticmethod
    @overload
    def cell(arg0: object, arg1: object, arg2: object) -> 'Cell':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.Table$Cell<R, C, V> dev.ultreon.libs.collections.v0.tables.AbstractTable.cell(R,C,V)"""
        return Cell._wrap(_AbstractTable.cell(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Table'):
        """public dev.ultreon.libs.collections.v0.tables.HashTable(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        val = _HashTable(arg0)
        self.__wrapper = val

    @override
    @overload
    def columnSet(self) -> 'Set':
        """public java.util.Set<C> dev.ultreon.libs.collections.v0.tables.HashTable.columnSet()"""
        return 'Set'._wrap(super(HashTable, self).columnSet())

    @overload
    def containsAll(self, arg0: 'Table') -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsAll(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return bool._wrap(super(_AbstractTable, self).containsAll(arg0))

    @override
    @overload
    def columnSize(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.HashTable.columnSize()"""
        return int._wrap(super(HashTable, self).columnSize())

    @overload
    def column(self, arg0: object) -> 'Map':
        """public java.util.Map<R, V> dev.ultreon.libs.collections.v0.tables.HashTable.column(C)"""
        return 'Map'._wrap(super(_HashTable, self).column(arg0))

    @overload
    def row(self, arg0: object) -> 'Map':
        """public java.util.Map<C, V> dev.ultreon.libs.collections.v0.tables.HashTable.row(R)"""
        return 'Map'._wrap(super(_HashTable, self).row(arg0))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public default boolean dev.ultreon.libs.collections.v0.tables.Table.containsValue(V)"""
        return bool._wrap(super(_Table, self).containsValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.tables.HashTable.toString()"""
        return str._wrap(super(HashTable, self).toString())

    @staticmethod
    @overload
    def ofRowMap(arg0: 'Map') -> 'HashTable':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.HashTable<R, C, V> dev.ultreon.libs.collections.v0.tables.HashTable.ofRowMap(java.util.Map<R, java.util.Map<C, V>>)"""
        return HashTable._wrap(_HashTable.ofRowMap(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def index(arg0: object, arg1: object) -> 'Index':
        """public static <R,C> dev.ultreon.libs.collections.v0.tables.Table$Index<R, C> dev.ultreon.libs.collections.v0.tables.AbstractTable.index(R,C)"""
        return Index._wrap(_AbstractTable.index(arg0, arg1))

    @override
    @overload
    def indexSet(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>> dev.ultreon.libs.collections.v0.tables.HashTable.indexSet()"""
        return 'Set'._wrap(super(HashTable, self).indexSet())

    @override
    @overload
    def cellSet(self) -> 'Set':
        """public java.util.Set<dev.ultreon.libs.collections.v0.tables.Table$Cell<R, C, V>> dev.ultreon.libs.collections.v0.tables.HashTable.cellSet()"""
        return 'Set'._wrap(super(HashTable, self).cellSet())

    @overload
    def contains(self, arg0: object, arg1: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.HashTable.contains(R,C)"""
        return bool._wrap(super(_HashTable, self).contains(arg0, arg1))

    @override
    @overload
    def rowSet(self) -> 'Set':
        """public java.util.Set<R> dev.ultreon.libs.collections.v0.tables.HashTable.rowSet()"""
        return 'Set'._wrap(super(HashTable, self).rowSet())

    @overload
    def containsColumn(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsColumn(C)"""
        return bool._wrap(super(_AbstractTable, self).containsColumn(arg0))

    @override
    @overload
    def toMap(self) -> 'Map':
        """public java.util.Map<dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>, V> dev.ultreon.libs.collections.v0.tables.HashTable.toMap()"""
        return 'Map'._wrap(super(HashTable, self).toMap())

    @overload
    def containsRow(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.containsRow(R)"""
        return bool._wrap(super(_AbstractTable, self).containsRow(arg0))

    @overload
    def put(self, arg0: object, arg1: object, arg2: object) -> object:
        """public V dev.ultreon.libs.collections.v0.tables.HashTable.put(R,C,V)"""
        return object._wrap(super(_HashTable, self).put(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def of(arg0: 'Table') -> 'HashTable':
        """public static <R,C,V> dev.ultreon.libs.collections.v0.tables.HashTable<R, C, V> dev.ultreon.libs.collections.v0.tables.HashTable.of(dev.ultreon.libs.collections.v0.tables.Table<R, C, V>)"""
        return HashTable._wrap(_HashTable.of(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.collections.v0.tables.HashTable()"""
        val = _HashTable()
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.HashTable.isEmpty()"""
        return bool._wrap(super(HashTable, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def contains(self, arg0: 'Index') -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable.contains(dev.ultreon.libs.collections.v0.tables.Table$Index<R, C>)"""
        return bool._wrap(super(_AbstractTable, self).contains(arg0))

    @override
    @overload
    def toRowMap(self) -> 'Map':
        """public java.util.Map<R, java.util.Map<C, V>> dev.ultreon.libs.collections.v0.tables.HashTable.toRowMap()"""
        return 'Map'._wrap(super(HashTable, self).toRowMap())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.Table$Index
import dev.ultreon.libs.collections.v0.tables.Table as _Table_Index
_Index = _Table_Index.Index
from abc import abstractmethod, ABC
 
class Index():
    """dev.ultreon.libs.collections.v0.tables.Table.Index"""
 
    @staticmethod
    def _wrap(java_value: _Index) -> 'Index':
        return Index(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Index):
        """
        Dynamic initializer for Index.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Index__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Index__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.collections.v0.tables.AbstractTable as _AbstractTable_SimpleIndex
_SimpleIndex = _AbstractTable_SimpleIndex.SimpleIndex
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleIndex():
    """dev.ultreon.libs.collections.v0.tables.AbstractTable.SimpleIndex"""
 
    @staticmethod
    def _wrap(java_value: _SimpleIndex) -> 'SimpleIndex':
        return SimpleIndex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleIndex):
        """
        Dynamic initializer for SimpleIndex.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleIndex__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleIndex__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getRow(self) -> object:
        """public R dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.getRow()"""
        return object._wrap(super(SimpleIndex, self).getRow())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.equals(java.lang.Object)"""
        return bool._wrap(super(_SimpleIndex, self).equals(arg0))

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex(R,C)"""
        val = _SimpleIndex(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.toString()"""
        return str._wrap(super(SimpleIndex, self).toString())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.hashCode()"""
        return int._wrap(super(SimpleIndex, self).hashCode())

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
    def getColumn(self) -> object:
        """public C dev.ultreon.libs.collections.v0.tables.AbstractTable$SimpleIndex.getColumn()"""
        return object._wrap(super(SimpleIndex, self).getColumn())
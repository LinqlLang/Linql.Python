from linql_core.LinqlParameter import LinqlParameter
from src.linql_client.ALinqlSearch import ALinqlSearch
from src.linql_client.LinqlParser import LinqlParser
from src.linql_client.LinqlContext import LinqlContext
from src.linql_client.LinqlSearch import LinqlSearch
from .FileLoader import FileLoader
from typing import Self

class DataModel:
   Boolean: bool
   OneToOne: Self 

context = LinqlContext(LinqlSearch, "")
testLoader = FileLoader("../C#/Test/Linql.Test.Files/TestFiles/Smoke")

class TestLinqlParser:

   def test_EmptySearch(self):
      search: LinqlSearch[DataModel] = context.Set(DataModel)
      testLoader.ExecuteTest(search)

   def test_SimpleConstant(self):
      search: LinqlSearch[DataModel] = context.Set(DataModel)
      newSearch = search.Where(lambda r: True)
      testLoader.ExecuteTest(newSearch)

   def test_SimpleBooleanProperty(self):
      search: LinqlSearch[DataModel] = context.Set(DataModel)
      newSearch = search.Where(lambda r: r.Boolean)
      testLoader.ExecuteTest(newSearch)

   def test_BooleanNegate(self):
      search: LinqlSearch[DataModel] = context.Set(DataModel)
      newSearch = search.Where(lambda r: not r.Boolean)
      testLoader.ExecuteTest(newSearch)

   def test_SimpleBooleanPropertyChaining(self):
      search: LinqlSearch[DataModel] = context.Set(DataModel)
      newSearch = search.Where(lambda r: r.OneToOne.Boolean)
      testLoader.ExecuteTest(newSearch)
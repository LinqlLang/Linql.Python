﻿using System;
using System.Collections.Generic;
using System.Text;

namespace Linql.Core
{
    public class LinqlFunction : LinqlExpression
    {
        public string FunctionName { get; set; }

        public List<LinqlExpression> Arguments { get; set; }

        public LinqlExpression Object { get; set; }

        public LinqlFunction() { }

        public LinqlFunction(string FunctionName, List<LinqlExpression> Arguments = null) 
        {
            this.FunctionName = FunctionName;
            this.Arguments = Arguments;
        }
    }
}
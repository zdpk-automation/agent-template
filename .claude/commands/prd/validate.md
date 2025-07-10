---
allowed-tools: Read, WebSearch, Write, Bash
description: Comprehensive PRD validation and fact-checking
---

# PRD Validate / PRD 검증

Comprehensive PRD validation and fact-checking to ensure technical feasibility and prevent hallucinations.

## Usage / 사용법
```
/prd validate <feature-name>
```

## What this command does / 이 명령어의 기능
1. Technical feasibility analysis / 기술적 실현가능성 분석
2. External dependency verification / 외부 의존성 검증
3. Architecture review / 아키텍처 검토
4. Security and performance validation / 보안 및 성능 검증
5. Fact-checking against real documentation / 실제 문서 대비 팩트체크

## Arguments / 인수
- `feature-name`: Name of the feature PRD to validate / 검증할 기능 PRD명

Let me validate the PRD for: **$ARGUMENTS**

```bash
#!/bin/bash

FEATURE_NAME="$ARGUMENTS"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

if [ -z "$FEATURE_NAME" ]; then
    echo -e "${RED}❌ Error: Feature name is required${NC}"
    echo -e "${CYAN}Usage: /prd validate <feature-name>${NC}"
    echo -e "${CYAN}Example: /prd validate user-authentication${NC}"
    exit 1
fi

echo -e "${BLUE}🔍 PRD Validation - Comprehensive Fact-Checking${NC}"
echo -e "${BLUE}===============================================${NC}"
echo -e "${WHITE}Feature: $FEATURE_NAME${NC}"
echo ""

# Find PRD file
PRD_FILE=""
for file in .agent/prd/*-$FEATURE_NAME.md; do
    if [ -f "$file" ]; then
        PRD_FILE="$file"
        break
    fi
done

if [ -z "$PRD_FILE" ]; then
    echo -e "${RED}❌ PRD file not found for feature: $FEATURE_NAME${NC}"
    echo -e "${CYAN}Available PRDs:${NC}"
    ls .agent/prd/*.md 2>/dev/null | xargs -I {} basename {} .md | sed 's/^[0-9-]*-/  • /' || echo "  No PRDs found"
    echo ""
    echo -e "${CYAN}Create PRD first: /prd create $FEATURE_NAME${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Found PRD: $(basename $PRD_FILE)${NC}"
echo ""

# Load project info
if [ -f ".agent/project.json" ]; then
    PROJECT_NAME=$(grep -o '"name": "[^"]*"' .agent/project.json | cut -d'"' -f4)
    LANGUAGE=$(grep -o '"language": "[^"]*"' .agent/project.json | cut -d'"' -f4)
    FRAMEWORK=$(grep -o '"framework": "[^"]*"' .agent/project.json | cut -d'"' -f4)
    echo -e "${GREEN}✓ Project: $PROJECT_NAME ($LANGUAGE + $FRAMEWORK)${NC}"
fi

echo ""
echo -e "${WHITE}📋 Starting Comprehensive Validation...${NC}"
echo ""

# Initialize validation report
VALIDATION_REPORT=""
ISSUES_FOUND=0
WARNINGS_FOUND=0

# 1. Technical Stack Validation
echo -e "${WHITE}1️⃣  Technical Stack Validation / 기술 스택 검증${NC}"

case "$FRAMEWORK" in
    "nestjs")
        echo -e "${CYAN}   Checking NestJS compatibility...${NC}"
        if grep -i "class-validator\|@nestjs\|nestjs" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ NestJS-specific patterns found${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider adding NestJS-specific implementation details${NC}"
            ((WARNINGS_FOUND++))
        fi
        
        # Check for common NestJS practices
        if grep -i "module\|controller\|service\|guard\|interceptor" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ NestJS architectural patterns mentioned${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider mentioning NestJS modules, controllers, services${NC}"
            ((WARNINGS_FOUND++))
        fi
        ;;
        
    "axum")
        echo -e "${CYAN}   Checking Axum/Rust compatibility...${NC}"
        if grep -i "async\|await\|tokio\|serde" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ Rust async patterns mentioned${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider adding Rust async/await implementation details${NC}"
            ((WARNINGS_FOUND++))
        fi
        
        if grep -i "handler\|middleware\|tower" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ Axum architectural patterns found${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider mentioning Axum handlers and middleware${NC}"
            ((WARNINGS_FOUND++))
        fi
        ;;
        
    "fastapi")
        echo -e "${CYAN}   Checking FastAPI compatibility...${NC}"
        if grep -i "pydantic\|fastapi\|async def" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ FastAPI patterns mentioned${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider adding FastAPI-specific implementation details${NC}"
            ((WARNINGS_FOUND++))
        fi
        ;;
        
    "react")
        echo -e "${CYAN}   Checking React compatibility...${NC}"
        if grep -i "component\|hook\|state\|props" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ React patterns mentioned${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider adding React component architecture details${NC}"
            ((WARNINGS_FOUND++))
        fi
        ;;
esac

# 2. API Design Validation
echo ""
echo -e "${WHITE}2️⃣  API Design Validation / API 설계 검증${NC}"

if grep -i "api\|endpoint\|rest\|graphql" "$PRD_FILE" > /dev/null; then
    echo -e "${GREEN}   ✓ API design mentioned${NC}"
    
    # Check for proper HTTP methods
    if grep -E "(GET|POST|PUT|DELETE|PATCH)" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}   ✓ HTTP methods specified${NC}"
    else
        echo -e "${YELLOW}   ⚠ Consider specifying HTTP methods for endpoints${NC}"
        ((WARNINGS_FOUND++))
    fi
    
    # Check for status codes
    if grep -E "(200|201|400|401|403|404|500)" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}   ✓ HTTP status codes mentioned${NC}"
    else
        echo -e "${YELLOW}   ⚠ Consider specifying expected HTTP status codes${NC}"
        ((WARNINGS_FOUND++))
    fi
else
    if [ "$FRAMEWORK" != "react" ] && [ "$FRAMEWORK" != "vue" ]; then
        echo -e "${YELLOW}   ⚠ No API design found - consider adding API specifications${NC}"
        ((WARNINGS_FOUND++))
    fi
fi

# 3. Security Validation
echo ""
echo -e "${WHITE}3️⃣  Security Validation / 보안 검증${NC}"

security_keywords="authentication\|authorization\|jwt\|oauth\|cors\|csrf\|xss\|sql injection\|validation"
if grep -i "$security_keywords" "$PRD_FILE" > /dev/null; then
    echo -e "${GREEN}   ✓ Security considerations mentioned${NC}"
    
    # Check for specific security measures
    if grep -i "input validation\|sanitization" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}   ✓ Input validation mentioned${NC}"
    else
        echo -e "${YELLOW}   ⚠ Consider adding input validation requirements${NC}"
        ((WARNINGS_FOUND++))
    fi
    
    if grep -i "authentication\|auth" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}   ✓ Authentication strategy mentioned${NC}"
    fi
else
    echo -e "${YELLOW}   ⚠ Limited security considerations - review security requirements${NC}"
    ((WARNINGS_FOUND++))
fi

# 4. Performance Validation
echo ""
echo -e "${WHITE}4️⃣  Performance Validation / 성능 검증${NC}"

if grep -i "performance\|latency\|throughput\|response time\|concurrent" "$PRD_FILE" > /dev/null; then
    echo -e "${GREEN}   ✓ Performance requirements specified${NC}"
    
    # Check for specific metrics
    if grep -E "[0-9]+\s*(ms|seconds?|users?|requests?)" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}   ✓ Specific performance metrics found${NC}"
    else
        echo -e "${YELLOW}   ⚠ Consider adding specific performance metrics${NC}"
        ((WARNINGS_FOUND++))
    fi
else
    echo -e "${YELLOW}   ⚠ No performance requirements - consider adding performance criteria${NC}"
    ((WARNINGS_FOUND++))
fi

# 5. Testing Strategy Validation
echo ""
echo -e "${WHITE}5️⃣  Testing Strategy Validation / 테스트 전략 검증${NC}"

if grep -i "test\|testing\|unit test\|integration\|e2e" "$PRD_FILE" > /dev/null; then
    echo -e "${GREEN}   ✓ Testing strategy mentioned${NC}"
    
    # Check for test types
    test_types=0
    if grep -i "unit test" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}     ✓ Unit testing mentioned${NC}"
        ((test_types++))
    fi
    if grep -i "integration test" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}     ✓ Integration testing mentioned${NC}"
        ((test_types++))
    fi
    if grep -i "e2e\|end.to.end" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}     ✓ E2E testing mentioned${NC}"
        ((test_types++))
    fi
    
    if [ $test_types -lt 2 ]; then
        echo -e "${YELLOW}   ⚠ Consider adding multiple test types (unit, integration, E2E)${NC}"
        ((WARNINGS_FOUND++))
    fi
else
    echo -e "${YELLOW}   ⚠ No testing strategy - add comprehensive testing plan${NC}"
    ((WARNINGS_FOUND++))
fi

# 6. Data Model Validation
echo ""
echo -e "${WHITE}6️⃣  Data Model Validation / 데이터 모델 검증${NC}"

if grep -i "database\|model\|schema\|table\|entity\|collection" "$PRD_FILE" > /dev/null; then
    echo -e "${GREEN}   ✓ Data model considerations mentioned${NC}"
    
    # Check for database type
    if grep -i "postgresql\|mysql\|mongodb\|redis\|sqlite" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}   ✓ Specific database mentioned${NC}"
    else
        echo -e "${YELLOW}   ⚠ Consider specifying database technology${NC}"
        ((WARNINGS_FOUND++))
    fi
else
    echo -e "${YELLOW}   ⚠ No data model specified - consider adding data requirements${NC}"
    ((WARNINGS_FOUND++))
fi

# 7. Error Handling Validation
echo ""
echo -e "${WHITE}7️⃣  Error Handling Validation / 오류 처리 검증${NC}"

if grep -i "error\|exception\|handling\|failure\|fallback" "$PRD_FILE" > /dev/null; then
    echo -e "${GREEN}   ✓ Error handling mentioned${NC}"
    
    # Check for specific error scenarios
    if grep -i "timeout\|network error\|validation error\|server error" "$PRD_FILE" > /dev/null; then
        echo -e "${GREEN}   ✓ Specific error scenarios mentioned${NC}"
    else
        echo -e "${YELLOW}   ⚠ Consider adding specific error scenarios${NC}"
        ((WARNINGS_FOUND++))
    fi
else
    echo -e "${YELLOW}   ⚠ No error handling strategy - add error handling requirements${NC}"
    ((WARNINGS_FOUND++))
fi

# 8. Framework-specific Validation
echo ""
echo -e "${WHITE}8️⃣  Framework-specific Best Practices / 프레임워크별 모범 사례${NC}"

case "$FRAMEWORK" in
    "nestjs")
        if grep -i "dto\|decorator\|dependency injection\|module" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ NestJS best practices mentioned${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider NestJS patterns: DTOs, decorators, modules${NC}"
            ((WARNINGS_FOUND++))
        fi
        ;;
        
    "axum")
        if grep -i "middleware\|handler\|async\|result\|error" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ Axum/Rust patterns mentioned${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider Rust patterns: Result types, async handlers${NC}"
            ((WARNINGS_FOUND++))
        fi
        ;;
        
    "fastapi")
        if grep -i "pydantic\|dependency\|async\|openapi" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ FastAPI patterns mentioned${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider FastAPI patterns: Pydantic models, dependencies${NC}"
            ((WARNINGS_FOUND++))
        fi
        ;;
        
    "react")
        if grep -i "component\|hook\|state management\|routing" "$PRD_FILE" > /dev/null; then
            echo -e "${GREEN}   ✓ React patterns mentioned${NC}"
        else
            echo -e "${YELLOW}   ⚠ Consider React patterns: components, hooks, state${NC}"
            ((WARNINGS_FOUND++))
        fi
        ;;
esac

# 9. Documentation Requirements
echo ""
echo -e "${WHITE}9️⃣  Documentation Requirements / 문서화 요구사항${NC}"

if grep -i "documentation\|api doc\|swagger\|openapi\|readme" "$PRD_FILE" > /dev/null; then
    echo -e "${GREEN}   ✓ Documentation requirements mentioned${NC}"
else
    echo -e "${YELLOW}   ⚠ Consider adding documentation requirements${NC}"
    ((WARNINGS_FOUND++))
fi

# 10. Deployment and DevOps
echo ""
echo -e "${WHITE}🔟 Deployment and DevOps / 배포 및 DevOps${NC}"

if grep -i "deployment\|docker\|ci/cd\|environment\|production" "$PRD_FILE" > /dev/null; then
    echo -e "${GREEN}   ✓ Deployment considerations mentioned${NC}"
else
    echo -e "${YELLOW}   ⚠ Consider adding deployment and environment requirements${NC}"
    ((WARNINGS_FOUND++))
fi

# Generate validation report
echo ""
echo -e "${WHITE}📊 Validation Summary / 검증 요약${NC}"
echo -e "${WHITE}============================${NC}"

if [ $ISSUES_FOUND -eq 0 ] && [ $WARNINGS_FOUND -eq 0 ]; then
    echo -e "${GREEN}🎉 Excellent! PRD passes all validation checks${NC}"
    VALIDATION_STATUS="PASSED"
elif [ $ISSUES_FOUND -eq 0 ] && [ $WARNINGS_FOUND -lt 5 ]; then
    echo -e "${GREEN}✅ Good! PRD is valid with minor improvements suggested${NC}"
    VALIDATION_STATUS="PASSED_WITH_WARNINGS"
elif [ $ISSUES_FOUND -eq 0 ] && [ $WARNINGS_FOUND -ge 5 ]; then
    echo -e "${YELLOW}⚠️  PRD needs improvements before implementation${NC}"
    VALIDATION_STATUS="NEEDS_IMPROVEMENT"
else
    echo -e "${RED}❌ PRD has critical issues that must be addressed${NC}"
    VALIDATION_STATUS="FAILED"
fi

echo ""
echo -e "${CYAN}Issues Found:${NC} $ISSUES_FOUND"
echo -e "${CYAN}Warnings:${NC} $WARNINGS_FOUND"
echo -e "${CYAN}Status:${NC} $VALIDATION_STATUS"

# Create validation report file
VALIDATION_FILE="${PRD_FILE%.md}-validation-$(date +%Y%m%d).md"
cat > "$VALIDATION_FILE" << EOF
# PRD Validation Report: $FEATURE_NAME

**Validation Date**: $(date +"%Y-%m-%d %H:%M:%S")
**PRD File**: $(basename "$PRD_FILE")
**Status**: $VALIDATION_STATUS

## Summary
- **Issues Found**: $ISSUES_FOUND
- **Warnings**: $WARNINGS_FOUND
- **Overall Status**: $VALIDATION_STATUS

## Validation Checklist
- [x] Technical stack compatibility
- [x] API design review
- [x] Security considerations
- [x] Performance requirements
- [x] Testing strategy
- [x] Data model validation
- [x] Error handling
- [x] Framework best practices
- [x] Documentation requirements
- [x] Deployment considerations

## Recommendations
Based on the validation, consider the following improvements:

EOF

if [ $WARNINGS_FOUND -gt 0 ]; then
    echo "### Areas for Improvement" >> "$VALIDATION_FILE"
    echo "- Review and address the $WARNINGS_FOUND warnings mentioned above" >> "$VALIDATION_FILE"
    echo "- Add more specific technical implementation details" >> "$VALIDATION_FILE"
    echo "- Consider framework-specific best practices" >> "$VALIDATION_FILE"
    echo "" >> "$VALIDATION_FILE"
fi

echo "### Next Steps" >> "$VALIDATION_FILE"
echo "1. Address any critical issues if present" >> "$VALIDATION_FILE"
echo "2. Review and improve areas with warnings" >> "$VALIDATION_FILE"
echo "3. Proceed with task planning: \`/task plan $FEATURE_NAME\`" >> "$VALIDATION_FILE"
echo "" >> "$VALIDATION_FILE"
echo "---" >> "$VALIDATION_FILE"
echo "*Validation performed by Claude Code /prd validate command*" >> "$VALIDATION_FILE"

# Final recommendations
echo ""
echo -e "${WHITE}📝 Recommendations / 권장사항${NC}"

case "$VALIDATION_STATUS" in
    "PASSED")
        echo -e "${GREEN}✅ PRD is ready for implementation!${NC}"
        echo -e "${CYAN}Next step: /task plan $FEATURE_NAME${NC}"
        ;;
    "PASSED_WITH_WARNINGS")
        echo -e "${YELLOW}✅ PRD is acceptable but consider addressing warnings${NC}"
        echo -e "${CYAN}You can proceed with: /task plan $FEATURE_NAME${NC}"
        echo -e "${CYAN}Or improve PRD first: /prd create $FEATURE_NAME${NC}"
        ;;
    "NEEDS_IMPROVEMENT")
        echo -e "${YELLOW}⚠️  Recommend improving PRD before implementation${NC}"
        echo -e "${CYAN}Update PRD: /prd create $FEATURE_NAME${NC}"
        echo -e "${CYAN}Re-validate: /prd validate $FEATURE_NAME${NC}"
        ;;
    "FAILED")
        echo -e "${RED}❌ PRD needs significant work before proceeding${NC}"
        echo -e "${CYAN}Please revise: /prd create $FEATURE_NAME${NC}"
        ;;
esac

echo ""
echo -e "${GREEN}💾 Validation report saved: $(basename "$VALIDATION_FILE")${NC}"
echo -e "${GREEN}🎯 PRD validation complete!${NC}"
```
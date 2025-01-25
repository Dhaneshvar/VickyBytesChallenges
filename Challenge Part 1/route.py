from flask import request, jsonify
from main import app, db, jwt
from models import Company, CompanySchema, Tool, Section, Component, ToolSchema, ComponentSchema
from flask_jwt_extended import jwt_required, create_access_token

company_schema_serializer = CompanySchema()
companies_schema_serializer = CompanySchema(many=True)

@app.route('/home', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to  challenge !!!'})

@app.route('/register_company', methods=['POST'])
def register():
    data = request.json
    user_mail = Company.find_by_email(data.get('email'))

    if user_mail is not None:
        return jsonify({"error": "Already your registered. Email already exists"}), 400

    company = Company(name=data.get('name'), email=data.get('email'))
    company.set_password(data['password'])
    company.saveCompanyDetails_to_db()
    return company_schema_serializer.jsonify(company), 201

@app.route('/show_all_companies', methods=['GET'])
def showAllCompanies():
    companies = Company.query.all()
    return companies_schema_serializer.jsonify(companies), 200

@app.route('/find_Company_By_Id/<int:id>', methods=['GET'])
def getById(id):
    company = Company.query.get(id)
    if company is None:
        return jsonify({"error": "Company not found"}), 404
    return company_schema_serializer.jsonify(company), 200

@app.route('/find_By_Company_Email/<string:email>', methods=['GET'])
def getByEmail(email):
    company = Company.find_by_email(email)
    if company is None:
        return jsonify({"error": "Company not found"}), 404
    return company_schema_serializer.jsonify(company), 200



# ----------------------------------------------------------------------------------------

@app.route('/companyLogin', methods=['POST'])
def login():
    data = request.json
    company = Company.query.filter_by(email=data['email']).first()
    # if company and company.check_password(data['password']):
    #     token = create_access_token(identity=company.id)
    #     return jsonify(access_token=token), 200
    # return jsonify(message="Invalid credentials"), 401
    if company and company.check_password(data['password']):
        return jsonify({"messsage": "Login Success !!"}), 200
    
    return jsonify({"error": "Login Failed !!"}), 401


# ----------------------------------------------------------------------------------------

ToolSchema_serializer = ToolSchema()
ToolsSchema_serializer = ToolSchema(many=True)

@app.route('/create_tool', methods=['POST'])
# @jwt_required()
def create_tool():
    data = request.json
    tool = Tool(company_id=data['company_id'], name=data['name'], version=data['version'])
    db.session.add(tool)
    db.session.commit()
    return jsonify(message="Tool created successfully"), 201

@app.route('/show_tool', methods=['GET'])
# @jwt_required()
def show_tool():
    tools = Tool.query.all()
    return ToolsSchema_serializer.jsonify(tools), 200

@app.route('/get_tool_By_Id/<int:tool_id>', methods=['GET'])
# @jwt_required()
def get_tool_by_Id(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    return ToolSchema_serializer.jsonify(tool), 200

@app.route('/update_tool/<int:tool_id>', methods=['PUT'])
# @jwt_required()
def update_tool_By_Id(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    data = request.json
    tool.name = data['name']
    tool.version = data['version']
    db.session.commit()
    return jsonify(message="Tool updated successfully"), 200

@app.route('/delete_tool/<int:tool_id>', methods=['DELETE'])
# @jwt_required()
def delete_tool_By_Id(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    db.session.delete(tool)
    db.session.commit()
    return jsonify(message="Tool deleted successfully"), 200


# ----------------------------------------------------------------------------------------
@app.route('/publish_tools/<int:tool_id>/<string:state>', methods=['POST'])
# @jwt_required()
def publish_tool(tool_id, state):
    tool = Tool.query.get_or_404(tool_id)
    if(state == 'draft'):
        tool.state = 'draft'
    elif(state == 'live'):
        tool.state = 'live'
    db.session.commit()
    return jsonify(message=f"Tool is in {state} state"), 200


# ----------------------------------------------------------------------------------------

@app.route('/create_section', methods=['POST'])
def create_section():
    data = request.json
    new_section = Section(tool_id=data['tool_id'], name=data['name'])
    db.session.add(new_section)
    db.session.commit()
    return jsonify({"message": "Section created successfully!", "section": new_section.id}), 201

@app.route('/get_sections_By_Id/<int:id>', methods=['GET'])
def get_sections_By_Id(id):
    section = Section.query.get(id)
    if not section:
        return jsonify({"message": "Section not found"}), 404
    return jsonify({"id": section.id, "tool_id": section.tool_id, "name": section.name}), 200

@app.route('/update_section_By_Id/<int:id>', methods=['PUT'])
def update_section_By_Id(id):
    section = Section.query.get(id)
    if not section:
        return jsonify({"message": "Section not found"}), 404
    data = request.json
    section.name = data.get('name', section.name)
    db.session.commit()
    return jsonify({"message": "Section updated successfully"}), 200

@app.route('/delete_section_By_Id/<int:id>', methods=['DELETE'])
def delete_section_By_Id(id):
    section = Section.query.get(id)
    if not section:
        return jsonify({"message": "Section not found"}), 404
    db.session.delete(section)
    db.session.commit()
    return jsonify({"message": "Section deleted successfully"}), 200


# ----------------------------------------------------------------------------------------

component_schema_serializer  =  ComponentSchema()
component_all__schema_serializer = ComponentSchema(many=True)

@app.route('/create_components', methods=['POST'])
def create_component():
    data = request.json
    new_component = Component(
        section_id=data['section_id'],
        type=data['type'],
        variant=data['variant'],
        pricing=data['pricing']
    )
    db.session.add(new_component)
    db.session.commit()
    return jsonify({"message": "Component created successfully!", "component": new_component.id}), 201

@app.route('/get_component_By_Id/<int:id>', methods=['GET'])
def get_component_By_Id(id):
    component = Component.query.get(id)
    if not component:
        return jsonify({"message": "Component not found"}), 404
    return jsonify({
        "id": component.id,
        "section_id": component.section_id,
        "type": component.type,
        "variant": component.variant,
        "pricing": component.pricing
    }), 200

@app.route('/update_component_By_Id/<int:id>', methods=['PUT'])
def update_component_By_Id(id):
    component = Component.query.get(id)
    if not component:
        return jsonify({"message": "Component not found"}), 404
    data = request.json
    component.type = data.get('type', component.type)
    component.variant = data.get('variant', component.variant)
    component.pricing = data.get('pricing', component.pricing)
    db.session.commit()
    return jsonify({"message": "Component updated successfully"}), 200

@app.route('/delete_component_By_Id/<int:id>', methods=['DELETE'])
def delete_component_By_Id(id):
    component = Component.query.get(id)
    if not component:
        return jsonify({"message": "Component not found"}), 404
    db.session.delete(component)
    db.session.commit()
    return jsonify({"message": "Component deleted successfully"}), 200

@app.route('/show_all_components', methods=['GET'])
def show_all_components():
    components = Component.query.all()
    return component_all__schema_serializer.jsonify(components), 200

# ----------------------------------------------------------------------------------------
@app.route('/estimate_cost', methods=['POST'])
def calculate_cost():
    data = request.json
    total_cost = 0

    component = Component.query.get(data['id'])
    if not component:
        return jsonify({"error": f"Component with ID {id} not found"}), 404
    total_cost += component.pricing

    return jsonify({"total_cost": total_cost}), 200
# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug = True, port=5000)